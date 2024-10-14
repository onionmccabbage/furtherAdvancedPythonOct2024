from abc import ABCMeta, abstractmethod

class Meteorology(metaclass=ABCMeta):
    __slots__ = ('__city', '__description', '__temperature', '__wind')
    def __init__(self, city, description, temperature, wind):
        ''''''
    
class Weather(Meteorology):
    __slots__ = ('__city', '__description', '__temperature', '__wind')
    def __init__(self, city, description, temperature, wind):
        self.city = city
        self.description = description
        self.temperature = temperature
        self.wind = wind
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        if type(city)==str and city !='':
            self.__city = city
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        if type(description)==str and description !='':
            self.__description = description
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, temperature):
        if type(temperature) in (int, float):
            self.__temperature = temperature
    @property
    def wind(self):
        return self.__wind
    @wind.setter
    def wind(self, wind):
        if type(wind) == tuple: # should we also allow a list
            if type(wind[0]) in (int, float):
                wind_speed = wind[0]
            if type(wind[1]) in (int, float):
                wind_direction = wind[1]
            self.__wind = (wind_speed, wind_direction)
    def __str__(self):
        return f'In {self.city} the weather is {self.description} at {self.temperature} wind is {self.wind[0]}C at {self.wind[1]}'
    def __repr__(self):
        return f'In {self.city} the weather is {self.description} at {self.temperature} wind is {self.wind[0]}C at {self.wind[1]}'

if __name__ == '__main__':
    w = Weather('Athlone', 'sunny', 13.5, (3.2, 250))
    print(w)