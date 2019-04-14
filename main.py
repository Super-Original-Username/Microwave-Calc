from mainwindow import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math
import sys
import keyboard

class Unbuffered:

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush

    def flush(self):
        self.stream.flush

    def close(self):
        self.stream.close


class MainWindow(Ui_MainWindow):
    def __init__(self,dialog):
        super(MainWindow,self).__init__()

        self.setupUi(dialog)
        self.conv_btn.clicked.connect(self.converter)
        

    def converter(self):
        base = self.initial_t.text()
        ratio = self.find_ratio()
        print(ratio)
        base_decimal_split = base.split(":")
        base_decimal = float(base_decimal_split[0]) + (float(base_decimal_split[1])/60)
        print(base_decimal)
        t = ratio*base_decimal
        print(t)
        split_time = math.modf(t)
        print(split_time)
        seconds = str(round(split_time[0] * 60))
        if int(seconds) < 10:
            seconds = '0' + seconds
        print(seconds)
        converted_time = str(int(split_time[1])) + ':' + seconds
        print(converted_time)
        self.new_t.setText(converted_time)
        QApplication.processEvents()


    def find_ratio(self):
        p1 = float(self.initial_p.text())
        p2 = float(self.target_p.text())
        ratio = p1/p2
        #print(ratio)
        return ratio


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QMainWindow()
    m_gui = MainWindow(form)
    form.show()
    sys.stdout = Unbuffered(sys.stdout)

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback): # Catches exceptions that QT likes to hide
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook
    app.exec_()