from pypresence import AioPresence
from loguru import logger

class DiscordRPC(AioPresence):
    CLIENT_ID = "1290764180822954035"
    def __init__(self):
        super().__init__(self.CLIENT_ID)
        self.is_connected: bool = False

    async def connect(self):
        if self.is_connected:
            logger.warning("DiscordRPC already connected. Cant connect.")
            return

        await super().connect()
        logger.success("DiscordRPC connected.")
        self.is_connected = True

    async def close(self):
        if not self.is_connected:
            logger.warning("DiscordRPC is not connected. Cant close.")
            return

        await super().clear()
        logger.success("DiscordRPC closed.")
        self.is_connected = False