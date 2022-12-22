from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from cucm.phone_configured.list_phone_view import Ui_MainWindow

class PhoneListView(QObject): 
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.phone_win = Ui_MainWindow()
        self.phone_win.setupUi(self.window)
        self.window.show()
        self._data = model.data
        self.phone_win.phone_tableView.setModel(model)
        self.phone_win.export_btn.clicked.connect(self.export_to_file)
    
    def export_to_file(self):
        folderpath = QFileDialog.getSaveFileName()
        f = open(folderpath[0], 'w')
        f.write('name' + ',' + 'description' + ',' + 'model' + ',' + 'lines' + '\n')
        for item in self._data:
            #build string to export
            export_string = item['name'] + ',' + item['description'] + ',' + item['model'] + ',' + item['lines'] + '\n'
            f.write(export_string)
