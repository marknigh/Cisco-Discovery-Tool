# Universal Error Dialog to catch all try/except errors

from PyQt5.QtWidgets import QMessageBox
from error import Ui_ErrorMessage

class ErrorDialog():
   def __init__(self, data):
      super().__init__()

      self.mbox = QMessageBox()
      self.mbox.setIcon(QMessageBox.Critical)

      self.mbox.setText("There has been an error")
      self.mbox.setWindowTitle("Error")
      self.mbox.setDetailedText(str(data.args[0]))
      self.mbox.setStandardButtons(QMessageBox.Ok)
      self.mbox.exec()