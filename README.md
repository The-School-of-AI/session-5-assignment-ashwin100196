# Let's Time it with special functions

This module contains an implementation of timeit to provide the average time taken for a function execution. It also comes with function implementations of Temperature, Speed and Geometrical Polygons too! 

## Function argument concepts

As can be seen in the implementations of the following functions, the core concept displayed here is the differences in positional arguments and keyword arguments. The takeaways can be summarized as mentioned below:

- Positional arguments are passed as ```func(a, b, c)```
- When default values are passed to them, these arguments become optional arguments ```func(a, b = 10, c = 20)```
- including \*args exhausts all positional arguments.  

  ```python
  def func(*args, **kwargs):
    pass
  func(1,2,3)
  ```  
  The above would put (1,2,3) into args
 - arguments are called named arguments when the name is specified. ```func(1, 10, c = 3)``` makes c a named argument
 - Keyword arguments are all argumetns that follow the positional arguments and are always named. This is marked by the \*args or simply \* parameter as shown below
  
    ```def func(a, b *, c = 3, d = 5):```
 
    or
    
    ```def func(a, b *args, c = 3, d = 5):```
      
    In the above example, c and d are named keyword arguments

All these concepts are used in this implementation and the resulting Classes and Functions can be found below

### Classes

1. __Polygon__ - Represents a regular polygon of a given length and number of sides

    > Attributes </br>
    > side_length - length of each side of the regular polygon.</br>
    > number_of_sides - decides what type of regular polygon. possible options range from Triangle to Hexagon. Default: 3</br>

    > Methods</br>
    > __init__ : initializes the Polygon object</br>
    > __repr__ : Provides the details of the Polygon object</br>
    > __area__ : returns the area of the regular polygon</br>

2. __Temperature__ - Represents a temperature value in either degree Celsius or Farenheit

    > Attributes</br>
    > temperature - the value of temperature</br>
    > unit - The unit of the temperature, default = 'c'</br>

    > Methods</br>
    > __init__ : initializes the Temperature object</br>
    > __repr__ : Provides the details of the Temperature object</br>
    > __convert__ : returns the converted temperature (celsius if in farenheit and vice versa)</br>

2. __Speed__ - Represents the speed in kmph

    > Attributes</br>
    > speed - the value of speed, always in kmph</br>

    > Methods</br>
    > __init__ : initializes the Speed object</br>
    > __repr__ : Provides the details of the Speed object</br>
    > __convert__ : returns the converted speed by taking the distance and time units to which it needs to be converted to</br>

### Functions

With the help of the above classes, the functions have been implemented

1. **polygon_area** - Calculates the area of a regular polygon

    > Arguments</br>
    > side_length - length of each side</br>
    > sides - the number of sides</br>
    
    > Returns</br>
    > area - this is the area of the regular polygon</br>
    
    > Usage</br>
    > polygon_area(10, sides = 6)</br>

2. **temp_converter** - Converts temperature from Celsius to Farenheit and vice versa

    > Arguments</br>
    > temperature - value of temperature</br>
    > temp_given_in - the scale in which temperature has been recorded</br>
    
    > Returns</br>
    > converted_temperature - this is the converted value of temperature</br>
    
    > Usage</br>
    > temp_converter(100, temp_given_in = 'c')</br>

3. **speed_converter** - Converts speed from kmph to variety of scales

    > Arguments</br>
    > speed - value of temperature</br>
    > dist - the unit of distance to convert to ['km', 'm', 'ft', 'yrd']</br>
    > time - the unit of time to convert to ['day', 'hr', 'min', 's', 'ms']</br>
    
    > Returns</br>
    > converted_speed - this is the converted value of speed in the passed units</br>
    
    > Usage</br>
    > speed_converter(35, dist = 'm', time = 's')</br>

4. **squared_power_list** - Returns a list of the powers of a number based on start and end

    > Arguments</br>
    > number - the number whose powers needs to be returned, can be int or float</br>
    > start - the starting power in the list</br>
    > end - the ending power in the list</br>
    
    > Returns</br>
    > list_of_powers - a list of the powers of the given number</br>
    
    > Usage</br>
    > squared_power_list(2, start=0, end=5) returns [1, 2, 4, 8, 16, 32]</br>

5. **time_it** - Returns the average time taken to execute a function. It is defined as ```def time_it(fn, *args, repetitions= 1, **kwargs):```

    > Arguments</br>
    > fn - the function to be executed</br>
    > args - all the positional arguments to be sent to fn</br>
    > kwargs - all the keyword arguments to be sent to fn</br>
    > repetitions - the number of times the fn is to be executed</br>
    
    > Returns</br>
    > avg_time - the time taken to execute the fn on average</br>
    
    > Usage</br>
    > time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=500)</br>

### Test Case Results

The test cases have all passed as shown below.
![Test Cases](/test_cases_results.jpg)