# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_win0(object):
    def setupUi(self, win0):
        win0.setObjectName("win0")
        win0.resize(1529, 856)
        win0.setStyleSheet("background-color: rgba(29, 29, 29);\n"
"color: rgb(171, 171, 171);")
        self.centralwidget = QtWidgets.QWidget(win0)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(3, 9, 1365, 801))
        self.tabs.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabs.setTabsClosable(False)
        self.tabs.setObjectName("tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.table1 = QtWidgets.QTableWidget(self.tab1)
        self.table1.setGeometry(QtCore.QRect(24, 20, 544, 739))
        font = QtGui.QFont()
        font.setKerning(True)
        self.table1.setFont(font)
        self.table1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table1.setStyleSheet("background-color: rgba(100, 100, 100, 100);\n"
"border-color: rgb(47, 47, 47);\n"
"gridline-color: rgb(255, 255, 255);\n"
"color: rgb(100, 100, 100);\n"
"gridline-color: rgb(40, 40, 40);")
        self.table1.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setRowCount(100)
        self.table1.setColumnCount(5)
        self.table1.setObjectName("table1")
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(4, item)
        self.table1.horizontalHeader().setDefaultSectionSize(100)
        self.table1.verticalHeader().setDefaultSectionSize(20)
        self.configurate_selection_frame = QtWidgets.QFrame(self.tab1)
        self.configurate_selection_frame.setGeometry(QtCore.QRect(610, 19, 729, 448))
        self.configurate_selection_frame.setStyleSheet("border-color: rgb(65, 65, 65);\n"
"gridline-color: rgb(65, 65, 65);")
        self.configurate_selection_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configurate_selection_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configurate_selection_frame.setLineWidth(2)
        self.configurate_selection_frame.setObjectName("configurate_selection_frame")
        self.from_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.from_label.setGeometry(QtCore.QRect(224, 10, 26, 16))
        self.from_label.setObjectName("from_label")
        self.min_label_2 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.min_label_2.setGeometry(QtCore.QRect(250, 388, 19, 16))
        self.min_label_2.setObjectName("min_label_2")
        self.spin_hours_2 = QtWidgets.QSpinBox(self.configurate_selection_frame)
        self.spin_hours_2.setGeometry(QtCore.QRect(202, 366, 36, 22))
        self.spin_hours_2.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_hours_2.setObjectName("spin_hours_2")
        self.date_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.date_label.setGeometry(QtCore.QRect(24, 31, 28, 14))
        self.date_label.setObjectName("date_label")
        self.hours_label_3 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.hours_label_3.setGeometry(QtCore.QRect(339, 389, 34, 16))
        self.hours_label_3.setObjectName("hours_label_3")
        self.button_hide_all_acts = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_hide_all_acts.setGeometry(QtCore.QRect(290, 113, 35, 23))
        self.button_hide_all_acts.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_hide_all_acts.setObjectName("button_hide_all_acts")
        self.button_date_to = QtWidgets.QToolButton(self.configurate_selection_frame)
        self.button_date_to.setGeometry(QtCore.QRect(359, 29, 24, 20))
        self.button_date_to.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/calendarIcon/calendar2.jpg);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/calendarIcon/calendar2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_date_to.setIcon(icon)
        self.button_date_to.setIconSize(QtCore.QSize(18, 18))
        self.button_date_to.setObjectName("button_date_to")
        self.button_date_from = QtWidgets.QToolButton(self.configurate_selection_frame)
        self.button_date_from.setGeometry(QtCore.QRect(266, 29, 24, 20))
        self.button_date_from.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/calendarIcon/calendar2.jpg);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/calendarIcon/calendar2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../Icons/calendar2 (Pressed).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../Icons/calendar2 (Pressed).jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../Icons/calendar2 (Pressed).jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.button_date_from.setIcon(icon1)
        self.button_date_from.setIconSize(QtCore.QSize(18, 18))
        self.button_date_from.setObjectName("button_date_from")
        self.min_label_3 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.min_label_3.setGeometry(QtCore.QRect(383, 389, 19, 16))
        self.min_label_3.setObjectName("min_label_3")
        self.combo_box_ops_date = QtWidgets.QComboBox(self.configurate_selection_frame)
        self.combo_box_ops_date.setGeometry(QtCore.QRect(56, 28, 135, 20))
        self.combo_box_ops_date.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.combo_box_ops_date.setObjectName("combo_box_ops_date")
        self.time_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.time_label.setGeometry(QtCore.QRect(21, 367, 28, 16))
        self.time_label.setObjectName("time_label")
        self.spin_min_3 = QtWidgets.QSpinBox(self.configurate_selection_frame)
        self.spin_min_3.setGeometry(QtCore.QRect(373, 367, 36, 22))
        self.spin_min_3.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_min_3.setObjectName("spin_min_3")
        self.button_visible_all_acts = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_visible_all_acts.setGeometry(QtCore.QRect(290, 84, 35, 23))
        self.button_visible_all_acts.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_visible_all_acts.setObjectName("button_visible_all_acts")
        self.spin_sec_2 = QtWidgets.QSpinBox(self.configurate_selection_frame)
        self.spin_sec_2.setGeometry(QtCore.QRect(278, 366, 36, 22))
        self.spin_sec_2.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_sec_2.setObjectName("spin_sec_2")
        self.hidden_acts_list = QtWidgets.QListView(self.configurate_selection_frame)
        self.hidden_acts_list.setGeometry(QtCore.QRect(56, 83, 220, 112))
        self.hidden_acts_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.hidden_acts_list.setObjectName("hidden_acts_list")
        self.activity_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.activity_label.setGeometry(QtCore.QRect(12, 78, 42, 16))
        self.activity_label.setObjectName("activity_label")
        self.to_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.to_label.setGeometry(QtCore.QRect(322, 10, 17, 16))
        self.to_label.setObjectName("to_label")
        self.date_to = QtWidgets.QDateEdit(self.configurate_selection_frame)
        self.date_to.setGeometry(QtCore.QRect(294, 28, 65, 20))
        self.date_to.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.date_to.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date_to.setKeyboardTracking(True)
        self.date_to.setObjectName("date_to")
        self.sec_label_2 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.sec_label_2.setGeometry(QtCore.QRect(287, 389, 22, 16))
        self.sec_label_2.setObjectName("sec_label_2")
        self.spin_hours_3 = QtWidgets.QSpinBox(self.configurate_selection_frame)
        self.spin_hours_3.setGeometry(QtCore.QRect(335, 367, 36, 22))
        self.spin_hours_3.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_hours_3.setObjectName("spin_hours_3")
        self.spin_sec_3 = QtWidgets.QSpinBox(self.configurate_selection_frame)
        self.spin_sec_3.setGeometry(QtCore.QRect(411, 367, 36, 22))
        self.spin_sec_3.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_sec_3.setObjectName("spin_sec_3")
        self.spin_min_2 = QtWidgets.QSpinBox(self.configurate_selection_frame)
        self.spin_min_2.setGeometry(QtCore.QRect(240, 366, 36, 22))
        self.spin_min_2.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_min_2.setObjectName("spin_min_2")
        self.activities_show_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.activities_show_label.setGeometry(QtCore.QRect(409, 65, 74, 16))
        self.activities_show_label.setObjectName("activities_show_label")
        self.date_from = QtWidgets.QDateEdit(self.configurate_selection_frame)
        self.date_from.setGeometry(QtCore.QRect(202, 28, 65, 21))
        self.date_from.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.date_from.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date_from.setKeyboardTracking(True)
        self.date_from.setObjectName("date_from")
        self.combo_box_ops_time = QtWidgets.QComboBox(self.configurate_selection_frame)
        self.combo_box_ops_time.setGeometry(QtCore.QRect(54, 367, 135, 20))
        self.combo_box_ops_time.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.combo_box_ops_time.setObjectName("combo_box_ops_time")
        self.hours_label_2 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.hours_label_2.setGeometry(QtCore.QRect(206, 388, 34, 16))
        self.hours_label_2.setObjectName("hours_label_2")
        self.sec_label_3 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.sec_label_3.setGeometry(QtCore.QRect(420, 390, 22, 16))
        self.sec_label_3.setObjectName("sec_label_3")
        self.all_activities_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.all_activities_label.setGeometry(QtCore.QRect(129, 66, 81, 16))
        self.all_activities_label.setObjectName("all_activities_label")
        self.default_button = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.default_button.setGeometry(QtCore.QRect(21, 406, 75, 23))
        self.default_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.default_button.setObjectName("default_button")
        self.visible_acts_list = QtWidgets.QListView(self.configurate_selection_frame)
        self.visible_acts_list.setGeometry(QtCore.QRect(336, 83, 220, 112))
        self.visible_acts_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.visible_acts_list.setObjectName("visible_acts_list")
        self.configurate_selection_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.configurate_selection_label.setGeometry(QtCore.QRect(13, 7, 133, 16))
        self.configurate_selection_label.setObjectName("configurate_selection_label")
        self.button_visible_act = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_visible_act.setGeometry(QtCore.QRect(290, 142, 35, 23))
        self.button_visible_act.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_visible_act.setObjectName("button_visible_act")
        self.button_hide_act = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_hide_act.setGeometry(QtCore.QRect(290, 171, 35, 23))
        self.button_hide_act.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_hide_act.setObjectName("button_hide_act")
        self.people_show_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.people_show_label.setGeometry(QtCore.QRect(411, 208, 69, 16))
        self.people_show_label.setObjectName("people_show_label")
        self.all_people_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.all_people_label.setGeometry(QtCore.QRect(130, 209, 72, 16))
        self.all_people_label.setObjectName("all_people_label")
        self.button_hide_people = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_hide_people.setGeometry(QtCore.QRect(289, 314, 35, 23))
        self.button_hide_people.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_hide_people.setObjectName("button_hide_people")
        self.button_hide_all_people = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_hide_all_people.setGeometry(QtCore.QRect(289, 256, 35, 23))
        self.button_hide_all_people.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_hide_all_people.setObjectName("button_hide_all_people")
        self.people_label = QtWidgets.QLabel(self.configurate_selection_frame)
        self.people_label.setGeometry(QtCore.QRect(11, 221, 42, 16))
        self.people_label.setObjectName("people_label")
        self.button_visible_people = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_visible_people.setGeometry(QtCore.QRect(289, 285, 35, 23))
        self.button_visible_people.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_visible_people.setObjectName("button_visible_people")
        self.visible_people_list = QtWidgets.QListView(self.configurate_selection_frame)
        self.visible_people_list.setGeometry(QtCore.QRect(335, 226, 220, 112))
        self.visible_people_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.visible_people_list.setObjectName("visible_people_list")
        self.button_visible_all_people = QtWidgets.QPushButton(self.configurate_selection_frame)
        self.button_visible_all_people.setGeometry(QtCore.QRect(289, 227, 35, 23))
        self.button_visible_all_people.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.button_visible_all_people.setObjectName("button_visible_all_people")
        self.hidden_people_list = QtWidgets.QListView(self.configurate_selection_frame)
        self.hidden_people_list.setGeometry(QtCore.QRect(55, 226, 220, 112))
        self.hidden_people_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.hidden_people_list.setObjectName("hidden_people_list")
        self.from_label_2 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.from_label_2.setGeometry(QtCore.QRect(247, 348, 26, 16))
        self.from_label_2.setObjectName("from_label_2")
        self.to_label_2 = QtWidgets.QLabel(self.configurate_selection_frame)
        self.to_label_2.setGeometry(QtCore.QRect(386, 350, 17, 16))
        self.to_label_2.setObjectName("to_label_2")
        self.manage_register_frame = QtWidgets.QFrame(self.tab1)
        self.manage_register_frame.setGeometry(QtCore.QRect(610, 487, 696, 272))
        self.manage_register_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manage_register_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manage_register_frame.setObjectName("manage_register_frame")
        self.spin_hours = QtWidgets.QSpinBox(self.manage_register_frame)
        self.spin_hours.setGeometry(QtCore.QRect(124, 50, 36, 22))
        self.spin_hours.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_hours.setObjectName("spin_hours")
        self.sec_label = QtWidgets.QLabel(self.manage_register_frame)
        self.sec_label.setGeometry(QtCore.QRect(209, 31, 22, 16))
        self.sec_label.setObjectName("sec_label")
        self.spin_min = QtWidgets.QSpinBox(self.manage_register_frame)
        self.spin_min.setGeometry(QtCore.QRect(162, 50, 36, 22))
        self.spin_min.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_min.setObjectName("spin_min")
        self.spin_sec = QtWidgets.QSpinBox(self.manage_register_frame)
        self.spin_sec.setGeometry(QtCore.QRect(200, 50, 36, 22))
        self.spin_sec.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.spin_sec.setObjectName("spin_sec")
        self.hours_label = QtWidgets.QLabel(self.manage_register_frame)
        self.hours_label.setGeometry(QtCore.QRect(128, 30, 34, 16))
        self.hours_label.setObjectName("hours_label")
        self.min_label = QtWidgets.QLabel(self.manage_register_frame)
        self.min_label.setGeometry(QtCore.QRect(172, 30, 19, 16))
        self.min_label.setObjectName("min_label")
        self.button_date_selected = QtWidgets.QToolButton(self.manage_register_frame)
        self.button_date_selected.setGeometry(QtCore.QRect(88, 51, 24, 20))
        self.button_date_selected.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"image: url(:/calendarIcon/calendar2.jpg);\n"
"")
        self.button_date_selected.setIcon(icon)
        self.button_date_selected.setIconSize(QtCore.QSize(18, 18))
        self.button_date_selected.setObjectName("button_date_selected")
        self.date_selected = QtWidgets.QDateEdit(self.manage_register_frame)
        self.date_selected.setGeometry(QtCore.QRect(24, 50, 65, 21))
        self.date_selected.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.date_selected.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date_selected.setKeyboardTracking(True)
        self.date_selected.setObjectName("date_selected")
        self.manage_register_label = QtWidgets.QLabel(self.manage_register_frame)
        self.manage_register_label.setGeometry(QtCore.QRect(12, 7, 97, 16))
        self.manage_register_label.setObjectName("manage_register_label")
        self.activities_list = QtWidgets.QListView(self.manage_register_frame)
        self.activities_list.setGeometry(QtCore.QRect(10, 108, 211, 84))
        self.activities_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.activities_list.setObjectName("activities_list")
        self.activities_label = QtWidgets.QLabel(self.manage_register_frame)
        self.activities_label.setGeometry(QtCore.QRect(95, 89, 45, 17))
        self.activities_label.setObjectName("activities_label")
        self.add_activity_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.add_activity_button.setGeometry(QtCore.QRect(10, 230, 33, 23))
        self.add_activity_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.add_activity_button.setObjectName("add_activity_button")
        self.update_activity_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.update_activity_button.setGeometry(QtCore.QRect(52, 230, 45, 23))
        self.update_activity_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.update_activity_button.setObjectName("update_activity_button")
        self.remove_activity_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.remove_activity_button.setGeometry(QtCore.QRect(106, 230, 45, 23))
        self.remove_activity_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.remove_activity_button.setObjectName("remove_activity_button")
        self.details_label = QtWidgets.QLabel(self.manage_register_frame)
        self.details_label.setGeometry(QtCore.QRect(334, 90, 35, 16))
        self.details_label.setObjectName("details_label")
        self.update_details_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.update_details_button.setGeometry(QtCore.QRect(283, 231, 45, 23))
        self.update_details_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.update_details_button.setObjectName("update_details_button")
        self.details_line_edit = QtWidgets.QLineEdit(self.manage_register_frame)
        self.details_line_edit.setGeometry(QtCore.QRect(241, 203, 211, 20))
        self.details_line_edit.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.details_line_edit.setObjectName("details_line_edit")
        self.remove_details_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.remove_details_button.setGeometry(QtCore.QRect(337, 231, 45, 23))
        self.remove_details_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.remove_details_button.setObjectName("remove_details_button")
        self.add_details_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.add_details_button.setGeometry(QtCore.QRect(241, 231, 33, 23))
        self.add_details_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.add_details_button.setObjectName("add_details_button")
        self.remove_involved_people_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.remove_involved_people_button.setGeometry(QtCore.QRect(569, 231, 45, 23))
        self.remove_involved_people_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.remove_involved_people_button.setObjectName("remove_involved_people_button")
        self.update_involved_people_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.update_involved_people_button.setGeometry(QtCore.QRect(515, 231, 45, 23))
        self.update_involved_people_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.update_involved_people_button.setObjectName("update_involved_people_button")
        self.add_involved_people_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.add_involved_people_button.setGeometry(QtCore.QRect(473, 231, 33, 23))
        self.add_involved_people_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.add_involved_people_button.setObjectName("add_involved_people_button")
        self.delete_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.delete_button.setGeometry(QtCore.QRect(451, 50, 59, 23))
        self.delete_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.delete_button.setObjectName("delete_button")
        self.new_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.new_button.setGeometry(QtCore.QRect(273, 50, 33, 23))
        self.new_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.new_button.setObjectName("new_button")
        self.update_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.update_button.setGeometry(QtCore.QRect(315, 50, 59, 23))
        self.update_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.update_button.setObjectName("update_button")
        self.unselect_button = QtWidgets.QPushButton(self.manage_register_frame)
        self.unselect_button.setGeometry(QtCore.QRect(383, 50, 59, 23))
        self.unselect_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.unselect_button.setObjectName("unselect_button")
        self.details_list = QtWidgets.QListView(self.manage_register_frame)
        self.details_list.setGeometry(QtCore.QRect(241, 108, 211, 84))
        self.details_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.details_list.setObjectName("details_list")
        self.involved_people_list = QtWidgets.QListView(self.manage_register_frame)
        self.involved_people_list.setGeometry(QtCore.QRect(473, 108, 211, 84))
        self.involved_people_list.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.involved_people_list.setObjectName("involved_people_list")
        self.involved_people_label = QtWidgets.QLabel(self.manage_register_frame)
        self.involved_people_label.setGeometry(QtCore.QRect(543, 90, 81, 16))
        self.involved_people_label.setObjectName("involved_people_label")
        self.activity_line_edit = QtWidgets.QLineEdit(self.manage_register_frame)
        self.activity_line_edit.setGeometry(QtCore.QRect(10, 203, 211, 20))
        self.activity_line_edit.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.activity_line_edit.setObjectName("activity_line_edit")
        self.involved_people_line_edit = QtWidgets.QLineEdit(self.manage_register_frame)
        self.involved_people_line_edit.setGeometry(QtCore.QRect(473, 203, 211, 20))
        self.involved_people_line_edit.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.involved_people_line_edit.setObjectName("involved_people_line_edit")
        self.date_label_2 = QtWidgets.QLabel(self.manage_register_frame)
        self.date_label_2.setGeometry(QtCore.QRect(52, 31, 25, 16))
        self.date_label_2.setObjectName("date_label_2")
        self.tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 1060, 630))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.tabs.addTab(self.tab2, "")
        win0.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(win0)
        self.statusbar.setObjectName("statusbar")
        win0.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(win0)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1529, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        win0.setMenuBar(self.menubar)
        self.new_workspace_menu = QtWidgets.QAction(win0)
        self.new_workspace_menu.setObjectName("new_workspace_menu")
        self.open_workspace_menu = QtWidgets.QAction(win0)
        self.open_workspace_menu.setObjectName("open_workspace_menu")
        self.save_workspace_menu = QtWidgets.QAction(win0)
        self.save_workspace_menu.setObjectName("save_workspace_menu")
        self.saveas_workspace_menu = QtWidgets.QAction(win0)
        self.saveas_workspace_menu.setObjectName("saveas_workspace_menu")
        self.import_menu = QtWidgets.QAction(win0)
        self.import_menu.setObjectName("import_menu")
        self.line_graphic = QtWidgets.QAction(win0)
        self.line_graphic.setObjectName("line_graphic")
        self.menuNew.addAction(self.new_workspace_menu)
        self.menuNew.addAction(self.open_workspace_menu)
        self.menuNew.addAction(self.save_workspace_menu)
        self.menuNew.addAction(self.saveas_workspace_menu)
        self.menuImport.addAction(self.import_menu)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())

        self.retranslateUi(win0)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(win0)

    def retranslateUi(self, win0):
        _translate = QtCore.QCoreApplication.translate
        win0.setWindowTitle(_translate("win0", "Time Visualizer"))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("win0", "Date"))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("win0", "Activity"))
        item = self.table1.horizontalHeaderItem(2)
        item.setText(_translate("win0", "Details"))
        item = self.table1.horizontalHeaderItem(3)
        item.setText(_translate("win0", "Time"))
        item = self.table1.horizontalHeaderItem(4)
        item.setText(_translate("win0", "Involved People"))
        self.from_label.setText(_translate("win0", "From"))
        self.min_label_2.setText(_translate("win0", "Min"))
        self.date_label.setText(_translate("win0", "Date:"))
        self.hours_label_3.setText(_translate("win0", "Hours"))
        self.button_hide_all_acts.setText(_translate("win0", "<-*"))
        self.button_date_to.setText(_translate("win0", "..."))
        self.button_date_from.setText(_translate("win0", "..."))
        self.min_label_3.setText(_translate("win0", "Min"))
        self.time_label.setText(_translate("win0", "Time:"))
        self.button_visible_all_acts.setText(_translate("win0", "*->"))
        self.activity_label.setText(_translate("win0", "Activity:"))
        self.to_label.setText(_translate("win0", "To"))
        self.sec_label_2.setText(_translate("win0", "Sec"))
        self.activities_show_label.setText(_translate("win0", "Visible activities"))
        self.hours_label_2.setText(_translate("win0", "Hours"))
        self.sec_label_3.setText(_translate("win0", "Sec"))
        self.all_activities_label.setText(_translate("win0", "Hidden activities"))
        self.default_button.setText(_translate("win0", "Default"))
        self.configurate_selection_label.setText(_translate("win0", "CONFIGURATE SELECTION"))
        self.button_visible_act.setText(_translate("win0", "->"))
        self.button_hide_act.setText(_translate("win0", "<-"))
        self.people_show_label.setText(_translate("win0", "Visible people"))
        self.all_people_label.setText(_translate("win0", "Hidden people"))
        self.button_hide_people.setText(_translate("win0", "<-"))
        self.button_hide_all_people.setText(_translate("win0", "<-*"))
        self.people_label.setText(_translate("win0", "People:"))
        self.button_visible_people.setText(_translate("win0", "->"))
        self.button_visible_all_people.setText(_translate("win0", "*->"))
        self.from_label_2.setText(_translate("win0", "From"))
        self.to_label_2.setText(_translate("win0", "To"))
        self.sec_label.setText(_translate("win0", "Sec"))
        self.hours_label.setText(_translate("win0", "Hours"))
        self.min_label.setText(_translate("win0", "Min"))
        self.button_date_selected.setText(_translate("win0", "..."))
        self.manage_register_label.setText(_translate("win0", "MANAGE REGISTER"))
        self.activities_label.setText(_translate("win0", "Activities"))
        self.add_activity_button.setText(_translate("win0", "Add"))
        self.update_activity_button.setText(_translate("win0", "Update"))
        self.remove_activity_button.setText(_translate("win0", "Remove"))
        self.details_label.setText(_translate("win0", "Details"))
        self.update_details_button.setText(_translate("win0", "Update"))
        self.remove_details_button.setText(_translate("win0", "Remove"))
        self.add_details_button.setText(_translate("win0", "Add"))
        self.remove_involved_people_button.setText(_translate("win0", "Remove"))
        self.update_involved_people_button.setText(_translate("win0", "Update"))
        self.add_involved_people_button.setText(_translate("win0", "Add"))
        self.delete_button.setText(_translate("win0", "Delete"))
        self.new_button.setText(_translate("win0", "New"))
        self.update_button.setText(_translate("win0", "Update"))
        self.unselect_button.setText(_translate("win0", "Unselect"))
        self.involved_people_label.setText(_translate("win0", "Involved People"))
        self.date_label_2.setText(_translate("win0", "Date"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab1), _translate("win0", "Selected Data"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab2), _translate("win0", "+"))
        self.menuNew.setTitle(_translate("win0", "New"))
        self.menuImport.setTitle(_translate("win0", "Import"))
        self.new_workspace_menu.setText(_translate("win0", "New Workspace"))
        self.open_workspace_menu.setText(_translate("win0", "Open Workspace"))
        self.save_workspace_menu.setText(_translate("win0", "Save Workspace"))
        self.saveas_workspace_menu.setText(_translate("win0", "Save As Workspace"))
        self.import_menu.setText(_translate("win0", "Import From CSV"))
        self.line_graphic.setText(_translate("win0", "Line Graphic"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win0 = QtWidgets.QMainWindow()
    ui = Ui_win0()
    ui.setupUi(win0)
    win0.show()
    sys.exit(app.exec_())

