from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
from photon_db import Table, session
from sqlalchemy import desc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(45, 630, 30, 200))
        self.verticalSlider.setMinimum(-50)
        self.verticalSlider.setMaximum(50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(200, 630, 30, 200))
        self.verticalSlider_2.setMinimum(1)
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")

        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(365, 630, 30, 200))
        self.verticalSlider_3.setMinimum(100)
        self.verticalSlider_3.setMaximum(150)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")

        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setGeometry(QtCore.QRect(525, 630, 30, 200))
        self.verticalSlider_4.setMinimum(6)
        self.verticalSlider_4.setMaximum(12)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")

        self.plot_widget = pg.PlotWidget(self.centralwidget)
        self.plot_widget.setGeometry(QtCore.QRect(20, 50, 601, 521))
        self.plot_widget.setObjectName("plot_widget")

        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(20, 590, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 590, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 590, 97, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 590, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")


        # Добавляем QLineEdit под слайдеры
        self.lineEdit_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_temp.setGeometry(QtCore.QRect(35, 840, 51, 25))
        self.lineEdit_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_temp.setObjectName("lineEdit_temp")

        self.lineEdit_population = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_population.setGeometry(QtCore.QRect(189, 840, 51, 25))
        self.lineEdit_population.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_population.setObjectName("lineEdit_population")

        self.lineEdit_power = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_power.setGeometry(QtCore.QRect(353, 840, 51, 25))
        self.lineEdit_power.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_power.setObjectName("lineEdit_power")

        self.lineEdit_night = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_night.setGeometry(QtCore.QRect(514, 840, 51, 25))
        self.lineEdit_night.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_night.setObjectName("lineEdit_night")

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)

        self.save_action = QtWidgets.QAction(MainWindow)
        self.save_action.setObjectName("save_action")
        self.load_action  =QtWidgets.QAction(MainWindow)
        self.save_action.setObjectName("load_action")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотон"))
        self.temp.setText(_translate("MainWindow", "Температура  "))
        self.label.setText(_translate("MainWindow", "ФОТОН"))
        self.label_2.setText(_translate("MainWindow", "Население, тыс. чел."))
        self.label_3.setText(_translate("MainWindow", "Мощность ТЭС,\n кВт"))
        self.label_4.setText(_translate("MainWindow", "Продолжительность ночи,\n ч."))
        self.save_action.setText(_translate("MainWindow", "Сохранить результат"))
        self.load_action.setText(_translate("MainWindow", "Лучший результат"))


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color: grey;")
        self.cons = 0

        self.save_action.triggered.connect(self.save_results)
        self.load_action.triggered.connect(self.load_result)

        self.toolBar.addAction(self.save_action)
        self.toolBar.addAction(self.load_action)

        # Установка начальных значений слайдеров для наглядности
        self.verticalSlider.setValue(0)  # Температура
        self.verticalSlider_2.setValue(50)  # Население
        self.verticalSlider_3.setValue(125)  # Мощность ТЭС
        self.verticalSlider_4.setValue(9)  # Продолжительность ночи

        # Инициализация полей ввода начальными значениями
        self.update_line_edits()

        # Инициализация графика
        self.init_plot()

        # Подключение слайдеров к функции обновления
        self.verticalSlider.valueChanged.connect(self.on_slider_changed)
        self.verticalSlider_2.valueChanged.connect(self.on_slider_changed)
        self.verticalSlider_3.valueChanged.connect(self.on_slider_changed)
        self.verticalSlider_4.valueChanged.connect(self.on_slider_changed)

        # Подключение полей ввода к функции обработки
        self.lineEdit_temp.returnPressed.connect(self.on_lineedit_changed)
        self.lineEdit_population.returnPressed.connect(self.on_lineedit_changed)
        self.lineEdit_power.returnPressed.connect(self.on_lineedit_changed)
        self.lineEdit_night.returnPressed.connect(self.on_lineedit_changed)


        # Первоначальное построение графика
        self.update_plot()

    def save_results(self):
        result = Table(temperature=self.verticalSlider.value(),
                       population=self.verticalSlider_2.value(),
                       power=self.verticalSlider_3.value(),
                       night_duration=self.verticalSlider_4.value(),
                       consumption=round(np.mean(self.cons)))
        session.add(result)
        session.commit()


    def load_result(self):
        record = session.query(Table).order_by(Table.consumption).first()
        self.verticalSlider.setValue(record.temperature)
        self.verticalSlider_2.setValue(record.population)
        self.verticalSlider_3.setValue(record.power)
        self.verticalSlider_4.setValue(record.night_duration)
        self.update_line_edits()

    def init_plot(self):
        """Инициализация графика с отключением взаимодействия"""
        # Настройка отображения графика
        self.plot_widget.setLabel('left', 'Потребление', units='кВт·ч')
        self.plot_widget.setLabel('bottom', 'Время', units='часы')
        self.plot_widget.setTitle('График потребления электроэнергии')
        self.plot_widget.showGrid(x=True, y=True)

        # Отключение взаимодействия с мышью
        self.plot_widget.setMouseEnabled(x=False, y=False)
        self.plot_widget.setMenuEnabled(False)
        self.plot_widget.setLimits(xMin=0, xMax=24)
        self.plot_widget.setLimits(yMin=0)

        # Настройка делений оси X по 1 часу
        x_axis = self.plot_widget.getAxis('bottom')
        x_axis.setTickSpacing(major=1, minor=0.5)

        # Отключаем колесико мыши для масштабирования
        self.plot_widget.wheelEvent = lambda event: None

        # Создание кривой для графика
        self.curve = self.plot_widget.plot(pen=pg.mkPen(color='y', width=2))

    def update_line_edits(self):
        self.lineEdit_temp.setText(str(self.verticalSlider.value()))
        self.lineEdit_population.setText(str(self.verticalSlider_2.value()))
        self.lineEdit_power.setText(str(self.verticalSlider_3.value()))
        self.lineEdit_night.setText(str(self.verticalSlider_4.value()))

    def on_slider_changed(self, value):
        # Определяем, какой слайдер вызвал событие
        sender = self.sender()

        if sender == self.verticalSlider:
            self.lineEdit_temp.setText(str(value))
        elif sender == self.verticalSlider_2:
            self.lineEdit_population.setText(str(value))
        elif sender == self.verticalSlider_3:
            self.lineEdit_power.setText(str(value))
        elif sender == self.verticalSlider_4:
            self.lineEdit_night.setText(str(value))

        # Обновляем график
        self.update_plot()

    def on_lineedit_changed(self):
        """Обработчик нажатия Enter в QLineEdit"""
        sender = self.sender()

        try:
            if sender == self.lineEdit_temp:
                value = int(sender.text())
                # Проверяем границы
                if value < self.verticalSlider.minimum():
                    value = self.verticalSlider.minimum()
                elif value > self.verticalSlider.maximum():
                    value = self.verticalSlider.maximum()

                # Обновляем слайдер и поле ввода
                self.verticalSlider.setValue(value)
                self.lineEdit_temp.setText(str(value))

            elif sender == self.lineEdit_population:
                value = int(sender.text())
                if value < self.verticalSlider_2.minimum():
                    value = self.verticalSlider_2.minimum()
                elif value > self.verticalSlider_2.maximum():
                    value = self.verticalSlider_2.maximum()

                self.verticalSlider_2.setValue(value)
                self.lineEdit_population.setText(str(value))

            elif sender == self.lineEdit_power:
                value = int(sender.text())
                if value < self.verticalSlider_3.minimum():
                    value = self.verticalSlider_3.minimum()
                elif value > self.verticalSlider_3.maximum():
                    value = self.verticalSlider_3.maximum()

                self.verticalSlider_3.setValue(value)
                self.lineEdit_power.setText(str(value))

            elif sender == self.lineEdit_night:
                value = int(sender.text())
                if value < self.verticalSlider_4.minimum():
                    value = self.verticalSlider_4.minimum()
                elif value > self.verticalSlider_4.maximum():
                    value = self.verticalSlider_4.maximum()

                self.verticalSlider_4.setValue(value)
                self.lineEdit_night.setText(str(value))

        except ValueError:
            # Если введено не число - восстанавливаем текущее значение слайдера
            self.update_line_edits()

        # Обновляем график
        self.update_plot()

    def calculate_consumption(self, time):
        """
           Расчёт потребления электроэнергии по уточнённой модели.
           Параметры (из слайдеров):
             temperature    – температура воздуха, °C       (-50…+50)
             population    – население, тыс. чел.           (1…100)
             night_duration – продолжительность ночи, час   (6…12)
           Возвращает массив мгновенной мощности (кВт) для каждого момента времени.
           """
        # Текущие значения
        temp = self.verticalSlider.value()
        pop = self.verticalSlider_2.value()  # тыс. чел.
        night = self.verticalSlider_4.value()  # часов

        # Переводим население в число жителей
        people = pop * 1000.0

        # ---------- 1. Климатическая добавка (отопление + охлаждение), кВт/чел ----------
        # Радиаторы: включаются при ≤ +10°C, полная мощность (0.35 кВт) при ≤ -25°C
        # Кондиционеры: включаются при ≥ +10°C, полная мощность (0.35 кВт) при ≥ +50°C
        if temp <= -25:
            climate_per_capita = 0.350
        elif -25 < temp <= 10:
            # Линейный рост с 1/4 мощности при +10°C до полной при -25°C
            fraction = 0.25 + 0.75 * (10 - temp) / 35.0
            climate_per_capita = 0.350 * fraction
        elif 10 < temp <= 50:
            # Линейный рост от 0 до полной мощности при +50°C
            fraction = (temp - 10) / 40.0  # 0 при +10, 1 при +50
            climate_per_capita = 0.350 * fraction
        else:  # temp > 50 (теоретически, слайдер ограничен 50)
            climate_per_capita = 0.350

        # ---------- 2. Базовый суточный профиль (без климатической добавки) ----------
        sigma_peak = 1.5
        sigma_night = night / 4.0
        A_peak = 3.0
        A_night = 0.5

        morning_peak_time = night / 2.0 + 2.0
        evening_peak_time = 24.0 - night / 2.0 - 2.0

        gauss_morning = np.exp(-((time - morning_peak_time) ** 2) / (2 * sigma_peak ** 2))
        gauss_evening = np.exp(-((time - evening_peak_time) ** 2) / (2 * sigma_peak ** 2))
        dist_to_midnight = np.minimum(np.abs(time - 0), np.abs(time - 24))
        gauss_night = np.exp(-(dist_to_midnight ** 2) / (2 * sigma_night ** 2))

        raw_profile = (1.0
                       + A_peak * (gauss_morning + gauss_evening)
                       - A_night * gauss_night)
        raw_mean = np.mean(raw_profile)
        target_mean = 2.5 / 24.0  # 2.5 кВт*ч/сут на человека → средняя мощность
        base_per_capita = (target_mean / raw_mean) * raw_profile

        # ---------- 3. Суммарная мощность (кВт) ----------
        total_power = people * (base_per_capita + climate_per_capita)
        total_power = np.maximum(total_power, 0)

        return total_power

    def update_plot(self):
        time = np.linspace(0, 24, 241)
        self.cons = self.calculate_consumption(time)
        self.curve.setData(time, self.cons)
        self.plot_widget.setYRange(0, max(self.cons) * 1.1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())