# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickmultiattributeedit_update_selected_form.ui'
#
# Created: Tue Feb 14 17:11:16 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_quickmultiattributeedit_update_selected_form(object):
    def setupUi(self, quickmultiattributeedit_update_selected_form):
        quickmultiattributeedit_update_selected_form.setObjectName(_fromUtf8("quickmultiattributeedit_update_selected_form"))
        quickmultiattributeedit_update_selected_form.resize(471, 140)
        quickmultiattributeedit_update_selected_form.setWindowTitle(QtGui.QApplication.translate("quickmultiattributeedit_update_selected_form", "MBupSelected", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(quickmultiattributeedit_update_selected_form)
        self.buttonBox.setGeometry(QtCore.QRect(120, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.CBfields = QtGui.QComboBox(quickmultiattributeedit_update_selected_form)
        self.CBfields.setGeometry(QtCore.QRect(10, 40, 211, 24))
        self.CBfields.setObjectName(_fromUtf8("CBfields"))
        self.QLEvalore = QtGui.QLineEdit(quickmultiattributeedit_update_selected_form)
        self.QLEvalore.setGeometry(QtCore.QRect(300, 40, 161, 24))
        self.QLEvalore.setObjectName(_fromUtf8("QLEvalore"))
        self.label = QtGui.QLabel(quickmultiattributeedit_update_selected_form)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText(QtGui.QApplication.translate("quickmultiattributeedit_update_selected_form", "For all selected elements in the current layer set the value of field:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(quickmultiattributeedit_update_selected_form)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 61, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setText(QtGui.QApplication.translate("quickmultiattributeedit_update_selected_form", "equal to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(quickmultiattributeedit_update_selected_form)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 451, 16))
        self.label_3.setText(QtGui.QApplication.translate("quickmultiattributeedit_update_selected_form", "You can also activate this form with F12 funct key - by Marco Braida 2011", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(quickmultiattributeedit_update_selected_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), quickmultiattributeedit_update_selected_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), quickmultiattributeedit_update_selected_form.reject)
        QtCore.QMetaObject.connectSlotsByName(quickmultiattributeedit_update_selected_form)

    def retranslateUi(self, quickmultiattributeedit_update_selected_form):
        pass

