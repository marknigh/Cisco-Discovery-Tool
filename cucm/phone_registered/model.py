from PyQt5.QtCore import QAbstractTableModel, Qt

class PhoneRegistrationModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['Name', 'Status', 'DirNumber', 'IPAddress']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 4

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ['NAME', 'STATUS', 'Dir Number', 'IP ADDRESS'][section]
            if orientation == Qt.Vertical:
                return str(section + 1)

    def data(self,index,role):
        if role == Qt.DisplayRole:
            column = index.column()
            return self.data[index.row()][self.headers[column]]