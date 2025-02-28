import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic
#from 계산기 import Ui_Form
#from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QFont

ui_path = r"C:\Users\USER\OneDrive\바탕 화면\python40-main\python40-main\33.calculator\pyqtUI.ui"
form_class = uic.loadUiType(ui_path)[0]
       

class WindowClass(QMainWindow, form_class) :
    def __init__(self):     # 초기화
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Calculator")

        # 폰트 전체 적용
        self.setFont(QFont("맑은 고딕", 14))

        # 스타일 시트 적용
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f8f8;
            }
            QPushButton {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QLineEdit {
                background-color: #ffffff;
                border: none;
                font-size: 20px;
                color: #333;
                padding: 10px;
                qproperty-alignment: 'AlignRight | AlignVCenter';
            }
            QPushButton {
                background-color: #ffffff;  /* 흰색 */
                color: #000000;            /* 검정색 */
            }
        """)

        # 나머지 시그널/슬롯 연결 등 동일
        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)

        self.le_view.setEnabled(False)

        self.text_value = ""

    def btn_clicked(self):
        btn_value = self.sender().text()
        if btn_value == 'C':
            print("Clear")
            self.le_view.setText("0")
            self.text_value = ""
        elif btn_value == '=':
            print("=")
            try:
                resultValue = eval(self.text_value.lstrip("0"))
                self.le_view.setText(str(resultValue))
            except:         #계산 불가 경우 에러 출력 
                self.le_view.setText("error")
        else:
            if btn_value == 'X':
                btn_value = '*'
            self.text_value = self.text_value + btn_value
            print(self.text_value)
            self.le_view.setText(self.text_value)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
