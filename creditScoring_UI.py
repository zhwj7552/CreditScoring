# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditScoring_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pylab

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(744, 688)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 130, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(510, 20, 91, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(520, 390, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(490, -10, 20, 891))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 340, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox_15 = QtGui.QComboBox(Dialog)
        self.comboBox_15.setGeometry(QtCore.QRect(510, 160, 78, 27))
        self.comboBox_15.setObjectName(_fromUtf8("comboBox_15"))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(520, 420, 201, 221))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 340, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        '''
        self.fileDialog = QtGui.QFileDialog(Dialog)
        self.fileDialog.setGeometry(QtCore.QRect(510, 60, 111, 27))
        self.fileDialog.setObjectName(_fromUtf8("fileDialog"))
        '''
        '''
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(510, 60, 111, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        '''


        self.fileButton = QtGui.QPushButton(Dialog)
        self.fileButton.setGeometry(QtCore.QRect(510, 60, 111, 27))
        self.fileButton.setObjectName(_fromUtf8("QPushButton"))

        self.filePathBrowser = QtGui.QTextBrowser(Dialog)
        self.filePathBrowser.setGeometry(QtCore.QRect(630, 60, 100, 27))
        self.filePathBrowser.setObjectName(_fromUtf8("filePathBrowser"))

        self.spinBox_4 = QtGui.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(42, 88, 181, 27))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(42, 416, 76, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(42, 62, 47, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(42, 147, 181, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(42, 121, 68, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_23 = QtGui.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(42, 180, 76, 20))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(42, 206, 181, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(42, 475, 76, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(42, 239, 76, 20))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.comboBox_4 = QtGui.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(42, 265, 181, 27))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.setItemText(4, _fromUtf8(""))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(42, 298, 68, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.comboBox_5 = QtGui.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(42, 324, 181, 27))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.label_24 = QtGui.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(42, 357, 76, 20))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.comboBox_6 = QtGui.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(42, 383, 181, 27))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_7 = QtGui.QComboBox(Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(42, 442, 181, 27))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.spinBox_3 = QtGui.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(42, 501, 181, 27))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(42, 534, 76, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.comboBox_8 = QtGui.QComboBox(Dialog)
        self.comboBox_8.setGeometry(QtCore.QRect(42, 560, 181, 27))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(42, 593, 67, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox_9 = QtGui.QComboBox(Dialog)
        self.comboBox_9.setGeometry(QtCore.QRect(42, 619, 181, 27))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(235, 416, 120, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(235, 62, 76, 20))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.comboBox_10 = QtGui.QComboBox(Dialog)
        self.comboBox_10.setGeometry(QtCore.QRect(235, 147, 181, 27))
        self.comboBox_10.setObjectName(_fromUtf8("comboBox_10"))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.spinBox_6 = QtGui.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(235, 88, 181, 27))
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(235, 121, 67, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(235, 180, 82, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(235, 206, 181, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(235, 475, 141, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(235, 239, 68, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.comboBox_11 = QtGui.QComboBox(Dialog)
        self.comboBox_11.setGeometry(QtCore.QRect(235, 265, 181, 27))
        self.comboBox_11.setObjectName(_fromUtf8("comboBox_11"))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(235, 298, 68, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_12 = QtGui.QComboBox(Dialog)
        self.comboBox_12.setGeometry(QtCore.QRect(235, 324, 181, 27))
        self.comboBox_12.setObjectName(_fromUtf8("comboBox_12"))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(235, 357, 83, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(235, 383, 181, 27))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_5 = QtGui.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(235, 442, 181, 27))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.comboBox_13 = QtGui.QComboBox(Dialog)
        self.comboBox_13.setGeometry(QtCore.QRect(235, 501, 181, 27))
        self.comboBox_13.setObjectName(_fromUtf8("comboBox_13"))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(235, 534, 134, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.comboBox_14 = QtGui.QComboBox(Dialog)
        self.comboBox_14.setGeometry(QtCore.QRect(235, 560, 181, 27))
        self.comboBox_14.setObjectName(_fromUtf8("comboBox_14"))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(235, 593, 184, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(235, 619, 181, 27))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.spinBox_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.comboBox_15.raise_()
        self.textBrowser.raise_()
        self.pushButton_2.raise_()
        self.fileButton.raise_()
        self.filePathBrowser.raise_()

        self.retranslateUi(Dialog)

        '''
        #QtCore.QObject.connect(self.spinBox_4, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        #QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_3, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_4, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_5, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_6, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_7, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_8, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_9, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.spinBox_6, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_11, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_11, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_12, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        QtCore.QObject.connect(self.spinBox_5, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_13, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_14, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.doubleSpinBox, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pushButton.click)
        #QtCore.QObject.connect(self.kurlcomborequester, QtCore.SIGNAL(_fromUtf8("openFileDialog(KUrlRequester*)")), self.pushButton.click)
        QtCore.QObject.connect(self.comboBox_15, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.forward)
        QtCore.QObject.connect(self.comboBox_10, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.pushButton.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        '''
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "个人信用评估", None))
        self.label.setText(_translate("Dialog", "选择分类器", None))
        self.label_2.setText(_translate("Dialog", "上传文件", None))
        self.label_3.setText(_translate("Dialog", "用户信息", None))
        self.label_4.setText(_translate("Dialog", "输出", None))
        self.pushButton.setText(_translate("Dialog", "信用评估", None))
        self.comboBox_15.setItemText(0, _translate("Dialog", "KNN", None))
        self.comboBox_15.setItemText(1, _translate("Dialog", "LR", None))
        self.comboBox_15.setItemText(2, _translate("Dialog", "SVM", None))
        self.pushButton_2.setText(_translate("Dialog", "刷新", None))
        self.spinBox_4.setToolTip(_translate("Dialog", "用户的年龄", None))
        self.label_19.setText(_translate("Dialog", "住房性质", None))
        self.label_17.setText(_translate("Dialog", "年龄", None))
        self.comboBox_2.setToolTip(_translate("Dialog", "用户的性别及婚姻状况", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "男性：离婚/分居", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "女性：离婚/分居/已婚", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "男性：单身", None))
        self.comboBox_2.setItemText(3, _translate("Dialog", "男性：已婚/丧偶", None))
        self.comboBox_2.setItemText(4, _translate("Dialog", "女性：单身", None))
        self.label_13.setText(_translate("Dialog", "个人状态", None))
        self.label_23.setText(_translate("Dialog", "电话验证", None))
        self.comboBox_3.setToolTip(_translate("Dialog", "用户是否有电话验证", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "无", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "有且用本名注册", None))
        self.label_15.setText(_translate("Dialog", "居住时间", None))
        self.label_21.setText(_translate("Dialog", "工作性质", None))
        self.comboBox_4.setToolTip(_translate("Dialog", "用户的工作性质", None))
        self.comboBox_4.setItemText(0, _translate("Dialog", "无业/无技能-非常住人口", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "无技能-常住人口", None))
        self.comboBox_4.setItemText(2, _translate("Dialog", "有技能从业者/公务员", None))
        self.comboBox_4.setItemText(3, _translate("Dialog", "管理者/创业者/高级职员/政府官员", None))
        self.label_11.setText(_translate("Dialog", "工作年限", None))
        self.comboBox_5.setToolTip(_translate("Dialog", "用户在当前单位的工作年限", None))
        self.comboBox_5.setItemText(0, _translate("Dialog", "无业人员", None))
        self.comboBox_5.setItemText(1, _translate("Dialog", "少于1年", None))
        self.comboBox_5.setItemText(2, _translate("Dialog", "1年-4年", None))
        self.comboBox_5.setItemText(3, _translate("Dialog", "4年-7年", None))
        self.comboBox_5.setItemText(4, _translate("Dialog", "超过7年", None))
        self.label_24.setText(_translate("Dialog", "是否外籍", None))
        self.comboBox_6.setToolTip(_translate("Dialog", "用户是否为外国籍", None))
        self.comboBox_6.setItemText(0, _translate("Dialog", "是", None))
        self.comboBox_6.setItemText(1, _translate("Dialog", "否", None))
        self.comboBox_7.setToolTip(_translate("Dialog", "用户当前住房的性质", None))
        self.comboBox_7.setItemText(0, _translate("Dialog", "租房", None))
        self.comboBox_7.setItemText(1, _translate("Dialog", "自己的", None))
        self.comboBox_7.setItemText(2, _translate("Dialog", "免费居住", None))
        self.spinBox_3.setToolTip(_translate("Dialog", "用户在当前房子的居住时间", None))
        self.label_16.setText(_translate("Dialog", "个人财产", None))
        self.comboBox_8.setToolTip(_translate("Dialog", "用户个人拥有的财产情况", None))
        self.comboBox_8.setItemText(0, _translate("Dialog", "不动产", None))
        self.comboBox_8.setItemText(1, _translate("Dialog", "building society savings agreement/life insurance", None))
        self.comboBox_8.setItemText(2, _translate("Dialog", "汽车或其他（银行存款不算）", None))
        self.comboBox_8.setItemText(3, _translate("Dialog", "不知/没有", None))
        self.label_8.setText(_translate("Dialog", "贷款目的", None))
        self.comboBox_9.setToolTip(_translate("Dialog", "用户的贷款目的", None))
        self.comboBox_9.setItemText(0, _translate("Dialog", "新车", None))
        self.comboBox_9.setItemText(1, _translate("Dialog", "二手车", None))
        self.comboBox_9.setItemText(2, _translate("Dialog", "家具", None))
        self.comboBox_9.setItemText(3, _translate("Dialog", "广播/电视", None))
        self.comboBox_9.setItemText(4, _translate("Dialog", "家用电器", None))
        self.comboBox_9.setItemText(5, _translate("Dialog", "修理", None))
        self.comboBox_9.setItemText(6, _translate("Dialog", "教育", None))
        self.comboBox_9.setItemText(7, _translate("Dialog", "培训", None))
        self.comboBox_9.setItemText(8, _translate("Dialog", "商业", None))
        self.comboBox_9.setItemText(9, _translate("Dialog", "其他", None))
        self.label_20.setText(_translate("Dialog", "本行信用卡数量", None))
        self.label_22.setText(_translate("Dialog", "供养人口", None))
        self.comboBox_10.setToolTip(_translate("Dialog", "用户拥有的支票账户的金额", None))
        self.comboBox_10.setItemText(0, _translate("Dialog", "0", None))
        self.comboBox_10.setItemText(1, _translate("Dialog", "0-200DM", None))
        self.comboBox_10.setItemText(2, _translate("Dialog", ">=200DM", None))
        self.comboBox_10.setItemText(3, _translate("Dialog", "无", None))
        self.spinBox_6.setToolTip(_translate("Dialog", "用户当前所要供养的人数", None))
        self.label_5.setText(_translate("Dialog", "支票账户", None))
        self.label_6.setText(_translate("Dialog", "支票有效期", None))
        self.spinBox.setToolTip(_translate("Dialog", "用户支票的有效期", None))
        self.label_14.setText(_translate("Dialog", "其他债务人/担保人", None))
        self.label_10.setText(_translate("Dialog", "账户存款", None))
        self.comboBox_11.setToolTip(_translate("Dialog", "用户拥有的存款", None))
        self.comboBox_11.setItemText(0, _translate("Dialog", "<100DM", None))
        self.comboBox_11.setItemText(1, _translate("Dialog", "100-500DM", None))
        self.comboBox_11.setItemText(2, _translate("Dialog", "500-1000DM", None))
        self.comboBox_11.setItemText(3, _translate("Dialog", ">=1000DM", None))
        self.comboBox_11.setItemText(4, _translate("Dialog", "不知/无", None))
        self.label_7.setText(_translate("Dialog", "信用历史", None))
        self.comboBox_12.setToolTip(_translate("Dialog", "用户使用信用卡的历史", None))
        self.comboBox_12.setItemText(0, _translate("Dialog", "无信用卡/均已还清", None))
        self.comboBox_12.setItemText(1, _translate("Dialog", "本行的信用卡均已还清", None))
        self.comboBox_12.setItemText(2, _translate("Dialog", "现有的信用卡均已还清", None))
        self.comboBox_12.setItemText(3, _translate("Dialog", "有逾期还款记录", None))
        self.comboBox_12.setItemText(4, _translate("Dialog", "重要账户不在本行", None))
        self.label_9.setText(_translate("Dialog", "信用卡欠款", None))
        self.spinBox_2.setToolTip(_translate("Dialog", "用户信用卡欠款的数目", None))
        self.spinBox_5.setToolTip(_translate("Dialog", "用户在本行开设的信用卡账户数量", None))
        self.comboBox_13.setToolTip(_translate("Dialog", "用户是否拥有其他债务人或担保人", None))
        self.comboBox_13.setItemText(0, _translate("Dialog", "无", None))
        self.comboBox_13.setItemText(1, _translate("Dialog", "联合申请人", None))
        self.comboBox_13.setItemText(2, _translate("Dialog", "担保人", None))
        self.label_18.setText(_translate("Dialog", "其他分期付款计划", None))
        self.comboBox_14.setToolTip(_translate("Dialog", "用户是否有其他分期付款的项目", None))
        self.comboBox_14.setItemText(0, _translate("Dialog", "银行", None))
        self.comboBox_14.setItemText(1, _translate("Dialog", "商店", None))
        self.comboBox_14.setItemText(2, _translate("Dialog", "无", None))
        self.label_12.setText(_translate("Dialog", "分期付款占可支配收入的比重", None))
        self.doubleSpinBox.setToolTip(_translate("Dialog", "本次贷款的每月分期付款占用户可支配收入的百分比", None))
        self.fileButton.setText(_translate("Dialog", "选择文件", None))

