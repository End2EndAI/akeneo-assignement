import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from functions import generate_draw

class TestGenerateDraw(unittest.TestCase):
    
    def test_generate_draw_valid(self):
        MAX_ATTEMPTS = 1000
        input_dict = {
            'person_1': ['person_2', 'person_3'],
            'person_2': [],
            'person_3': ['person_1'],
            'person_4': ['person_2'],
            'person_5': ['person_3', 'person_4'],
            'person_6': ['person_1', 'person_5']
        }
        
        result = generate_draw(input_dict, MAX_ATTEMPTS)
        
        # Ensure the result is not None (i.e., a valid draw was found)
        self.assertIsNotNone(result)
        
        # Ensure each person is assigned to someone else and respects exclusion lists
        for person, assigned in result.items():
            self.assertNotEqual(person, assigned)  # No one should be assigned to themselves
            self.assertNotIn(assigned, input_dict[person])  # Assigned person should not be in blacklist

        # Ensure that all people are assigned
        self.assertEqual(set(result.keys()), set(input_dict.keys()))
        self.assertEqual(set(result.values()), set(input_dict.keys()))
        
    def test_generate_draw_no_valid_draw(self):
        MAX_ATTEMPTS = 1000
        input_dict = {
            'person_1': ['person_2','person_3','person_4'],
            'person_2': [],
            'person_3': [],
            'person_4': [],
        }
        
        result = generate_draw(input_dict, MAX_ATTEMPTS)
        
        # Since there's no valid draw possible, the result should be None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()