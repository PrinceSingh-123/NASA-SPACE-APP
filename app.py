
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,QWidget,QMessageBox,QDialog
import sys

from numpy import float16
from Ui_main import Ui_MainWindow
import pickle

# main windows
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        
        self.predict.clicked.connect(self.prediction)
        
    def prediction(self):
        bf1 = self.bf1.text()
        print(bf1)
        # ampl1_i = self.ampl1_i.Text()
        # bgse = self.bgse.Text()
        # time_pb5 = self.time_pb5.Text()
        
        # load model from disk
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        bf1 = [[float(bf1)]]
        
        result = loaded_model.predict(bf1)
        
        result = result.item()
        
        result = float16(result)
        
        self.result.setText(str(result))
        

        
# main function to execute
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()    