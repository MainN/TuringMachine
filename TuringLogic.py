import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtGui
import Turing
class ExampleApp(QtWidgets.QMainWindow, Turing.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайн
        self.pushButton.clicked.connect(self.step)
        self.pushButton_5.clicked.connect(self.load_list)
        self.pushButton_6.clicked.connect(self.load_tablet)
        self.current_state=None
        self.current_symbol=None 
        self.dict={}
    def step(self):
        transition=(self.getFunction(self.current_symbol,self.current_state))
    def load_list(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Choose start string")[0]
        f = open(directory)
        row=0
        for string in f:
            counter=0
            for x in string:
                #print(str(window.tableWidget_2.columnCount()))
                window.tableWidget_2.setColumnCount(window.tableWidget_2.columnCount()+1)
                window.tableWidget_2.setItem(row,counter,QtWidgets.QTableWidgetItem(x))
                counter=counter+1
            row = 1    
        self.current_state= window.tableWidget_2.item(1,0).text()
        self.current_symbol= window.tableWidget_2.item(0,0).text()
    def load_tablet(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Choose tablet")[0]
        f = open(directory)
        counter=0
        for string in f:
            window.tableWidget.setRowCount(window.tableWidget.rowCount()+1)
            window.tableWidget.setItem(counter,0,QtWidgets.QTableWidgetItem(string[2]))
            window.tableWidget.setItem(counter,1,QtWidgets.QTableWidgetItem(string[0]))
            window.tableWidget.setItem(counter,2,QtWidgets.QTableWidgetItem(string[4]))
            window.tableWidget.setItem(counter,3,QtWidgets.QTableWidgetItem(string[6]))
            window.tableWidget.setItem(counter,4,QtWidgets.QTableWidgetItem(string[8]))
            self.dict[(string[2],string[0])]=(string[4],string[6],string[8])
            counter=counter+1
    def getFunction(self,symbol,state):
        return self.dict[(symbol,state)]
def main():
    global window
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()