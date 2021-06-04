"""Use of functional parameters - positional, optional and named arguments

We illustrate the applications of different kinds of parameters using args and kwargs too! Its all done by building special functions and using time it functionality ob them, so get ready to time some stuff! :D """

import time
import math
import types

class Polygon:

    def __init__(self, side_length, number_of_sides = 3):
        self.side_length = side_length
        self.number_of_sides = number_of_sides

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, side_length):
        if not isinstance(side_length,(int, float)):
            raise TypeError("Only integer or float type arguments are allowed")
        elif side_length <= 0:
            raise ValueError("Side of polygon must be greater than zero")
        else:
            self._side_length = side_length

    @property
    def number_of_sides(self):
        return self._number_of_sides

    @number_of_sides.setter
    def number_of_sides(self, number_of_sides):
        if not isinstance(number_of_sides,(int)):
            raise TypeError("Only integer type arguments are allowed")
        elif number_of_sides not in [3, 4, 5, 6]:
            raise ValueError("Polygon only supported for traingle to hexagon (3 to 6 number of sides)")
        else:
            self._number_of_sides = number_of_sides

    def __repr__():
        return f"Polygon(length={self.side_length}, number_of_sides = {self.number_of_sides})"

    def __str__():
        return f"Polygon of side {self.side_length} and {self.number_of_sides} sides"

    def area(self):
        # divide into traingles and then calculate area of one traingle
        included_angle = 2 * math.pi / self.number_of_sides
        altitude = (self.side_length/2) / math.tan(included_angle / 2)
        traingle_area = 0.5 * self.side_length * altitude
        return self.number_of_sides * traingle_area

class Temperature:

    def __init__(self, temperature, unit = 'c'):
        self.temperature = temperature
        self.unit = unit
        if self.unit == 'c' and self.temperature < -273.15:
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
        if self.unit == 'f' and self.temperature < -459.67:
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if not (isinstance(temperature, int) or isinstance(temperature, float)):
            raise TypeError("Invalid type of input temperature : Only integer or float type arguments are allowed")
        else:
            self._temperature = temperature

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit):
        if not isinstance(unit, str):
            raise TypeError("Charcater string expected")
        elif unit.lower() not in ['c', 'f']:
            raise ValueError("Invalid unit of temperature. Only f or c is allowed")
        else:
            self._unit = unit.lower()

    def __repr__():
        return f"Temperature(value={self.temperature}, unit = {self.unit})"

    def __str__():
        return f"Temperature {self.temperature} in degrees {self.unit}"

    def convert(self):
        if self.unit == 'c':
            return 9/5 * self.temperature + 32
        elif self.unit == 'f':
            return 5/9 * (self.temperature - 32)

class Speed:

    def __init__(self, speed):
        self.speed = speed
        self.dist_conversion_factors = {'km' : 1, 'm' : 1000, 'ft' : 3280.8375, 'yrd' : 1093.609}
        self.time_conversion_factors = {'day' : 1/24, 'hr' : 1, 'min' : 60, 's' : 60*60, 'ms' : 60*60*1000 }

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, (int, float)):
            raise TypeError("Speed can be int or float type only")
        if speed < 0:
            raise ValueError("Speed can't be negative")
        elif speed > 300000:
            raise ValueError("Speed can't be greater than speed of light")
        else:
            self._speed = speed

    def __repr__():
        return f"Speed(value = {self.speed})"

    def __str__():
        return f"Speed of {self.speed} kmph"

    def convert(self, distance_unit = 'm', time_unit = 's'):
        distance_unit = distance_unit.lower()
        time_unit = time_unit.lower()

        # validations on unit types
        if distance_unit not in ['km', 'm', 'ft', 'yrd']:
            raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
        if time_unit not in ['day', 'hr', 'min', 's', 'ms']:
            raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")

        return round(self.speed * self.dist_conversion_factors[distance_unit]/self.time_conversion_factors[time_unit])

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    if not callable(fn):
        raise ValueError("Callable funtion needs to be sent as first positional argument")
    # Repetition should be positive number
    if repetitions < 0:
        raise ValueError("Repetitions needs to be greater than zero")
    if not isinstance(repetitions, int):
        raise TypeError("Repetitions must be an integer value")

    if repetitions == 0:
        return 0
    sum_time = 0
    count = 0
    for i in range(repetitions):
        start = time.perf_counter()
        fn(*args, **kwargs)
        end = time.perf_counter()
        sum_time += (end - start)
        count += 1 
    return sum_time/count


def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if args:
        raise TypeError("Function takes maximum 1 positional arguments")
    if kwargs:
        raise TypeError("Function takes maximum 2 keyword/named arguments")
    if not (isinstance(number, int) or isinstance(number, float)):
        raise TypeError("Only integer type arguments are allowed")
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")
    if end - start < 0:
        raise ValueError("Value of start should be less than end")
    if number > 10:
        raise ValueError("Value of number should be less than 10")  

    # Return the list of number to the power of numbers from start to end
    return [number**i for i in range(start, end)]

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Other validations are internal to the class
    if args:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")

    p = Polygon(length, sides)
    return p.area()

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Other validations are internal to the class
    if args:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    t = Temperature(temp, unit = temp_given_in)
    return t.convert()

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Other validations are internal to the class
    if not isinstance(dist, str):
            raise TypeError("Charcater string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError("Charcater string expected")
    if args:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

    s = Speed(speed)
    return s.convert(dist, time)
