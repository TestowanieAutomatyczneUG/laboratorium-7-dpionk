import doctest
import unittest
import re


class CheckPassword:

    def ValidPasswordUnittest(self,password):
        if type(password) is str :
            pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
            if re.match(pattern, password):
                return True
            return False
        else:
            raise Exception("Wrong type of argument")

    def ValidPasswordDoctest(self, password):
        """ Takes a string (potential password) and return True if password is strong (has at leat 8 characters,
        including one number, one special character, one letter and one capital letter). If argument is not string type,
        raises exception
        >>> c = CheckPassword()
        >>> c.ValidPasswordDoctest("Haslo1234!")
        True
        >>> c.ValidPasswordDoctest("12345@dfkdF")
        True
        >>> c.ValidPasswordDoctest("dsfsdFFFF$$$$2021")
        True
        >>> c.ValidPasswordDoctest("ABCDAdfkdsfk20120^^^")
        True
        >>> c.ValidPasswordDoctest("12345")
        False
        >>> c.ValidPasswordDoctest("d3424")
        False
        >>> c.ValidPasswordDoctest("d4345fgfK")
        False
        >>> c.ValidPasswordDoctest("dsfsdfs54453hk^^^")
        False
        >>> c.ValidPasswordDoctest("AAA")
        False
        >>> c.ValidPasswordDoctest("")
        False
        >>> c.ValidPasswordDoctest("1Kl%")
        False
        >>> c.ValidPasswordDoctest("KKKKKKKKKKKKKKKsdf$$")
        False
        >>> c.ValidPasswordDoctest([])
        Traceback (most recent call last):
        ...
        Exception: Error: Wrong type of argument
        >>> c.ValidPasswordDoctest({})
        Traceback (most recent call last):
        ...
        Exception: Error: Wrong type of argument
        >>> c.ValidPasswordDoctest(True)
        Traceback (most recent call last):
        ...
        Exception: Error: Wrong type of argument
        >>> c.ValidPasswordDoctest(None)
        Traceback (most recent call last):
        ...
        Exception: Error: Wrong type of argument
        """
        if type(password) is str :
            pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
            if re.match(pattern, password):
                return True
            return False
        else:
            raise Exception("Wrong type of argument")


validPassword = CheckPassword().ValidPasswordUnittest               

class ValidPassword_Test(unittest.TestCase):

    def test_valid_password_ok(self):
        self.assertEqual(True, validPassword("Haslo1234!"))

    def test_valid_password_ok_2(self):
        self.assertEqual(True, validPassword("12345@dfkdF"))

    def test_valid_password_ok_3(self):
        self.assertEqual(True, validPassword("dsfsdFFFF$$$$2021"))

    def test_valid_password_ok_3(self):
        self.assertEqual(True, validPassword("ABCDAdfkdsfk20120^^^"))

    def test_valid_password_not_ok(self):
        self.assertEqual(False, validPassword("12345"))

    def test_valid_password_not_ok_2(self):
        self.assertEqual(False, validPassword("d3424"))
    
    def test_valid_password_not_ok_3(self):
        self.assertEqual(False, validPassword("d4345fgfK"))

    def test_valid_password_not_ok_4(self):
        self.assertEqual(False, validPassword("dsfsdfs54453hk^^^"))

    def test_valid_password_not_ok_5(self):
        self.assertEqual(False, validPassword("AAAAA"))

    def test_valid_password_not_ok_6(self):
        self.assertEqual(False, validPassword(""))

    def test_valid_password_not_ok_7(self):
        self.assertEqual(False, validPassword("1Kl%"))

    def test_valid_password_not_ok_8(self):
        self.assertEqual(False, validPassword("KKKKKKKKKKKKKKKsdf$$"))

    def test_valid_password_wrong_type(self):
        self.assertRaises(Exception, validPassword,[])

    def test_valid_password_wrong_type_2(self):
        self.assertRaises(Exception, validPassword, 0)

    def test_valid_password_wrong_type_3(self):
        self.assertRaises(Exception, validPassword, True)

    def test_valid_password_wrong_type_4(self):
        self.assertRaises(Exception, validPassword, None)
    
    doctest.testmod(extraglobs={'c': CheckPassword()})


    

    
    




        