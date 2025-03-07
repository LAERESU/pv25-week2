import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        
        groupIdentity = QGroupBox("Identity")
        layoutIdentity = QVBoxLayout()
        layoutIdentity.addWidget(QLabel("Nama : Yusril Ibtida Ramdhani"))
        layoutIdentity.addWidget(QLabel("Nim : F1D022102"))
        layoutIdentity.addWidget(QLabel("Kelas : D"))
        groupIdentity.setLayout(layoutIdentity)
        
        groupNavigation = QGroupBox("Navigation")
        layoutNavigation = QHBoxLayout()
        layoutNavigation.addWidget(QPushButton("Home"))
        layoutNavigation.addWidget(QPushButton("About"))
        layoutNavigation.addWidget(QPushButton("Contact"))
        groupNavigation.setLayout(layoutNavigation)
        
        groupRegis = QGroupBox("Registration Form")
        layoutRegis = QFormLayout()
        layoutRegis.addRow("Full Name:", QLineEdit())
        layoutRegis.addRow("Email:", QLineEdit())
        layoutRegis.addRow("Phone:", QLineEdit())
        
        genderWidget = QWidget()
        genderLayout = QHBoxLayout()

        # Menambahkan pilihan dengan radio button
        genderLayout.addWidget(QRadioButton("Male"))
        genderLayout.addWidget(QRadioButton("Female"))
        genderWidget.setLayout(genderLayout)
        layoutRegis.addRow("Gender:", genderWidget)
    
        countryBox = QComboBox()
        #Masukkan sekaligus
        # countryBox.addItems(["", "Indonesia", "Malaysia", "Japan", "Korea", "Argentina", "Spain", "Australia", "USA"])

        #Masukkan satu persatu
        countryBox.addItem("Indonesia")
        countryBox.addItem("Malaysia")
        countryBox.addItem("Japan")
        countryBox.addItem("Korea")
        countryBox.addItem("Argentina")
        countryBox.addItem("Spain")
        countryBox.addItem("Australia")
        countryBox.addItem("USA")
        layoutRegis.addRow("Country:", countryBox)
        
        # Isi groupRegis dengan layoutRegis
        groupRegis.setLayout(layoutRegis)
        
        groupActions = QGroupBox("Actions")
        layoutActions = QHBoxLayout()
        layoutActions.addWidget(QPushButton("Submit"))
        layoutActions.addWidget(QPushButton("Cancel"))
        groupActions.setLayout(layoutActions)
        
        # Masukkan semua group ke dalam main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupIdentity)
        mainLayout.addWidget(groupNavigation)
        mainLayout.addWidget(groupRegis)
        mainLayout.addWidget(groupActions)
        
        self.setLayout(mainLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())