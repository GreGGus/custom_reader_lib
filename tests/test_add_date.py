from unittest import TestCase
from custom_reader_lib.delta.delta_add_date import generate_date

class TryTesting(TestCase):
    def test_date_ok(self):
        generate_date()
        date = generate_date() #function from other python file. 
        date_formatted = date.strftime("%B")
        self.assertEqual(date_formatted, "May")
