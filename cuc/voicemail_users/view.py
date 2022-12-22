from PyQt5.QtWidgets import QMainWindow
from .vm_users_windows import Ui_VoiceMailUsers

class VoicemailUserView:
    def __init__(self, model):
        super().__init__()
        self._model = model
        #Set up User interface from designer
        self.window = QMainWindow()
        self.vmwin = Ui_VoiceMailUsers()
        self.vmwin.setupUi(self.window)
        self.window.show()
        self.vmwin.tableView.setModel(self._model)
        # self.vmwin.tableView.doubleClicked.connect(self.user_detail) 
        
    # def user_detail(self):
    #     print('double-click')
    #     print(self._model)
    #     indexes = self.vmwin.tableView.selectedIndexes()
    #     row = self.vmwin.vmUserTable.currentIndex().row()
    #     column = self.vmwin.vmUserTable.currentIndex().column()
    #     item = self.vmwin.vmUserTable.item(row, column)
    #     print(item.text())
    #     for sub in self.vmUserList:
    #         if sub['DisplayName'] == item.text():
    #             print (sub)
