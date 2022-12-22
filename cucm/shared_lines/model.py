from utilities.error_dialog import ErrorDialog
from PyQt5.QtCore import QObject, QAbstractTableModel, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtGui
from cucm.phone_configured.list_phone_view import Ui_MainWindow

class SharedLineModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['pattern']
    
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 1

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['PATTERN'][section]
            if orientation == Qt.Vertical:
                return str(section + 1)
        
        if role == Qt.ForegroundRole:
            return QtGui.QColor('blue')
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()]