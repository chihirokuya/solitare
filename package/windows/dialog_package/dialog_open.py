from package.windows.dialog_package.dialog import Ui_Dialog
from PyQt6 import QtWidgets


def open_dialog(err_message):
    dialog = QtWidgets.QDialog()
    dialog_ui = Ui_Dialog()
    dialog_ui.setupUi(dialog)

    dialog_ui.label.setText(err_message)

    dialog.setModal(True)

    dialog.show()
    dialog.exec()


def open_no_modal_dialog(err_message):
    dialog = QtWidgets.QDialog()
    dialog_ui = Ui_Dialog()
    dialog_ui.setupUi(dialog)

    dialog_ui.label.setText(err_message)

    dialog.show()
    dialog.exec()