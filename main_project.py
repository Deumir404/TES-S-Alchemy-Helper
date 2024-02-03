import sys
from search_property import Search_by_property
from search_ingredient import search_by_ingredient
from search_description_potion import Search_by_name_potion, Search_by_name_poison
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QLabel, QListWidget, QHBoxLayout, QTableWidgetItem , QMainWindow, QGridLayout)
from PySide6.QtCore import Qt 

def count_above_two(dict):
    count = 0
    for i in range(len(dict)):
        if dict[i]["sum"] > 1:
            count += 1
    return count

class Form_perk(QDialog):
    def __init__(self, parent=None):
        super(Form_perk, self).__init__(parent)
        # Create widgets
        self.label_alchemist = QLabel("Алхимик")
        self.edit_alchemist = QLineEdit()
        self.label_healer = QLabel("Целитель")
        self.edit_healer = QLineEdit()
        self.label_pharmacist = QLabel("Провизор(Фармацевт)")
        self.edit_pharmacist = QLineEdit()
        self.label_poisoner = QLabel("Отравитель")
        self.edit_poisoner = QLineEdit()
        self.label_purity = QLabel("Чистота")
        self.edit_purity = QLineEdit()
        # Create layout and add widgets
        layout_alchemist =QHBoxLayout()
        layout_alchemist.addWidget(self.label_alchemist)
        layout_alchemist.addWidget(self.edit_alchemist)
        layout_healer =QHBoxLayout()
        layout_healer.addWidget(self.label_healer)
        layout_healer.addWidget(self.edit_healer)
        layout_pharmacist =QHBoxLayout()
        layout_pharmacist.addWidget(self.label_pharmacist)
        layout_pharmacist.addWidget(self.edit_pharmacist)
        layout_poisoner =QHBoxLayout()
        layout_poisoner.addWidget(self.label_poisoner)
        layout_poisoner.addWidget(self.edit_poisoner)
        layout_purity =QHBoxLayout()
        layout_purity.addWidget(self.label_purity)
        layout_purity.addWidget(self.edit_purity)
        layout = QVBoxLayout()
        layout.addLayout(layout_alchemist)
        layout.addLayout(layout_healer)
        layout.addLayout(layout_pharmacist)
        layout.addLayout(layout_poisoner)
        layout.addLayout(layout_purity)
        # Set dialog layout
        self.setLayout(layout)
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
        item_with_amount = [item.text(), 1]
        if item_with_amount not in List_inv:
            List_inv.append(item_with_amount)
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
        item_with_amount = [item.text(), 1]
        if item_with_amount not in List_inv:
            List_inv.append(item_with_amount)
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
        for i in range(2):
            layout.addWidget(list_form[i])
        # Set dialog layout
        layout_vertical_potion = QVBoxLayout()
        layout_vertical_potion.addLayout(layout)
        layout_vertical_potion.addWidget(list_form[3])
        layout_vertical_inv = QVBoxLayout()
        label_inv = QLabel("Инвентарь")
        label_skill = QLabel("Навыки")
        layout_vertical_inv.addWidget(label_skill)
        layout_vertical_inv.addWidget(list_form[4])
        layout_vertical_inv.addWidget(label_inv)
        layout_vertical_inv.addWidget(list_form[2])
        True_layout = QGridLayout()
        True_layout.setColumnStretch(1, 0)
        True_layout.setColumnStretch(2, 1)
        True_layout.addLayout(layout_vertical_inv, 1, 1)
        True_layout.addLayout(layout_vertical_potion, 1, 2)
        self.setLayout(True_layout)
class Table_potion(QDialog):
    def __init__(self, parent=None):
        super(Table_potion, self).__init__(parent)
        # Create widgets
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        # Set dialog layout
        self.setLayout(layout)
    def fill_table(self, list):
        self.table.clear()
        self.table.setColumnCount(5)
        self.table.setRowCount(count_above_two(list))
        correct_row = 0
        for i in range(len(list)):
            if list[i]["sum"] > 1:
                item = QTableWidgetItem("Зелье " + list[i]["name"])
                item_list = Search_by_property(list[i]["name"])
                string_property = str()
                for j in range(len(item_list)):
                    string_property = string_property + item_list[j]
                    if j != len(item_list)-1:      
                        string_property += "\n"
                discription = str(Search_by_name_potion(list[i]["name"]))
                if discription == "Описание не найдено":
                    discription = str(Search_by_name_poison(list[i]["name"]))
                item_prop = QTableWidgetItem(string_property)
                item_sum = QTableWidgetItem(str(list[i]["sum"]-1))
                item_disctiption = QTableWidgetItem(discription)
                item.setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                item_prop.setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                item_disctiption.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                item_sum.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.table.setItem(correct_row,0, item)
                self.table.setItem(correct_row,1, item_prop)
                self.table.setItem(correct_row,2, item_disctiption)
                self.table.setItem(correct_row,3, item_sum)
                correct_row += 1

        self.table.resizeColumnToContents(1)
        self.table.resizeColumnToContents(2)
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
        self.table.itemChanged.connect(self.change)  
    def update_table (self, list):
            self.table.clear()
            self.table.setColumnCount(3)
            self.table.setRowCount(len(list))
            List_prop.clear()
            List_prop_dict.clear()
            for i in range(len(list)):
                item = QTableWidgetItem(list[i][0])
                item_property = search_by_ingredient(list[i][0])
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
                item_sum = QTableWidgetItem("1")
                item.setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                item_prop.setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.table.setItem(i,0, item)
                self.table.setItem(i,1, item_prop)
                self.table.setItem(i,2, item_sum)
            self.table.resizeColumnToContents(1)
            self.table.resizeRowsToContents()
            Table_p.fill_table(List_prop_dict)  
    def remove_item (self):
        item = self.table.currentItem()
        if item.column() != 2:
            item_with_amount = [self.table.item(item.row(), 0).text(), List_inv[item.row()][1]]
            if item_with_amount in List_inv:
                List_inv.remove(item_with_amount)
            self.update_table(List_inv)
    def change (self):
        try:
            item_row = self.table.currentItem()
            item_row = item_row.row()
            amount = int(self.table.item(item_row, 2).text())
            List_inv[item_row][1] = amount
            print(List_inv)
        except AttributeError:
            pass
        except ValueError:
            print("Введи нормальные значения")
            self.table.editItem(item_row)
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        # setting title 
        self.setWindowTitle("TES:S alchemy helper") 
        # setting geometry 
        self.setGeometry(100, 100, 600, 400) 
        # calling method 
        self.showMaximized() 
        # showing all the widgets
        self.setCentralWidget(Layout) 
        self.show() 




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    #inventory list
    List_inv = []
    List_prop_dict = []
    List_prop = []
    # Create and show the form
    search_ingredient = Form_ingredient()
    Search_property = Form_property()
    Table_p = Table_potion()
    Form_skill = Form_perk()
    Table_in = Table_inv(List_inv)
    list_widget = [search_ingredient, Search_property, Table_in, Table_p, Form_skill]
    Layout = main_page(list_widget)
    # Run the main Qt loop
    main_menu = Window()
    sys.exit(app.exec())