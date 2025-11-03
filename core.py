import asyncio
import uvicorn
import random
import re
from loguru import logger
from datetime import datetime

import utils
from utils import DotaImage
from tools.dota_gsi import ClientDotaGSI
from tools.discord_rpc import DiscordRPC
from classes import ConfigGSI
from server import app, get_data



class Flag:
    def __init__(self, state: bool = False):
        self._active: bool = state

    def __bool__(self):
        return self._active

    def set(self):
        self._active = True

    def reset(self):
        self._active = False

    def decorator(self, func):
        async def wrapper(*args, **kwargs):
            if self._active:
                logger.warning(f"({func.__name__}) rejected with flag ({self})")
                return
            self.set()
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                self.reset()
        return wrapper


class Core:
    def __init__(self):
        self._server: None
        logger.success("App Core initializated.")

    FLAG_CONFIG_UPDATING: Flag = Flag()
    @FLAG_CONFIG_UPDATING.decorator
    async def update_config(self, config: ConfigGSI) -> bool:
        ClientDotaGSI.setup('pygsi', config)
        return True

    FLAG_SERVER_RUNNING: Flag = Flag()
    @FLAG_SERVER_RUNNING.decorator
    async def run_server(self, port: int, callback):
        config_uvicorn = uvicorn.Config(app, host="127.0.0.1", port=port, reload=False, log_level=30)
        server = uvicorn.Server(config_uvicorn)
        logger.success('Uvicorn running at ({}:{})', server.config.host, server.config.port)
        if callback: callback()
        await server.serve()

    FLAG_CONNECTED_TO_DATA_EVENT: Flag = Flag()
    @FLAG_CONNECTED_TO_DATA_EVENT.decorator
    async def connect_callback_to_data_event(self, callback):
        while self.FLAG_CONNECTED_TO_DATA_EVENT:
            callback(get_data())
            await asyncio.sleep(0.1)

    FLAG_DISCORD_RPC_CONNECTED: Flag = Flag()
    @FLAG_DISCORD_RPC_CONNECTED.decorator
    async def connect_discord_rpc(self):
        discord_rpc = DiscordRPC()

        wait_frequency = 1
        update_frequency = 10

        while self.FLAG_DISCORD_RPC_CONNECTED:
            data = get_data()
            if not data:
                if discord_rpc.is_connected:
                    await discord_rpc.close()
                logger.info("Waiting for match...")
                await asyncio.sleep(wait_frequency)
                continue
            else:
                try:
                    # hero name
                    hero_name = utils.get_from_dict(data, "hero.name")
                    if not hero_name:
                        raise Exception("Not enough data from GSI")
                    hero_name = hero_name.replace("npc_dota_hero_", "")

                    # ability name
                    abilities = utils.get_from_dict(data, "abilities")
                    ability_name = random.choice(list(abilities.items())[:-2])[1].get("name")
                    if not ability_name:
                        raise Exception("Not enough data from GSI")

                    # gpm xpm
                    gpm = utils.get_from_dict(data, "player.gpm")
                    xpm = utils.get_from_dict(data, "player.xpm")
                    secondary_stats = f"GPM/XPM: {gpm}/{xpm}"

                    # kda d/o
                    kills = utils.get_from_dict(data, "player.kills")
                    deaths = utils.get_from_dict(data, "player.deaths")
                    assists = utils.get_from_dict(data, "player.assists")
                    last_hits = utils.get_from_dict(data, "player.last_hits")
                    denies = utils.get_from_dict(data, "player.denies")
                    primary_stats = f"KDA: {kills}/{deaths}/{assists} | LH/DN: {last_hits}/{denies}"

                    # time
                    game_time = utils.get_from_dict(data, "map.game_time", 0)
                    game_time = int(datetime.now().timestamp()) - game_time

                except Exception as e:
                    if discord_rpc.is_connected:
                        await discord_rpc.close()
                    logger.info("Waiting for match start...")
                    await asyncio.sleep(wait_frequency)
                    continue

            try:
                if not discord_rpc.is_connected:
                    await discord_rpc.connect()

                await discord_rpc.update(
                    name="Dota 2",
                    large_image=DotaImage.hero_render_url(hero_name),
                    large_text=utils.snakecase_to_capital(hero_name),
                    small_image=DotaImage.ability_url(ability_name),
                    small_text=utils.snakecase_to_capital(ability_name.replace(hero_name, "")),
                    start=game_time,
                    details=primary_stats,
                    state=secondary_stats
                )
            except Exception as e:
                logger.debug(e)

            await asyncio.sleep(update_frequency)

        await discord_rpc.close()


