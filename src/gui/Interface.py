import os
import pathlib
import logging

from PySide6.QtWidgets import QApplication

from src.gui.MainWindow import MainWindow

LOGGER: logging.Logger = logging.getLogger(__name__)
STYLESHEET_FILE: str = os.path.join(pathlib.Path(__file__).parent.resolve(), "Interface.qss")

class Interface(QApplication):
  
  def __init__(self) -> None:
    LOGGER.info("Creating interface instance")
    QApplication.__init__(self)
    with open(STYLESHEET_FILE, "r") as stylesheet:
      self.setStyleSheet(stylesheet.read())

    self.main_window: MainWindow = MainWindow()
    self.main_window.setFixedSize(800, 440)
    self.main_window.show()

  def run(self) -> int:
    LOGGER.info("Starting interface instance")
    self.main_window.dataRequest.emit()
    return self.exec()