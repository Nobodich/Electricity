from sqlalchemy import create_engine, Integer, Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

link = create_engine("postgresql+psycopg2://postgres:(M1quella)@localhost/photon_score")
x = declarative_base()


class Table(x):
    __tablename__ = "photon_results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Integer, default=0)
    population = Column(Integer, default=50)
    power = Column(Integer, default=125)
    night_duration = Column(Integer, default=9)
    consumption = Column(Integer, default=0)


x.metadata.create_all(link)
s = sessionmaker(link)
session = s()

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
        """