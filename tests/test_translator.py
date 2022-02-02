import unittest
from translator import  english_to_french, french_to_english
class Testlang(unittest.TestCase): 
    
    def test_etof1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_etof2(self):
        self.assertNotEqual(english_to_french("None"), "") 
    def test_etof3(self):
        self.assertNotEqual(english_to_french(0), "") 

class Testlang1(unittest.TestCase): 

    def test_ftoe1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_ftoe2(self):
        self.assertNotEqual(french_to_english("None"), "") 
    def test_ftoe3(self):
        self.assertNotEqual(french_to_english(0), "")

unittest.main()        


  