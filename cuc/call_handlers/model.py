from PyQt5.QtCore import QAbstractTableModel, Qt

class CallHandlerModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['Display', 'URI']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 2

    def data(self,index,role):
        if role == Qt.DisplayRole:
            column = index.column()
            return self.data[index.row()][self.headers[column]]        
