from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtGui


class SipTrunkModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['name', 'model', 'destinations', 'description']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 4

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['NAME', 'MODEL', 'DESTINATIONS', 'DESCRIPTION'][section]
            if orientation == Qt.Vertical:
                return str(section + 1)
        
        if role == Qt.ForegroundRole:
            return QtGui.QColor('blue')
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            column = index.column()
            if column == 2:
                return ','.join(self.data[index.row()][self.headers[column]])
            else:
                return self.data[index.row()][self.headers[column]]