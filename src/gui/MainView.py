import logging

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.spi.CarData import CarData

from src.gui.DataPanel import DataPanel

LOGGER: logging.Logger = logging.getLogger(__name__)

class MainView(QWidget):
  
  def __init__(self, parent: QWidget = None) -> None:
    LOGGER.info("Creating MainView instance")

    QWidget.__init__(self, parent)

    self.map_panel: DataPanel  = DataPanel("MAP", 0)
    self.pwr_panel: DataPanel  = DataPanel("PWR", 0)
    self.soc_panel: DataPanel  = DataPanel("SOC [%]", 0)
    self.temp_panel: DataPanel = DataPanel("TEMP [C]", 0)
    self.curr_panel: DataPanel = DataPanel("CURR [A]", 0)
    self.volt_panel: DataPanel = DataPanel("VOLT [V]", 0)

    col1: QVBoxLayout = QVBoxLayout()
    col1.setSpacing(0)
    col1.setContentsMargins(0, 0, 0, 0)
    col1.addStretch(1)
    col1.addWidget(self.map_panel, 1)
    col1.addWidget(self.pwr_panel, 1)
    col1.addStretch(1)

    col2: QVBoxLayout = QVBoxLayout()
    col2.setSpacing(0)
    col2.setContentsMargins(0, 0, 0, 0)
    col2.addWidget(self.soc_panel)
    col2.addWidget(self.temp_panel)

    col3: QVBoxLayout = QVBoxLayout()
    col3.setSpacing(0)
    col3.setContentsMargins(0, 0, 0, 0)
    col3.addStretch(1)
    col3.addWidget(self.curr_panel, 1)
    col3.addWidget(self.volt_panel, 1)
    col3.addStretch(1)

    main_layout: QHBoxLayout = QHBoxLayout(self)
    main_layout.setSpacing(0)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.addLayout(col1, 1)  
    main_layout.addLayout(col2, 2)
    main_layout.addLayout(col3, 1)

    self.setLayout(main_layout)

  @Slot(CarData)
  def update(self, data: CarData):
    LOGGER.info("MainView executing update")
    pass
    # self.map_panel.update() 
    # self.pwr_panel.update()
    # self.soc_panel.update()
    # self.temp_panel.update()
    # self.curr_panel.update()
    # self.volt_panel.update()