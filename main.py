import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from main_window import Ui_mainWindow
from pathlib import Path
from PIL import Image

class Redimensionador(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_open.clicked.connect(self.abrir_imagem)
        self.btnSaveRoot.clicked.connect(self.get_root)
        self.btn_redefinir.clicked.connect(self.redimensionar)
        self.setWindowIcon(QIcon('crop_23893.ico'))

    def abrir_imagem(self):
        self.imagens, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Abrir Imagem',
            f'{Path.home()}',
            'Images (*.png *.jpg *.jpeg)'
        )
        self.listWidget.clear()
        self.listWidget.addItems(self.imagens)

        print(self.imagens)

    def get_root(self):
        self.save_root = QFileDialog.getExistingDirectory(directory=f'{Path.home()}')
        self.lblSaveRoot.setPlaceholderText(self.save_root)
        
    
    def redimensionar(self):

        width = int(self.inptLargura.text())
        height = int(self.inptAltura.text())
        extension = self.inptFileNamePlus.text()

        for imagem in self.imagens:
            with Image.open(imagem) as resize:
                
                if self.radioButton.isChecked():
                    resized = resize
                    resized.thumbnail(size=(width, height))
                else:
                    resized = resize.resize(size=(width, height))
                resized.save(f'{self.save_root}\
/{Path(imagem).stem + extension + Path(imagem).suffix}')

    def salvar(self):
        self.redimensionar(
            width=self.inptLargura.text(),
            height=self.inptAltura.text(),
            extension=self.inptFileNamePlus.text(),)
    

    



        

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    redimensionador = Redimensionador()
    redimensionador.show()
    qt.exec_()


