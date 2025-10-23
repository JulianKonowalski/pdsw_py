import os
import pathlib

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from src.gui.MainWindow import MainWindow

STYLESHEET_FILE: str = os.path.join(pathlib.Path(__file__).parent.resolve(), "Interface.qss")

class Interface(QApplication):
  
  def __init__(self) -> None:
    QApplication.__init__(self)
    with open(STYLESHEET_FILE, "r") as stylesheet:
      self.setStyleSheet(stylesheet.read())

    self.main_window: MainWindow = MainWindow()
    self.main_window.setWindowState(Qt.WindowState.WindowFullScreen)
    self.main_window.show()

  def run(self) -> int:
    # self.main_window.dataRequest.emit()
    return self.exec()