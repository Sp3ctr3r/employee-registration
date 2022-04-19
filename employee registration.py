from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3 as sql

connect = sql.connect("database.db")
cursor = connect.cursor()
cursor.execute("create table if not exists person (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username text, password text)")
connect.commit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(700, 630, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(320, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setGeometry(QtCore.QRect(320, 60, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(360, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.viewButton.setFont(font)
        self.viewButton.setObjectName("viewButton")
        self.idLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idLineEdit.setGeometry(QtCore.QRect(320, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.idLineEdit.setFont(font)
        self.idLineEdit.setObjectName("idLineEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(40, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 380, 341, 311))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(200, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(520, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.secondPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.secondPasswordLineEdit.setGeometry(QtCore.QRect(320, 160, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.secondPasswordLineEdit.setFont(font)
        self.secondPasswordLineEdit.setInputMask("")
        self.secondPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secondPasswordLineEdit.setObjectName("secondPasswordLineEdit")
        self.selectDatas = QtWidgets.QPushButton(self.centralwidget)
        self.selectDatas.setGeometry(QtCore.QRect(680, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.selectDatas.setFont(font)
        self.selectDatas.setObjectName("selectDatas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        ui.secondPasswordLineEdit.setVisible(False)

        def exit():
            quest = QMessageBox.question(MainWindow, "Quit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.Cancel)

            if quest == QMessageBox.Yes:
                sys.exit(app.exec_())

        ui.quitButton.clicked.connect(exit)

        def select():
            selected = ui.tableWidget.selectedItems()
            ui.idLineEdit.setText(selected[0].text())
            ui.usernameLineEdit.setText(selected[1].text())
            ui.passwordLineEdit.setText(selected[2].text())        
            
            ui.secondPasswordLineEdit.setVisible(True)

        ui.selectDatas.clicked.connect(select)

        def add():
            try:
                id = ui.idLineEdit.text()
                username = ui.usernameLineEdit.text()
                password = ui.passwordLineEdit.text()

                cursor.execute("insert into person(id, username, password) values({},'{}','{}')".format(id, username, password))
                connect.commit()
                ui.idLineEdit.clear()
                ui.usernameLineEdit.clear()
                ui.passwordLineEdit.clear()

                view()
            except sql.OperationalError:
                QMessageBox.information(MainWindow,"Warning","Username, password and id is can not be empty", QMessageBox.Ok)

        def delete():
            try:
                selected = ui.tableWidget.selectedItems()
                ui.idLineEdit.setText(selected[0].text())
                ui.usernameLineEdit.setText(selected[1].text())
                ui.passwordLineEdit.setText(selected[2].text())

                cursor.execute("delete from person where id = '{}'".format(int(ui.idLineEdit.text())))
                connect.commit()
                
                view()
                
            except IndexError:
                QMessageBox.information(MainWindow, "Warning", "Please select valid value!", QMessageBox.Ok)

        def update():
            select()

            cursor.execute("update person set password = '{}' where password = '{}'".format(ui.secondPasswordLineEdit.text(), ui.passwordLineEdit.text()))            
            connect.commit()

            ui.secondPasswordLineEdit.clear()

            ui.secondPasswordLineEdit.setVisible(False)

            view()

        def view():
            ui.tableWidget.clear()
            ui.tableWidget.setHorizontalHeaderLabels(('id', 'username', 'password'))
            ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            cursor.execute("select * from person")

            for lineIndex, rowData in enumerate(cursor):
                for colomnIndex, colomnData in enumerate (rowData):
                    ui.tableWidget.setItem(lineIndex, colomnIndex,QTableWidgetItem(str(colomnData)))

            ui.idLineEdit.clear()
            ui.usernameLineEdit.clear()
            ui.passwordLineEdit.clear()

        ui.addButton.clicked.connect(add)
        ui.deleteButton.clicked.connect(delete)
        ui.viewButton.clicked.connect(view)
        ui.updateButton.clicked.connect(update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.passwordLineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.usernameLineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.viewButton.setText(_translate("MainWindow", "View"))
        self.idLineEdit.setPlaceholderText(_translate("MainWindow", "ID"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.secondPasswordLineEdit.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.selectDatas.setText(_translate("MainWindow", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())