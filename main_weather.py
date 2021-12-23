from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtCore import QThread, QTimer
import weather
import time
import datetime
from weather import DAYS


class WeatherData(QThread):
    req = weather.today()
    temp = req['temp']
    feels = req['feels']
    pressure = req['pressure']
    speed = str(req['wind']['speed'])
    city = req['city']
    description = req['description']

    week = weather.week()

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try:
                req = weather.today()
            except:
                req['temp'] = self.temp
                req['feels'] = self.feels
                req['pressure'] = self.pressure
                req['wind']['speed'] = self.speed
                req['city'] = self.city
                req['description'] = self.description

            try:
                req_week = weather.week()
                self.week = req_week
            except:
                self.week = DAYS

            self.temp = req['temp']
            self.feels = req['feels']
            self.pressure = req['pressure']
            self.speed = req['wind']['speed']
            self.city = req['city']
            self.description = req['description']
            time.sleep(60)


class Ui_Form(object):
    show_more = True
    tick = True
    Window_show = [
        180, 181, 183, 185, 188,
        201, 222, 256, 311, 400,
        500, 510, 505, 500, 490,
        480
    ]
    Window_hide = [
        180, 249, 338, 393, 427,
        448, 461, 469, 474, 477,
        479, 480
    ]
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 180)
        Form.setMinimumSize(QtCore.QSize(300, 180))
        Form.setMaximumSize(QtCore.QSize(300, 480))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        Form.setFont(font)
        self.label_temp = QtWidgets.QLabel(Form)
        self.label_temp.setGeometry(QtCore.QRect(0, 30, 300, 50))
        self.label_temp.setMinimumSize(QtCore.QSize(300, 50))
        self.label_temp.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(50)
        self.label_temp.setFont(font)
        self.label_temp.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.label_city = QtWidgets.QLabel(Form)
        self.label_city.setGeometry(QtCore.QRect(2, 2, 295, 25))
        self.label_city.setMinimumSize(QtCore.QSize(295, 25))
        self.label_city.setMaximumSize(QtCore.QSize(295, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_city.setFont(font)
        self.label_city.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label_city.setAlignment(QtCore.Qt.AlignCenter)
        self.label_city.setObjectName("label_city")
        self.label_typeWeather = QtWidgets.QLabel(Form)
        self.label_typeWeather.setGeometry(QtCore.QRect(0, 80, 300, 30))
        self.label_typeWeather.setMinimumSize(QtCore.QSize(300, 30))
        self.label_typeWeather.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_typeWeather.setFont(font)
        self.label_typeWeather.setStyleSheet("color: rgba(255, 255, 255, 180);")
        self.label_typeWeather.setAlignment(QtCore.Qt.AlignCenter)
        self.label_typeWeather.setObjectName("label_typeWeather")
        self.label_howFeel = QtWidgets.QLabel(Form)
        self.label_howFeel.setGeometry(QtCore.QRect(11, 113, 90, 14))
        self.label_howFeel.setMinimumSize(QtCore.QSize(90, 14))
        self.label_howFeel.setMaximumSize(QtCore.QSize(90, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_howFeel.setFont(font)
        self.label_howFeel.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_howFeel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_howFeel.setObjectName("label_howFeel")
        self.label_pressure = QtWidgets.QLabel(Form)
        self.label_pressure.setGeometry(QtCore.QRect(101, 113, 100, 14))
        self.label_pressure.setMinimumSize(QtCore.QSize(100, 14))
        self.label_pressure.setMaximumSize(QtCore.QSize(100, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_pressure.setFont(font)
        self.label_pressure.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pressure.setObjectName("label_pressure")
        self.label_speedWind = QtWidgets.QLabel(Form)
        self.label_speedWind.setGeometry(QtCore.QRect(201, 113, 90, 14))
        self.label_speedWind.setMinimumSize(QtCore.QSize(90, 14))
        self.label_speedWind.setMaximumSize(QtCore.QSize(90, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_speedWind.setFont(font)
        self.label_speedWind.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_speedWind.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speedWind.setObjectName("label_speedWind")
        self.label_howFeel_2 = QtWidgets.QLabel(Form)
        self.label_howFeel_2.setGeometry(QtCore.QRect(11, 129, 90, 14))
        self.label_howFeel_2.setMinimumSize(QtCore.QSize(90, 14))
        self.label_howFeel_2.setMaximumSize(QtCore.QSize(90, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_howFeel_2.setFont(font)
        self.label_howFeel_2.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_howFeel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_howFeel_2.setObjectName("label_howFeel_2")
        self.label_pressure_2 = QtWidgets.QLabel(Form)
        self.label_pressure_2.setGeometry(QtCore.QRect(101, 129, 100, 14))
        self.label_pressure_2.setMinimumSize(QtCore.QSize(100, 14))
        self.label_pressure_2.setMaximumSize(QtCore.QSize(100, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_pressure_2.setFont(font)
        self.label_pressure_2.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_pressure_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pressure_2.setObjectName("label_pressure_2")
        self.label_speedWind2 = QtWidgets.QLabel(Form)
        self.label_speedWind2.setGeometry(QtCore.QRect(201, 129, 90, 14))
        self.label_speedWind2.setMinimumSize(QtCore.QSize(90, 14))
        self.label_speedWind2.setMaximumSize(QtCore.QSize(90, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_speedWind2.setFont(font)
        self.label_speedWind2.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_speedWind2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speedWind2.setObjectName("label_speedWind2")
        self.btn_showMore = QtWidgets.QPushButton(Form)
        self.btn_showMore.setGeometry(QtCore.QRect(0, 152, 300, 28))
        self.btn_showMore.setMinimumSize(QtCore.QSize(300, 28))
        self.btn_showMore.setMaximumSize(QtCore.QSize(300, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_showMore.setFont(font)
        self.btn_showMore.setStyleSheet("background-color: rgba(0, 0, 0, 16);\n"
        "color: rgba(0, 0, 0, 150);")
        self.btn_showMore.setObjectName("btn_showMore")
        self.label_day = QtWidgets.QLabel(Form)
        self.label_day.setGeometry(QtCore.QRect(10, 156, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_day.setFont(font)
        self.label_day.setAlignment(QtCore.Qt.AlignCenter)
        self.label_day.setObjectName("label_day")
        self.label_timeNow = QtWidgets.QLabel(Form)
        self.label_timeNow.setGeometry(QtCore.QRect(190, 156, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_timeNow.setFont(font)
        self.label_timeNow.setStyleSheet("background-color: rgb(26, 26, 26);\n"
        "border: 1px inset gray;\n"
        "color: rgb(54, 255, 114);")
        self.label_timeNow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timeNow.setObjectName("label_timeNow")
        self.frame_cold = QtWidgets.QFrame(Form)
        self.frame_cold.setGeometry(QtCore.QRect(0, 0, 300, 480))
        self.frame_cold.setMinimumSize(QtCore.QSize(300, 480))
        self.frame_cold.setMaximumSize(QtCore.QSize(300, 480))
        self.frame_cold.setStyleSheet("background-color: rgb(51, 153, 255);")
        self.frame_cold.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cold.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cold.setObjectName("frame_cold")
        self.frame_hot = QtWidgets.QFrame(Form)
        self.frame_hot.setGeometry(QtCore.QRect(0, 0, 300, 480))
        self.frame_hot.setMinimumSize(QtCore.QSize(300, 480))
        self.frame_hot.setMaximumSize(QtCore.QSize(300, 480))
        self.frame_hot.setBaseSize(QtCore.QSize(0, 0))
        self.frame_hot.setStyleSheet("background-color: rgb(255, 102, 51);")
        self.frame_hot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_hot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_hot.setObjectName("frame_hot")
        self.frame_showMore = QtWidgets.QFrame(Form)
        self.frame_showMore.setGeometry(QtCore.QRect(0, 180, 300, 300))
        self.frame_showMore.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_showMore.setMaximumSize(QtCore.QSize(300, 300))
        self.frame_showMore.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frame_showMore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_showMore.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showMore.setObjectName("frame_showMore")
        self.frame_more = QtWidgets.QFrame(Form)
        self.frame_more.setGeometry(QtCore.QRect(0, 180, 300, 300))
        self.frame_more.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_more.setMaximumSize(QtCore.QSize(300, 300))
        self.frame_more.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_more.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_more.setObjectName("frame_more")
        self.box = QtWidgets.QFormLayout(self.frame_more)
        self.box.setContentsMargins(6, 6, 8, 8)
        self.box.setSpacing(3)
        self.box.setObjectName("box")
        self.frame_hot.raise_()
        self.frame_cold.raise_()
        self.label_temp.raise_()
        self.label_city.raise_()
        self.label_typeWeather.raise_()
        self.label_howFeel.raise_()
        self.label_pressure.raise_()
        self.label_speedWind.raise_()
        self.label_howFeel_2.raise_()
        self.label_pressure_2.raise_()
        self.label_speedWind2.raise_()
        self.btn_showMore.raise_()
        self.label_day.raise_()
        self.label_timeNow.raise_()
        self.frame_showMore.raise_()
        self.frame_more.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.weather = WeatherData()
        self.weather.start()

        self.setData()
        self.setDay()
        self.setTime()

        self.timer = QTimer()
        self.timer.timeout.connect(self.setTime)
        self.timer.start(1000)

        self.btn_showMore.clicked.connect(self.showMoreWindow)

        self.setMore()

        self.setBackground()


    def setData(self):
        # Установка значений
        self.label_temp.setText(str(self.weather.temp) + '°C')
        self.label_howFeel.setText(self.weather.feels)
        self.label_pressure.setText(self.weather.pressure)
        self.label_speedWind.setText(self.weather.speed + ' м/с')
        self.label_city.setText(self.weather.city)
        self.label_typeWeather.setText(self.weather.description)
        self.btn_showMore.setText('🡻')

    def setDay(self):
        # Установка дня
        today = DAYS[datetime.datetime.today().weekday()]
        self.label_day.setText(today['title'])
        color = today['color']
        self.label_day.setStyleSheet(f'color:{color}')

    def setTime(self):
        # Установка времени
        if self.tick:
            nowTime = datetime.datetime.today().strftime('%H:%M:%S')
            self.tick = False
        else:
            nowTime = datetime.datetime.today().strftime('%H %M %S')
            self.tick = True
        self.label_timeNow.setText(nowTime)

    def showMoreWindow(self):
        if self.show_more:
            Form.resize(300, 180)
            self.btn_showMore.setText('🡻')
            self.show_more = False
        else:
            Form.resize(300, 480)
            self.btn_showMore.setText('🢁')
            self.show_more = True

    def setMore(self):
        for el in self.weather.week:
            w_day = uic.loadUi('form_day.ui')
            w_day.label_title.setText(el['title'])
            w_day.label_temp.setText(str(round(el['temp'])) + '°C')
            w_day.label_description.setText(el['type'])
            w_day.label_title.setStyleSheet("color: " + el['color'] + "; background-color: none; border: none;")
            w_day.label_temp.setStyleSheet("color:  rgba(255, 255, 255, 180); background-color: none; border: none;")
            w_day.label_description.setStyleSheet("color: rgb(255, 231, 57); background-color: none; border: none;")
            w_day.setStyleSheet("background-color: rgba(255, 255, 255, 25); border: none;")
            if el['active']:
                w_day.setStyleSheet("border: 1px solid; border-color:" + el['color'])
            self.box.addWidget(w_day)

    def setBackground(self):
        background_color_saturation = {
            15: 10,    14: 20,    13:   30,    12: 40,    11:   50,
            10: 60,    9: 20,     8:    80,    7: 90,     6:   100,
            5: 110,    4: 20,     3:    130,   2: 140,    1:   150,
            0: 160,    -1: 170,   -2:   180,   -3: 190,   -4:   200,
            -5: 210,   -6: 220,   -7:   230,   -8: 240,   -9:   250
        }
        if self.weather.temp > 15:
            self.background_color_saturation = 0
        elif self.weather.temp <= -10:
            self.background_color_saturation = 255
        else:
            self.background_color_saturation = background_color_saturation[self.weather.temp]

        self.frame_cold.setStyleSheet(f'background-color: rgba(54, 164, 255, {self.background_color_saturation})')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Погода"))
        self.label_temp.setText(_translate("Form", "+10 C"))
        self.label_city.setText(_translate("Form", "Город"))
        self.label_typeWeather.setText(_translate("Form", "Состояние"))
        self.label_howFeel.setText(_translate("Form", "0 C"))
        self.label_pressure.setText(_translate("Form", "750"))
        self.label_speedWind.setText(_translate("Form", "3 м/с"))
        self.label_howFeel_2.setText(_translate("Form", "ощущается"))
        self.label_pressure_2.setText(_translate("Form", "давление мм.р.ст"))
        self.label_speedWind2.setText(_translate("Form", "скорость ветра"))
        self.btn_showMore.setText(_translate("Form", "------"))
        self.label_day.setText(_translate("Form", "Воскресенье"))
        self.label_timeNow.setText(_translate("Form", "12:12:12"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
