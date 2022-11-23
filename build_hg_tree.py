from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem
from hunt_group_window import Ui_HuntGroup


class BuildHuntGroup():
    def __init__(self, data):
        super(BuildHuntGroup, self).__init__
        
        self._data = data
        
        #Set up User interface from designer
        self.window = QMainWindow()
        self.HGWin = Ui_HuntGroup()
        self.HGWin.setupUi(self.window)
        self.window.show()

        #Call method to load table (data is passed in from xxxxxx.py, SOAP API call)
        BuildTree(self)
        
def BuildTree(self):

    tree = self.HGWin.tree_hunt_group
    tree.setColumnCount(4)
    tree.setHeaderLabels(["Pilot", "HuntList", "Line Group", "Patterns"])
    items = []
    for index in range(len(self._data)):
        item =  QTreeWidgetItem(tree)
        item.setText(0, self._data[index]['pilot'])
        item.setText(1, self._data[index]['hunt_list'])
        item.addChild(item)
        
        for v in self._data[index]['hunt_list_members']:
            hg_child =  QTreeWidgetItem(tree)
            hg_child.setText(2, v['name'])
            item.addChild(hg_child)
            
            for lg in v['line_members']:
                lg_child = QTreeWidgetItem(tree)
                lg_child.setText(3, lg['pattern'])
                item.addChild(lg_child)
        items.append(item)
    tree.insertTopLevelItems(0, items)
