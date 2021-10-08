import random

from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
class Password_generator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('password_generator.ui',None)
        self.ui.show()
        numbers_list=['8','9','10','11','12','13','14','15','16','17','18','19','20']
        self.ui.long_password.addItems(numbers_list)
        self.ui.btn_generate.clicked.connect(self.generat_password)
        self.ui.checkBox_upercase.setChecked(True)
    def generat_password(self):
        long_pass=int(self.ui.long_password.currentText())
        password=[None for i in range(long_pass)]
        if self.ui.checkBox_numbers.isChecked():
            for i in range(random.randint(1,3)):
                nummber=random.randint(48,57)
                password[i]=chr(nummber)
        if self.ui.checkBox_upercase.isChecked():
            for i in range(password.index(None),password.index(None)+random.randint(1,3)):
                Letter=random.randint(65,90)
                password[i]=chr(Letter)
        for i in range(password.index(None),password.index(None)+random.randint(1,3)):
            letter=random.randint(33,47)
            password[i]=chr(letter)
        for i in range(password.index(None),len(password)):
            letter=random.randint(97,122)
            password[i]=chr(letter)
        string_pass=''
        self.ui.password_text.setText(string_pass.join(random.sample(password,long_pass)))

app=QApplication([])
window=Password_generator()
app.exec()