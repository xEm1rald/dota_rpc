import json
import sys
import asyncio

from loguru import logger

from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow
from qasync import QApplication, QEventLoop, asyncSlot, asyncClose
import qasync

from design import Ui_Form as Ui_Design
from core import Core
from classes import ConfigGSIData, ConfigGSI



class MainWindow(QMainWindow, Ui_Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tab_config.setLayout( self.verticalLayout_ofTabConfig )
        self.tab_info.setLayout( self.verticalLayout_ofTabInfo )
        self.setCentralWidget( self.tabWidget )

        # ui buttons
        self.pushButton_updateConfigGSI.clicked.connect( self.action_update_config )
        self.pushButton_runServer.clicked.connect( self.action_run_server )

        # init core
        self.core = Core()

    def get_config_gsi(self) -> ConfigGSI:
        return ConfigGSI(
            uri=self.lineEdit_uri.text(),
            timeout=self.doubleSpinBox_timeout.value(),
            buffer=self.doubleSpinBox_buffer.value(),
            throttle=self.doubleSpinBox_throttle.value(),
            heartbeat=self.doubleSpinBox_heartbeat.value(),
            data=ConfigGSIData(
                provider=int(bool(self.checkBox_provider.checkState().value)),
                player=int(bool(self.checkBox_player.checkState().value)),
                hero=int(bool(self.checkBox_hero.checkState().value)),
                map=int(bool(self.checkBox_map.checkState().value)),
                buildings=int(bool(self.checkBox_buildings.checkState().value)),
                abilities=int(bool(self.checkBox_abilities.checkState().value)),
                items=int(bool(self.checkBox_items.checkState().value)),
                draft=int(bool(self.checkBox_draft.checkState().value)),
                wearables=int(bool(self.checkBox_wearables.checkState().value))
            )
        )

    @asyncSlot()
    async def action_update_config(self):
        config = self.get_config_gsi()
        output = await self.core.update_config(config)
        if output:
            self.label_updateConfigStatus.setText("Config updated")
            await asyncio.sleep(2)
            self.label_updateConfigStatus.setText("")

    @asyncSlot()
    async def action_run_server(self):
        def wrapper():
            self.label_serverStatus.setText("ON")

        port = self.lineEdit_uri.text()
        port = port[port.rfind(":")+1:]
        port = port[:port.rfind("/")]
        port = int(port)
        asyncio.create_task(self.core.run_server(port=port, callback=wrapper))

        def wrapper(data: dict):
            scrollbar = self.textBrowser.verticalScrollBar()
            pos = scrollbar.value()
            self.textBrowser.setText(
                json.dumps(data, indent=4)
            )
            scrollbar.setValue(pos)

        await asyncio.gather(
            self.core.connect_discord_rpc(),
            self.core.connect_callback_to_data_event(callback=wrapper)
        )
        #await self.core.set_discord_rpc()
        #await self.core.connect_callback_to_data_event(callback=wrapper)

    @asyncClose
    async def closeEvent(self, event):
        """
        Close event
        """
        pass



def run():
    app = QApplication(sys.argv)

    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    window = MainWindow()
    window.show()

    qasync.run(app_close_event.wait())