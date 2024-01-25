import sys
from search_property import Search_by_property
from search_ingredient import search_by_ingredient
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QLabel, QListWidget, QHBoxLayout, QTableWidgetItem )

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

    def result(self):
        self.List_result.clear()
        list_result = Search_by_property(self.edit.text())
        if type(list_result) is str:
            self.List_result.addItem(list_result)
        else :
            self.List_result.addItems(list_result)
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

    def result(self):
        self.List_result.clear()
        list_result = search_by_ingredient(self.edit.text())
        if type(list_result) is str:
            self.List_result.addItem(list_result)
        else :
            self.List_result.addItem(list_result[0])
            self.List_result.addItems(list_result[1])
class main_page(QDialog):
    def __init__(self, list_form, parent=None):
        super(main_page, self).__init__(parent)
        # Create widgets
        layout = QHBoxLayout()
        for i in range(len(list_form)):
            layout.addWidget(list_form[i])
        # Set dialog layout
        self.setLayout(layout)
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
        #fill table
        for i in range(len(list_ing)):
            item = QTableWidgetItem(list_ing[i])
            item_property = search_by_ingredient(list_ing[i])
            string_property = str()
            for j in range(4):
                string_property = string_property + item_property[1][j]
                if j != 3:      
                    string_property += "\n"
            item_prop = QTableWidgetItem(string_property)
            self.table.setItem(i,0, item)
            self.table.setItem(i,1, item_prop)
        self.table.resizeColumnToContents(1)
        self.table.resizeRowsToContents()     
    




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication([])
    #inventory list
    List_inv = ["Собачий корень", "Алый корень Нирна"]
    # Create and show the form
    search_ingredient = Form_ingredient()
    Search_property = Form_property()
    Table_p = Table_potion()
    Table_in = Table_inv(List_inv)
    list_widget = [search_ingredient, Search_property, Table_p , Table_in]
    Layout = main_page(list_widget)
    Layout.show()
    # Run the main Qt loop
    sys.exit(app.exec())