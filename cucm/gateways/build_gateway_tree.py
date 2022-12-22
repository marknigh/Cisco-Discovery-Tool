from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMainWindow
from .gateway_window import Ui_GatewayTree

class BuildGatewayWindow(QWidget, Ui_GatewayTree):
    def __init__(self, data):
        super(BuildGatewayWindow, self).__init__()
        self._data = data
        
        #Set up User interface from designer
        self.window = QMainWindow()
        self.gatewayWin = Ui_GatewayTree()
        self.gatewayWin.setupUi(self.window)
        # self.gatewayWin.tree_gateway.itemDoubleClicked.connect(self.get_endpoints)
        self.window.show()

        #Call method to load table (data is passed in from phone_details.py, SOAP API call)
        self.build_tree()
        
    def build_tree(self):
        tree = self.gatewayWin.tree_gateway
        tree.setColumnCount(6)
        items = []
        for index in range(len(self._data)):
            item =  QTreeWidgetItem(tree)
            item.setText(0, self._data[index]['name'])
            item.setText(1, self._data[index]['description'])
            item.setText(2, self._data[index]['model'])
            item.addChild(item)
            
            for v in self._data[index]['units']:
                hg_child =  QTreeWidgetItem(tree)
                hg_child.setText(3, v['product'])
                item.addChild(hg_child)
                
                for lg in v['subunits']:
                    lg_child = QTreeWidgetItem(tree)
                    lg_child.setText(4, lg['product'])
                    item.addChild(lg_child)
                    
                for ep in v['endpoints']:
                    ep_child = QTreeWidgetItem(tree)
                    ep_child.setText(5, ep['pattern'])
                    item.addChild(ep_child)
            items.append(item)
        tree.insertTopLevelItems(0, items)
