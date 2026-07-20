from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(660, 110, 31, 461))
        self.verticalSlider.setMinimum(-50)
        self.verticalSlider.setMaximum(50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(780, 110, 31, 461))
        self.verticalSlider_2.setMinimum(1)
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(915, 110, 31, 461))
        self.verticalSlider_3.setMinimum(100)
        self.verticalSlider_3.setMaximum(150)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setGeometry(QtCore.QRect(1050, 110, 31, 461))
        self.verticalSlider_4.setMinimum(6)
        self.verticalSlider_4.setMaximum(12)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.plot_widget = pg.PlotWidget(self.centralwidget)
        self.plot_widget.setGeometry(QtCore.QRect(20, 50, 601, 521))
        self.plot_widget.setObjectName("plot_widget")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(630, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1000, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        # Добавляем QLineEdit под слайдеры
        self.lineEdit_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_temp.setGeometry(QtCore.QRect(650, 580, 51, 25))
        self.lineEdit_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_temp.setObjectName("lineEdit_temp")

        self.lineEdit_population = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_population.setGeometry(QtCore.QRect(770, 580, 51, 25))
        self.lineEdit_population.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_population.setObjectName("lineEdit_population")

        self.lineEdit_power = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_power.setGeometry(QtCore.QRect(905, 580, 51, 25))
        self.lineEdit_power.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_power.setObjectName("lineEdit_power")

        self.lineEdit_night = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_night.setGeometry(QtCore.QRect(1040, 580, 51, 25))
        self.lineEdit_night.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_night.setObjectName("lineEdit_night")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1175, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фотон"))
        self.temp.setText(_translate("MainWindow", "Температура  "))
        self.label.setText(_translate("MainWindow", "ФОТОН"))
        self.label_2.setText(_translate("MainWindow", "Население, тыс. чел."))
        self.label_3.setText(_translate("MainWindow", "Мощность ТЭС, кВт  "))
        self.label_4.setText(_translate("MainWindow", "Продолжительность ночи, ч."))


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color: grey;")

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
        """Обновление значений в QLineEdit из слайдеров"""
        self.lineEdit_temp.setText(str(self.verticalSlider.value()))
        self.lineEdit_population.setText(str(self.verticalSlider_2.value()))
        self.lineEdit_power.setText(str(self.verticalSlider_3.value()))
        self.lineEdit_night.setText(str(self.verticalSlider_4.value()))

    def on_slider_changed(self, value):
        """Обработчик изменения положения слайдера"""
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
        Демонстрационная функция с СИЛЬНОЙ зависимостью от параметров
        """
        # Получение текущих значений со слайдеров
        temperature = self.verticalSlider.value()
        population = self.verticalSlider_2.value()
        power = self.verticalSlider_3.value()
        night_duration = self.verticalSlider_4.value()
        radiator_cons = 0

        # ДЕМОНСТРАЦИОННАЯ ФОРМУЛА С СИЛЬНЫМИ ИЗМЕНЕНИЯМИ:

        # 1. Сильное влияние населения (квадратичная зависимость)
        population_effect = population * 1000 * 0.1042

        # 2. Сильное влияние температуры (экспоненциальный рост при понижении)
        temp_effect = 2.5 ** (-temperature / 25)

        # 3. Влияние мощности ТЭС (прямая сильная зависимость)
        power_effect = (power / 100) ** 2

        # 4. Влияние продолжительности ночи (сильная нелинейная зависимость)
        night_effect = (night_duration / 6) ** 3

        # 5. Базовое потребление с учетом всех факторов
        base_load = population_effect * temp_effect * power_effect * night_effect * 2

        if -25 < temperature < 10:
            radiator_cons = 0.35 * 0.25 * population * 1000
        elif temperature <= -25:
            radiator_cons = 0.35 * population * 1000

        # 6. Сильные пики потребления в зависимости от времени суток
        morning_peak_amplitude = 15 * population_effect * (2 - temperature / 50)
        morning_peak = morning_peak_amplitude * np.exp(-((time - 7.5) / 1.5) ** 2)

        day_peak_amplitude = 20 * power_effect
        day_peak = day_peak_amplitude * np.exp(-((time - 13) / 1.2) ** 2)

        evening_peak_amplitude = 25 * population_effect * night_effect
        evening_peak = evening_peak_amplitude * np.exp(-((time - 19.5) / 2) ** 2)

        night_minimum = -8 * night_effect * np.exp(-((time - 2) / 4) ** 2)

        daily_wave = (5 + temperature / 10) * np.sin(np.pi * time / 12 - np.pi / 2) * population_effect / 2

        consumption = base_load + morning_peak + day_peak + evening_peak + night_minimum + daily_wave + radiator_cons
        consumption = np.maximum(consumption, 0)

        return consumption

    def update_plot(self):
        """Обновление графика"""
        time = np.linspace(0, 24, 241)
        consumption = self.calculate_consumption(time)
        self.curve.setData(time, consumption)
        self.plot_widget.setYRange(0, max(consumption) * 1.1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())