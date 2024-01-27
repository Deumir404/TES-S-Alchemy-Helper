import sys
from search_property import Search_by_property
from search_ingredient import search_by_ingredient
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QLabel, QListWidget, QHBoxLayout, QTableWidgetItem )
from PySide6.QtCore import Qt


class Form_property(QDialog):
    def __init__(self, parent=None):
        super(Form_property, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit()
        self.button = QPushButton("Поиск по свойству")
        self.result_str = QLabel("Результаты")
        self.List_result = QListWidget()
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.result_str)
        layout.addWidget(self.List_result)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.result)
        self.List_result.itemDoubleClicked.connect(self.add_ingredients)
    def result(self):
        self.List_result.clear()
        list_result = Search_by_property(self.edit.text())
        if type(list_result) is str:
            self.List_result.addItem(list_result)
        else :
            self.List_result.addItems(list_result)
    def add_ingredients(self):
        item = self.List_result.currentItem()
        if item.text() not in List_inv:
            List_inv.append(item.text())
            Table_in.update_table(List_inv)
class Form_ingredient(QDialog):
    def __init__(self, parent=None):
        super(Form_ingredient, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit()
        self.button = QPushButton("Поиск свойств")
        self.result_str = QLabel("Результаты")
        self.List_result = QListWidget()
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.result_str)
        layout.addWidget(self.List_result)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.result)
        self.List_result.itemDoubleClicked.connect(self.add_ingredients)
    def add_ingredients(self):
        item = self.List_result.currentItem()
        if item.text() not in List_inv:
            List_inv.append(item.text())
            Table_in.update_table(List_inv)
    def result(self):
        self.List_result.clear()
        list_result = search_by_ingredient(self.edit.text())
        if type(list_result) is str:
            self.List_result.addItem(list_result)
        else :
            self.List_result.addItem(list_result[0])
class main_page(QDialog):
    def __init__(self, list_form, parent=None):
        super(main_page, self).__init__(parent)
        # Create widgets
        layout = QHBoxLayout()
        for i in range(3):
            layout.addWidget(list_form[i])
        # Set dialog layout
        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(layout)
        layout_vertical.addWidget(list_form[3])
        self.setLayout(layout_vertical)
class Table_potion(QDialog):
    def __init__(self, parent=None):
        super(Table_potion, self).__init__(parent)
        # Create widgets
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setRowCount(10)
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        # Set dialog layout
        self.setLayout(layout)
    def fill_table(self, list):
        self.table.clear()
        self.table.setColumnCount(5)
        self.table.setRowCount(len(list))

        for i in range(len(list)):
            item = QTableWidgetItem("Зелье " + list[i]["name"])
            item_list = Search_by_property(list[i]["name"])
            string_property = str()
            for j in range(len(item_list)):
                string_property = string_property + item_list[j]
                if j != len(item_list)-1:      
                    string_property += "\n"
            item_prop = QTableWidgetItem(string_property)
            item_sum = QTableWidgetItem(str(list[i]["sum"]-1))
            item.setFlags(Qt.ItemFlag.ItemIsEditable)
            item_prop.setFlags(Qt.ItemFlag.ItemIsEditable)
            item_sum.setFlags(Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(i,0, item)
            self.table.setItem(i,1, item_prop)
            self.table.setItem(i,2, item_sum)

        self.table.resizeColumnToContents(1)
        self.table.resizeRowsToContents()  
class Table_inv(QDialog):
    def __init__(self, list_ing, parent=None):
        super(Table_inv, self).__init__(parent)
        # Create widgets
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(len(list_ing))
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        # Set dialog layout
        self.setLayout(layout)
        self.table.itemDoubleClicked.connect(self.remove_item)  
    def update_table (self, list):
            self.table.clear()
            self.table.setColumnCount(3)
            self.table.setRowCount(len(list))
            List_prop.clear()
            List_prop_dict.clear()
            for i in range(len(list)):
                item = QTableWidgetItem(list[i])
                item_property = search_by_ingredient(list[i])
                string_property = str()
                for j in range(4):
                    string_property = string_property + item_property[1][j]
                    dict_item = dict(name = item_property[1][j], sum = 1)
                    if item_property[1][j] not in List_prop:
                        List_prop.append(item_property[1][j])
                        List_prop_dict.append(dict_item)
                    else:
                        for k in range(len(List_prop_dict)):
                            if List_prop_dict[k]["name"] == dict_item["name"]:
                                List_prop_dict[k]["sum"] =  List_prop_dict[k]["sum"] + 1
                                break
                    if j != 3:      
                        string_property += "\n"
                item_prop = QTableWidgetItem(string_property)
                item.setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                item_prop.setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.table.setItem(i,0, item)
                self.table.setItem(i,1, item_prop)
            self.table.resizeColumnToContents(1)
            self.table.resizeRowsToContents()
            
            Table_p.fill_table(List_prop_dict)  
    def remove_item (self):
        item = self.table.currentItem()
        if self.table.item(item.row(), 0).text() in List_inv :
            List_inv.remove(self.table.item(item.row(), 0).text()) 
        self.update_table(List_inv)
        




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication([])
    #inventory list
    List_inv = []
    List_prop_dict = []
    List_prop = []
    # Create and show the form
    search_ingredient = Form_ingredient()
    Search_property = Form_property()
    Table_p = Table_potion()
    Table_in = Table_inv(List_inv)
    list_widget = [search_ingredient, Search_property, Table_in, Table_p]
    Layout = main_page(list_widget)
    Layout.show()
    # Run the main Qt loop
    sys.exit(app.exec())