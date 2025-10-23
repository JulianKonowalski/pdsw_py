import logging

from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QMainWindow

from src.spi.SpiBus import SpiBus
from src.spi.CarData import CarData

from src.gui.MainView import MainView

LOGGER: logging.Logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):

  dataUpdated: Signal = Signal(CarData)
  dataRequest: Signal = Signal(None)

  def __init__(self) -> None:
    LOGGER.info("Creating MainWindow instance")
    QMainWindow.__init__(self)
    
    self.spi_bus: SpiBus = SpiBus()
    self.main_view: MainView = MainView(self)

    self.dataRequest.connect(self.onDataRequest, type=Qt.ConnectionType.QueuedConnection)
    self.dataUpdated.connect(self.main_view.update)

    self.setCentralWidget(self.main_view)

  @Slot(None)
  def onDataRequest(self) -> None:
    LOGGER.info("MainWindow executing onDataRequest")
    car_data: CarData = self.spi_bus.getCarData()
    self.dataUpdated.emit(car_data)
    self.dataRequest.emit()