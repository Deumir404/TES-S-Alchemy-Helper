import sys
from search import search_by_ingredient, Search_by_property
from search_description_potion import get_description, get_amount
from secondary_function import get_property, count_above_one, add_property, load_file, save_file
from PySide6.QtWidgets import (QLineEdit, QPushButton, QComboBox, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QWidget,  QLabel, QStackedWidget, QListWidget, QHBoxLayout, QTableWidgetItem , QMainWindow, QGridLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QCloseEvent, QPixmap, QPalette, QAction


    

class Form_perk(QWidget):
    def __init__(self, parent=None):
        super(Form_perk, self).__init__(parent)
        # Create widgets
        self.label_alchemy = QLabel("Уровень алхимии")
        self.edit_alchemy = QLineEdit("15")
        self.label_alchemist = QLabel("Алхимик")
        self.edit_alchemist = QComboBox()
        list_alchemist = ["0","1","2","3","4","5"]
        self.edit_alchemist.addItems(list_alchemist)
        self.label_healer = QLabel("Целитель")
        List_bool = ["0","1"]
        self.edit_healer = QComboBox()
        self.edit_healer.addItems(List_bool)
        self.label_pharmacist = QLabel("Провизор(Фармацевт)")
        self.edit_pharmacist = QComboBox()
        self.edit_pharmacist.addItems(List_bool)
        self.label_poisoner = QLabel("Отравитель")
        self.edit_poisoner = QComboBox()
        self.edit_poisoner.addItems(List_bool)
        self.label_purity = QLabel("Чистота")
        self.edit_purity = QComboBox()
        self.edit_purity.addItems(List_bool)
        # Create layout and add widgets
        layout_alchemy =QHBoxLayout()
        layout_alchemy.addWidget(self.label_alchemy)
        layout_alchemy.addWidget(self.edit_alchemy)
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
        layout.addLayout(layout_alchemy)
        layout.addLayout(layout_alchemist)
        layout.addLayout(layout_healer)
        layout.addLayout(layout_pharmacist)
        layout.addLayout(layout_poisoner)
        layout.addLayout(layout_purity)
        # Set dialog layout
        self.setLayout(layout)
        #Привязываем редактирование навыков к функции
        self.edit_alchemy.editingFinished.connect(self.change_perk)
        self.edit_alchemist.currentIndexChanged.connect(self.change_perk)
        self.edit_healer.currentIndexChanged.connect(self.change_perk)
        self.edit_pharmacist.currentIndexChanged.connect(self.change_perk)
        self.edit_poisoner.currentIndexChanged.connect(self.change_perk)
        self.edit_purity.currentIndexChanged.connect(self.change_perk)
    def change_perk(self):
        try :
            if int(self.edit_alchemy.text()) >= 0:
                List_perk[0] = int(self.edit_alchemy.text())
            else:
                raise ValueError
            List_perk[1] = self.edit_alchemist.currentIndex()
            List_perk[2] = self.edit_healer.currentIndex()
            List_perk[3] = self.edit_pharmacist.currentIndex()
            List_perk[4] = self.edit_poisoner.currentIndex()
            List_perk[5] = self.edit_purity.currentIndex()
            Table_p.fill_table(List_prop_dict)
        except ValueError:
            print("Введите числовое значения")
            self.edit_alchemy.setText("15")
class Form_property(QWidget):
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
class Form_ingredient(QWidget):
    def __init__(self, parent=None):
        super(Form_ingredient, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit()
        self.button = QPushButton("Поиск свойств")
        self.result_str = QLabel("Результаты")
        self.List_result = QListWidget()
        self.result()
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
            self.List_result.addItems(list_result)
class Table_potion(QWidget):
    def __init__(self, parent=None):
        super(Table_potion, self).__init__(parent)
        # Create widgets
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.verticalHeader().hide()
        self.table.setHorizontalHeaderLabels(["Название","Ингредиенты", "Свойства", "Количество", "Стоимость"])
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        # Set dialog layout
        self.setLayout(layout)
    def fill_table(self, list):
        self.table.clear()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Название","Ингредиенты", "Свойства", "Количество", "Стоимость"])
        self.table.setRowCount(count_above_one(list))
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
                description = get_description(list[i]["name"],List_perk[0],List_perk[1],List_perk[2],List_perk[3],List_perk[4])
                item_prop = QTableWidgetItem(string_property)
                item_sum = QTableWidgetItem(str(get_amount(List_inv, list[i]["name"])))
                item_disctiption = QTableWidgetItem(description[0])
                item_cost = QTableWidgetItem(str(description[1]))
                list_items  = [item, item_prop, item_disctiption, item_sum, item_cost]
                for i in range(len(list_items)):
                    list_items[i].setFlags( Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                    self.table.setItem(correct_row,i, list_items[i])
                correct_row += 1
        self.table.resizeColumnToContents(1)
        self.table.resizeColumnToContents(2)
        self.table.resizeRowsToContents()  
class Table_inv(QWidget):
    def __init__(self, list_ing, parent=None):
        super(Table_inv, self).__init__(parent)
        # Create widgets
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Название", "Свойства", "Количество"])
        self.table.setRowCount(len(list_ing))
        self.table.verticalHeader().hide()
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
            self.table.setHorizontalHeaderLabels(["Название", "Свойства", "Количество"])
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
                item_sum = QTableWidgetItem(str(list[i][1]))
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
            if int(self.table.item(item_row, 2).text()) >= 0:
                amount = int(self.table.item(item_row, 2).text())
            else:
                raise ValueError
            List_inv[item_row][1] = amount
            Table_p.fill_table(List_prop_dict)
        except AttributeError:
            pass
        except ValueError:
            print("Введи нормальные значения")
            self.table.item(item_row, 2).setText("1")
class math_page(QWidget):
    def __init__(self, list_form, parent=None):
        super(math_page, self).__init__(parent)
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
        True_layout.setColumnStretch(1, 1)
        True_layout.setColumnStretch(2, 2)
        True_layout.addLayout(layout_vertical_inv, 1, 1)
        True_layout.addLayout(layout_vertical_potion, 1, 2) 
        self.setLayout(True_layout)

class mixing_game(QWidget):
    def __init__(self, parent=None):
        super(mixing_game, self).__init__(parent)
        self.goal = get_property()
        self.attemp = 5
        self.label_goal = QLabel(f"Нужно смешать: \n Зелье {self.goal.lower()}")
        self.label_attemp = QLabel(f"Осталось попыток: {self.attemp}")
        self.image = QLabel()
        self.image.setPixmap(QPixmap("res/table.jpg").scaled(QSize(400,400)))
        self.button_mix = QPushButton("Смешать")
        self.button_clear = QPushButton("Очистить выбор")
        self.button_reset = QPushButton("Перезапуск")
        self.choice_ingredient = QHBoxLayout()
        self.choice_ingredient.setSpacing(0)
        self.first_ingredient = QLabel()
        self.first_ingredient.setTextFormat(Qt.TextFormat.RichText)
        self.first_ingredient.setText(f"<img src=\"res/image/{Mix_ingedients[0]}.png\" width = \"120\" height = \"120\"> <br>{Mix_ingedients[0]}</br>")
        self.second_ingredient = QLabel()
        self.second_ingredient.setTextFormat(Qt.TextFormat.RichText)
        self.second_ingredient.setText(f"<img src=\"res/image/{Mix_ingedients[1]}.png\" width = \"120\" height = \"120\"> <br>{Mix_ingedients[1]}</br>")
        self.choice_ingredient.addWidget(self.first_ingredient)
        Plus = QLabel("+")
        Plus.setStyleSheet("font-size: 64px")
        Plus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.choice_ingredient.addWidget(Plus)
        self.choice_ingredient.addWidget(self.second_ingredient)
        self.choice_ingredient.setSpacing(0)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_goal)
        self.layout.addWidget(self.label_attemp)
        self.layout.addWidget(self.image)
        self.layout.addLayout(self.choice_ingredient)
        self.layout.addWidget(self.button_mix)
        self.layout.addWidget(self.button_clear)
        self.layout.addWidget(self.button_reset)
        self.setLayout(self.layout)
        self.button_reset.clicked.connect(self.reset_game)
        self.button_mix.clicked.connect(self.mix_ingredients)
        self.button_clear.clicked.connect(self.clear_list)
    def reset_game(self):
        self.goal = get_property()
        self.label_goal.setText(f"Нужно смешать: \n Зелье {self.goal.lower()}")
        self.attemp = 5
        self.label_attemp.setText(f"Осталось попыток: {self.attemp}")
        self.clear_list()
    def mix_ingredients(self):
        Message = QLabel()
        if "black" in Mix_ingedients or "black" in Mix_ingedients or (Mix_ingedients[0] == Mix_ingedients[1]):
            Message_Text = "Пожалуйста, выберете 2  разных ингредиента"
            Message_title = "Ошибка"
            self.result = 0
        else :
            
            list_property_dict_game = []
            item_property = search_by_ingredient(Mix_ingedients[0])
            add_property(item_property, list_property_dict_game)
            item_property = search_by_ingredient(Mix_ingedients[1])
            add_property(item_property, list_property_dict_game)
            Checker = count_above_one(list_property_dict_game)
            if Checker == 0:
                Message_Text = "У вас ничего не получилось"
                Message_title = "Ошибка"
                self.result = 1
            elif Checker == 1:
                for i in range(len(list_property_dict_game)):
                    if list_property_dict_game[i]["sum"] > 1:
                        prop = list_property_dict_game[i]["name"]
                        break
                Message_Text = f"У вас получилось зелье {prop.lower()}"
                if self.goal == prop:
                    Message_Text = Message_Text + "\n Вы сварили правильное зелье!!!"
                    Message_title = "Победа"
                    self.result = 2
                else:
                    Message_Text = Message_Text + "\n Но это неправильное зелье"
                    Message_title = "Ошибка"
                    self.result = 1
            else:
                prop = []
                for i in range(len(list_property_dict_game)):
                    if list_property_dict_game[i]["sum"] > 1:
                        prop.append(list_property_dict_game[i]["name"])
                Message_Text = "У вас получилось смешанное зелье со следующими эффектами: \n"
                for i in range(len(prop)):
                    Message_Text = Message_Text + f"{prop[i]} \n"
                if self.goal in prop:
                    Message_Text = Message_Text + "\n Вы сварили правильное зелье!!!"
                    Message_title = "Победа"
                    self.result = 2
                else:
                    Message_Text = Message_Text + "\n Но это неправильное зелье"
                    Message_title = "Ошибка"
                    self.result = 1
        Message.setText(Message_Text)
        Button_OK = QPushButton("OK")
        Finish = QDialog()
        Finish.setWindowTitle(Message_title)
        layout_message = QVBoxLayout()
        layout_message.addWidget(Message)
        layout_message.addWidget(Button_OK)
        Finish.setLayout(layout_message)
        Button_OK.clicked.connect(Finish.accept)
        Finish.finished.connect(self.finish_result)
        Finish.exec()
    def finish_result(self):
        if self.result == 0 :
            pass
        elif self.result == 1:
            self.attemp = self.attemp - 1
            self.label_attemp.setText(f"Осталось попыток: {self.attemp}")
            if self.attemp == 0:
                Message = QLabel("Вы проиграли!\n Попробуйте ещё раз")
                Button_OK = QPushButton("OK")
                Finish = QDialog()
                Finish.setWindowTitle("Игра окончена")
                layout_message = QVBoxLayout()
                layout_message.addWidget(Message)
                layout_message.addWidget(Button_OK)
                Finish.setLayout(layout_message)
                Button_OK.clicked.connect(Finish.accept)
                Finish.finished.connect(self.finish_result)
                Finish.exec()
                self.reset_game()
        elif self.result == 2:
            self.reset_game()
    def clear_list(self):
        Mix_ingedients[0] = "black"
        Mix_ingedients[1] = "black"
        self.reset_image()
    def reset_image(self):
        self.first_ingredient.setTextFormat(Qt.TextFormat.RichText)
        self.first_ingredient.setText(f"<img src=\"res/image/{Mix_ingedients[0]}.png\" width = \"120\" height = \"120\"> <br>{Mix_ingedients[0]}</br>")
        self.second_ingredient.setTextFormat(Qt.TextFormat.RichText)
        self.second_ingredient.setText(f"<img src=\"res/image/{Mix_ingedients[1]}.png\" width = \"120\" height = \"120\"> <br>{Mix_ingedients[1]}</br>")
class Table_game(QWidget):
    def __init__(self, num, parent=None):
        super(Table_game, self).__init__(parent)
        # Create widgets
        self.number = num
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        # Create layout and add widgets
        layout = QHBoxLayout()
        layout.addWidget(self.table)
        # Set dialog layout
        self.setLayout(layout)
        self.fill_table()
        self.table.cellDoubleClicked.connect(self.add_ingredients)
    def fill_table(self):
        correct = 0
        list_ingredients = search_by_ingredient("")
        self.table.setRowCount(len(list_ingredients)//3+1)
        for i in range(len(list_ingredients)//3+1):
                for j in range(3):
                    if correct == len(list_ingredients):
                        break
                    ingredient = QLabel()
                    ingredient.setTextFormat(Qt.TextFormat.RichText)
                    ingredient.setText(f"<img src=\"res/image/{list_ingredients[correct]}.png\" width = \"120\" height = \"120\"> <br>{list_ingredients[correct]}</br>")
                    correct = correct + 1
                    self.table.setCellWidget(i,j,ingredient)
                    self.table.verticalHeader().hide()
                    self.table.horizontalHeader().hide()
                    self.table.resizeColumnsToContents()
                    self.table.resizeRowsToContents()
    def add_ingredients(self):
        item = self.table.currentIndex()
        ingredient = self.table.cellWidget(item.row(), item.column()).text().split("<br>")[1]
        ingredient = ingredient.split("</br>")[0]
        Mix_ingedients[self.number] = ingredient
        Mix.reset_image()
class game_page(QWidget):
    def __init__(self, list_form, parent=None):
        super(game_page, self).__init__(parent)
        # Create widgets
        True_layout = QHBoxLayout()
        True_layout.addWidget(list_form[0])
        True_layout.addWidget(list_form[1])
        True_layout.addWidget(list_form[2])
        self.setLayout(True_layout)

class changer_page(QStackedWidget):
    def __init__(self, list, parent=None):
        super(changer_page, self).__init__(parent)
        for i in range(len(list)):
            self.addWidget(list[i])
        self.setCurrentIndex(0)
    def change(self):
        if self.currentIndex()== 0:
            self.setCurrentIndex(1)
        else:
            self.setCurrentIndex(0)
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("TES:S alchemy helper") 
        bkgnd = QPixmap("res/main_window.jpg")
        bkgnd.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        icon = QPixmap("res/main_icon.png")
        icon.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, bkgnd)
        self.setPalette(palette)
        help_act = QAction("Справка", self) 
        help_act.triggered.connect(self.open_help)
        change_act = QAction("Сменить окно", self) 
        change_act.triggered.connect(changer.change)
        load_act = QAction("Загрузить из файла", self) 
        load_act.triggered.connect(lambda:  load_file(List_inv, Table_in))
        self.showMaximized()
        self.setWindowIcon(icon)
        self.menu = self.menuBar()
        self.menu.addAction(help_act)
        self.menu.addAction(load_act)
        self.menu.addAction(change_act)
        # showing all the widgets
        self.setCentralWidget(changer)
        self.show()
    def open_help(self):
        Help_dialog = QDialog()
        self.correct_help = 0
        Help_layout = QVBoxLayout()
        Text_help = QLabel()
        Text_help.setText("Test")
        Help_layout.addWidget(Text_help)
        Button_layout = QHBoxLayout()
        Ok_button = QPushButton("Выход")
        next_button = QPushButton("След. стр.")
        perv_button = QPushButton("Пред. стр.")
        Button_layout.addWidget(perv_button)
        Button_layout.addWidget(Ok_button)
        Button_layout.addWidget(next_button)
        Ok_button.clicked.connect(Help_dialog.accept)
        next_button.clicked.connect(lambda: self.swap_help(Text_help,   1))
        next_button.clicked.connect(lambda: self.swap_help(Text_help,  -1))
        Help_layout.addLayout(Button_layout)
        Help_dialog.setLayout(Help_layout)
        Help_dialog.exec()


    def swap_help(self, label, inc):
        self.correct_help += inc
        Text = ["Adawodmawiofioawnfioawnfioanwfioanwionaiofnoifniowanfioawnfoianwf", "nwaoifnioawnfioawfoiajwfioajfwoiafj", "lfanwofinaiownfioan"]
        if self.correct_help < 0:
            self.correct_help = 0
        if self.correct_help > len(Text):
            self.correct_help = len(Text)
        label.setText(str(self.correct_help))
        

    def closeEvent(self, event: QCloseEvent) -> None:
        save_file(List_inv)


if __name__ == '__main__':
    # Создания приложения
    app = QApplication(sys.argv)
    # Создание листов для инвентаря и таблицы расчёта зелий 
    global List_inv
    List_inv = []
    List_prop_dict = []
    List_prop = []
    List_perk = [15,0,0,0,0,0]
    # Создание форм для поиска ингредиента
    search_ingredient = Form_ingredient()
    Search_property = Form_property()
    # создание таблицы, в которой указаны возможные зелья 
    Table_p = Table_potion()
    # создание формы, для считывания характеристик для расчёта
    Form_skill = Form_perk()
    # создание таблицы инвентаря
    Table_in = Table_inv(List_inv)
    # листа со всеми виджетами
    list_widget = [search_ingredient, Search_property, Table_in, Table_p, Form_skill]
    # Создание объекта отвечающего за расположение виджетов в калькуляторе
    Layout = math_page(list_widget)
    # Лист для смешивания в игре
    Mix_ingedients = ["black","black"]
    #создание таблиц для выбора ингредиента
    Table_ingredients = Table_game(0)
    Table_ingredients_2 = Table_game(1)
    #Создание  интерфейса для взаимодействия с игрой
    Mix = mixing_game()
    List_game_widget = [Table_ingredients ,  Mix, Table_ingredients_2]
    #Создание объекта отвечающего за расположение виджетов на окне игры
    Layout_game_page = game_page(List_game_widget)
    List_page = [Layout, Layout_game_page]
    # создания объекта для смены окон(калькулятора и игры)
    changer = changer_page(List_page)
    # Создание окна
    main_menu = Window()
    sys.exit(app.exec())