import winreg
import os
import vdf
from loguru import logger



class _Regedit:
    def __init__(self, path: str):
        self.path = path

    def get(self, obj: str) -> tuple[str, str] | None:
        """:return: steam_path: str, auto_login: str"""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path)
            query_obj = winreg.QueryValueEx(key, obj)[0]
            winreg.CloseKey(key)

            return query_obj
        except WindowsError:
            return

    def set(self, obj: str, new_value: str) -> None:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, obj, 0, winreg.REG_SZ, new_value)
            winreg.CloseKey(key)
        except WindowsError:
            return


class Steam:
    REGISTRY_PATH = r"Software\Valve\Steam"
    LOCAL_LIBRARY_FOLDERS_PATH = r"steamapps\libraryfolders.vdf"

    PATH = _Regedit(REGISTRY_PATH).get("SteamPath")
    LIBRARY_FOLDERS_PATH = os.path.join(PATH, LOCAL_LIBRARY_FOLDERS_PATH)
    DOTA_GSI_PATH = os.path

    @staticmethod
    def get_app_library_path(app_id: int) -> str | None:
        with open(Steam.LIBRARY_FOLDERS_PATH) as f:
            r = vdf.loads(f.read())

        for number_of_library, library_info in r.get('libraryfolders', {}).items():
            library_apps = library_info.get('apps').items()
            if app_id in [int(app_id) for app_id, _ in library_apps]:
                return library_info.get('path')

        return None

    @staticmethod
    def print_app_info(app_id: int) -> None:
        logger.info(f'https://steamdb.info/app/{app_id}/')


if __name__ == "__main__":
    logger.success(
        Steam.get_app_library_path(570)
    )