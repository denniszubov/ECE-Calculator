from helper_methods import translate_input, correct_binary_num
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(200, 10, 431, 61))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.truth_table = QtWidgets.QTableWidget(self.centralwidget)
        self.truth_table.setEnabled(False)
        self.truth_table.setGeometry(QtCore.QRect(110, 190, 591, 341))
        self.truth_table.setRowCount(0)
        self.truth_table.setColumnCount(0)
        self.truth_table.setObjectName("truth_table")

        # item = QtWidgets.QTableWidgetItem()
        # self.truth_table.setItem(0, 0, item)
        

        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(350, 140, 113, 32))
        self.calculate_button.setObjectName("calculate_button")

        self.boolean_equation_text_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.boolean_equation_text_box.setGeometry(QtCore.QRect(220, 90, 371, 41))
        self.boolean_equation_text_box.setObjectName("boolean_equation_text_box")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Calculate button pushed
        self.calculate_button.clicked.connect(self.calculate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Truth Table Generator"))
        __sortingEnabled = self.truth_table.isSortingEnabled()
        self.truth_table.setSortingEnabled(False)
        self.truth_table.setSortingEnabled(__sortingEnabled)
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))

    def calculate(self):
        self.truth_table.setEnabled(True)
        # Get text
        input_expression = self.boolean_equation_text_box.toPlainText()
        table_info = translate_input(input_expression)
        eval_expression = table_info["expression"]
        num_inputs = table_info["num_inputs"]
        chars = table_info["input_chars"]

        self.truth_table.setRowCount(2 ** num_inputs)
        self.truth_table.setColumnCount(num_inputs+1)
        # Populating horizontal headers with input characters
        output_header_item = QtWidgets.QTableWidgetItem("Output")
        self.truth_table.setHorizontalHeaderItem(num_inputs, output_header_item)
        for i in range(num_inputs):
            header_item = QtWidgets.QTableWidgetItem(chars[i])
            self.truth_table.setHorizontalHeaderItem(i, header_item)
        # Populating vertical headers
        for i in range(2 ** num_inputs):
            header_item = QtWidgets.QTableWidgetItem(str(i))
            self.truth_table.setVerticalHeaderItem(i, header_item)
        
        #Populating table and output value
        for i in range(2 ** num_inputs):
            current_expression = eval_expression
            # Creates a string representation of the binary number (loop count )
            # that is padded with 0s as neccessary.
            bin_num = correct_binary_num(str(bin(i))[2:], num_inputs)
            for j in range(num_inputs):
                bin_digit = bin_num[j]
                cell_item = QtWidgets.QTableWidgetItem(bin_digit)
                self.truth_table.setItem(i, j, cell_item)
                # Change characters in expression to 1s and 0s.
                current_expression = current_expression.replace(chars[j], bin_digit)
            eval_answer = eval(current_expression)
            # Weird output with (~) not operator
            if eval_answer < 0:
                eval_answer += 2
            output_item = QtWidgets.QTableWidgetItem(str(eval_answer))
            self.truth_table.setItem(i, num_inputs, output_item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
