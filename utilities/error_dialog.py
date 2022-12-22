# Universal Error Dialog to catch all try/except errors

from PyQt5.QtWidgets import QMessageBox

class ErrorDialog():
   def __init__(self, data):
      super().__init__()

      self.mbox = QMessageBox()
      self.mbox.setIcon(QMessageBox.Critical)

      self.mbox.setText("An Error Has Occurred")
      self.mbox.setWindowTitle("Error")
      self.mbox.setDetailedText(str(data.args[0]))
      self.mbox.setStandardButtons(QMessageBox.Ok)
      self.mbox.exec()