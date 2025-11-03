from typing import Any


class DotaImage:
    RENDERS_URL = r"https://cdn.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/{}.png" # https://cdn.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/antimage.png
    CROPS_URL = r"https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/crops/{}.png" # https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/crops/antimage.png
    HERO_URL = r"https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/{}.png" # https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/antimage.png
    ABILITY_URL = r"https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/{}.png" # antimage_mana_void # 1:1 spell icon

    @staticmethod
    def hero_render_url(hero_name: str) -> str:
        return DotaImage.RENDERS_URL.format(hero_name)

    @staticmethod
    def hero_corp_url(hero_name: str) -> str:
        return DotaImage.CROPS_URL.format(hero_name)

    @staticmethod
    def hero_url(hero_name: str) -> str:
        return DotaImage.HERO_URL.format(hero_name)

    @staticmethod
    def ability_url(hero_name: str) -> str:
        return DotaImage.ABILITY_URL.format(hero_name)


def snakecase_to_capital(name: str) -> str:
    return " ".join(i.capitalize() for i in name.split("_"))

def get_from_dict(data: dict, expression: str, default = None) -> Any | None:
    for ex in expression.split("."):
        res = data.get(ex)
        if res is None:
            return default
        data = res
    return data
