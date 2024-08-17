import json
import unittest
import csv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution import parse_fixed_width_file

class TestParseFixedWidthFile(unittest.TestCase):
    def setUp(self):
        # Create a mock spec JSON file
        self.spec = {
            "ColumnNames": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
            "Offsets": ["5", "12", "3", "2", "13", "7", "10", "13", "20", "13"],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }

        with open('spec.json', 'w') as spec_file:
            json.dump(self.spec, spec_file)

        # Create a mock fixed-width input file
        self.input_data = (
            "00123John Smith   34CA12345 Maple St650018M  123-456-7890john.smith@email.com  Manager         HR Department  \n"
            "00456Jane Doe     28NY98765 Elm Ave 100022F  234-567-8901jane.doe@email.com    Engineer        R&D Team       \n"
        )
        
        with open('input.txt', 'w', encoding='windows-1252') as input_file:
            input_file.write(self.input_data)

    def tearDown(self):
        # Clean up created files
        os.remove('spec.json')
        os.remove('input.txt')
        if os.path.exists('output.csv'):
            os.remove('output.csv')

    def test_parse_fixed_width_file(self):
        # Run the parser
        parse_fixed_width_file('spec.json', 'input.txt', 'output.csv')
        
        # Check that the output file was created
        self.assertTrue(os.path.exists('output.csv'))
        
        # Verify the content of the output CSV
        with open('output.csv', 'r', encoding='utf-8') as output_file:
            reader = csv.reader(output_file)
            rows = list(reader)
        
        # Check the number of fields in each row
        num_columns = len(self.spec["ColumnNames"])
        for row in rows:
            self.assertEqual(len(row), num_columns)

if __name__ == '__main__':
    unittest.main()