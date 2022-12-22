
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtGui

class MeetMeModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['pattern', 'securityLevel', 'description']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 3

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['PATTERN', 'SECURITYLEVEL', 'DESCRIPTION'][section]
            if orientation == Qt.Vertical:
                return str(section + 1)
        
        if role == Qt.ForegroundRole:
            return QtGui.QColor('blue')
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            column = index.column()
            return self.data[index.row()][self.headers[column]]