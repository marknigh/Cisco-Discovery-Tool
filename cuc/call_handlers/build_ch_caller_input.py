from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QTableWidgetItem
from callhander_ci_window import Ui_Caller_Input

class BuildCallerInput():
    def __init__(self, data):
        super(BuildCallerInput, self).__init__
        
        self._data = data
        print(data)
        
        #Set up User interface from designer
        self.window = QMainWindow()
        self.ch_ci_win = Ui_Caller_Input()
        self.ch_ci_win.setupUi(self.window)
        self.ch_ci_win.ch_ci_table.setColumnWidth(0, 150)
        self.ch_ci_win.ch_ci_table.setColumnWidth(1, 150)
        self.window.show()

        #Call method to load table
        BuildTree(self)
        
def BuildTree(self):

    tree = self.ch_ci_win.ch_ci_table
    tree.setColumnCount(2)
    tree.setRowCount(12)
    
    for (index, value) in enumerate(self._data['MenuEntry']):
        self.ch_ci_win.ch_ci_table.setItem(index, 0, QTableWidgetItem(value['TouchtoneKey']))
        self.ch_ci_win.ch_ci_table.setItem(index, 1, QTableWidgetItem(value['Action']))

