#Import pyqt 5,pandas dan sklearn nya dulu
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from sklearn import linear_model

#INI ADALAH PEMBENTUKAN UI NYA
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 318)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 110, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 150, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 250, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 250, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton.clicked.connect(self.func)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "APLIKASI PREDIKSI HARGA RUMAH"))
        self.label_2.setText(_translate("Form", "Masukan Luas Rumah"))
        self.label_3.setText(_translate("Form", "Masukan Jumlah Kasur yang di inginkan"))
        self.pushButton.setText(_translate("Form", "CARI"))
        self.label_5.setText(_translate("Form", "Kurang Lebih Harganya"))

    #Fungsi Prediksi nya
    def func(self):
        # INI ADALAH IMPLEMENTASI Multiple Regression Python
        # Regresi berganda variabelnya lebih dari satu
        # Y’ = a + b1X1+ b2X2+…..+ bnXn
        # Y’= Variabel dependen (nilai yang diprediksikan).
        # X1 dan X2 = Variabel independen.
        # a Konstanta (nilai Y’ apabila X1, X2…..Xn = 0).
        # b Koefisien regresi (nilai peningkatan ataupun penurunan).
        # Ini manggil file CSV nya data harga rumah
        # Di Definisikan Sebagai df
        df = pd.read_csv("harga_rumah.csv")


        #Disini ada 2 variable x dan y yang di definisikan masing2
        x = df[["luas", "kasur"]]
        y = df["harga"]

        #Setelah itu menggunakan library sklearn menggunakan fungsi Linear regression
        regr = linear_model.LinearRegression()
        regr.fit(x, y)

        #Di program saya membuat lineedit untuk memasukan kriteria2 yang di inginkan ketika ingin memprediksi harga rumah
        # A didefinisikan sebagai Luas rumah
        # B didefinisikan sebagai Jumlah kasur
        a=int(self.lineEdit.text())
        b=int(self.lineEdit_2.text())

        #disini baru di prediksi
        prediksirumah = regr.predict([[a, b]])
        #Setelah itu hasil nya di tampilkan
        self.label_4.setText(str(prediksirumah))
        print(prediksirumah)

        #Padasarnya aplikasi ini bergantung pada data yang dimasukkan
        #Karna machine learning memprediksi data yang telah di masukkan tadi , yaitu data harga rumah

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
