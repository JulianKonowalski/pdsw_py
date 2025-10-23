from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.spi.CarData import CarData

from src.gui.DataPanel import DataPanel

class MainView(QWidget):
  
  def __init__(self, parent: QWidget = None) -> None:
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
    self.map_panel.updateData(data.getValue("DIAL_0")) 
    self.pwr_panel.updateData(data.getValue("DIAL_1"))
    self.soc_panel.updateData(data.getValue("SOC"))
    self.temp_panel.updateData(data.getValue("TEMP"))
    self.curr_panel.updateData(data.getValue("CURR_LSB"))
    self.volt_panel.updateData(data.getValue("VOLT_LSB"))