import json
import os
import vdf
from loguru import logger

from tools.steam import Steam
from classes import ConfigGSI, ConfigGSIData


class ClientDotaGSI:
    APP_ID = 570
    LOCAL_PATH = r"steamapps\common\dota 2 beta\game\dota\cfg\gamestate_integration"

    @staticmethod
    def setup(name: str, config: ConfigGSI):
        ClientDotaGSI._update_config(name, config)

    @staticmethod
    def get_path() -> str:
        app_library_path = Steam.get_app_library_path(ClientDotaGSI.APP_ID)
        return os.path.join(app_library_path, ClientDotaGSI.LOCAL_PATH)

    @staticmethod
    def _update_config(title: str, config: ConfigGSI) -> None:
        template = f"gamestate_integration_{title}.cfg"

        config = {title: config.to_dict()}

        path = os.path.join(ClientDotaGSI.get_path(), template)
        with open(path, 'w') as f:
            f.write(
                vdf.dumps(config, pretty=True)
            )
        logger.success("Config updated ({}) ", template)



if __name__ == '__main__':
    config = ConfigGSI(
        'http://localhost:8070/',
        data=ConfigGSIData(
            map=1, player=1, hero=1, items=1, draft=1
        )
    )

    ClientDotaGSI.setup('pygsi', config)