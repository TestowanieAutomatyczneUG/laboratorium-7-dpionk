import doctest

class FizzBuzz:
    def game(self, num): 
        """Takes a number (type must be int or float, in other case function returns
        an Exception) and returns "Fizz" if a number is divisible by 3, "Buzz" if 
        is divisible by 5, and "FizzBuzz" if is divisible by both 3 and 5 If it is not 
        divisible by 3, 5 or 15, it returns given number.
        # >>> c = FizzBuzz()
        >>> c.game(3)
        'Fizz'
        >>> c.game(5)
        'Buzz'
        >>> c.game(15)
        'FizzBuzz'
        >>> c.game(-15)
        'FizzBuzz'
        >>> c.game(5.5354354354)
        5.5354354354
        >>> c.game(104729)
        104729
        >>> c.game(0)
        'FizzBuzz'
        >>> c.game(333333333333333213333339)
        'Fizz'
        >>> c.game(3333333333333332133333345594359435)
        'Buzz'
        >>> c.game(3333333333333333333332133336915)
        'FizzBuzz'
        >>> c.game(-3333333333333332133333345594359435)
        'Buzz'
        >>> c.game(-3333333333333333333332133336915)
        'FizzBuzz'
        >>> c.game(-333333333333333213333339)
        'Fizz'
        >>> c.game(-104729)
        -104729
        >>> c.game([])
        Traceback (most recent call last):
        ...
        Exception: Error: number is not an int or float
        >>> c.game({})
        Traceback (most recent call last):
        ...
        Exception: Error: number is not an int or float
        >>> c.game(True)
        Traceback (most recent call last):
        ...
        Exception: Error: number is not an int or float
        >>> c.game(None)
        Traceback (most recent call last):
        ...
        Exception: Error: number is not an int or float

        """
        if type(num) is int or type(num) is float:
            if type(num) is int or type(num) is float:
                if num % 3 == 0 and num % 15 != 0:
                    return("Fizz")
                elif num % 5 == 0 and num % 15 != 0 :
                    return("Buzz")
                elif num % 15 == 0:
                    return("FizzBuzz")
                else:
                    return(num)
        else:
            raise Exception("Error: number is not an int or float")


doctest.testmod(extraglobs={'c': FizzBuzz()})
