import os.path
from package.windows.main import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore, QtGui
import sys
import subprocess
from package.game import Game

_original_constructor = subprocess.Popen.__init__


def _patched_constructor(*args, **kwargs):
    for key in ('stdin', 'stdout', 'stderr'):
        if key not in kwargs:
            kwargs[key] = subprocess.PIPE

    return _original_constructor(*args, **kwargs)


subprocess.Popen.__init__ = _patched_constructor


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def setup(self):
        game = Game(self.ui)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setup()
    window.show()

    sys.exit(app.exec())
