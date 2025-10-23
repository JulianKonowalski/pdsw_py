import logging

from PySide6.QtGui import QFont
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

LOGGER: logging.Logger = logging.getLogger(__name__)

class DataPanel(QWidget):

  dataUpdated: Signal = Signal(any)

  def __init__(self, title: str, initial_data: int, parent: QWidget = None):
    LOGGER.log("Creating DataPanel instance")

    QWidget.__init__(self, parent)

    self.header: QLabel = QLabel(title)
    self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.header.setObjectName("data-panel-header")

    self.content: QLabel = QLabel(str(initial_data))
    self.content.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.content.setObjectName("data-panel-content")

    main_layout: QVBoxLayout = QVBoxLayout(self)
    main_layout.setSpacing(0)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.addWidget(self.header)
    main_layout.addWidget(self.content)

    self.setLayout(main_layout)
    self.setObjectName("data-panel")

  @Slot(int)
  def updateData(self, new_value: int):
    LOGGER.log("DataPanel executing updateData")
    self.content.setText(str(new_value))
    self.dataUpdated.emit()

  @Slot(int)
  def onDataUpdated(self, new_value: int):
    LOGGER.log("DataPanel executing onDataUpdated")
    # do something, maybe change style
    pass

  def resizeEvent(self, event):
    LOGGER.log("DataPanel executing resizeEvent")
    font: QFont = self.header.font()

    font.setPointSize(self.height() / 8)
    self.header.setFont(font)
    
    font.setPointSize(self.height() / 4)
    self.content.setFont(font)