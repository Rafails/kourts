import unittest
from boarding_cards import boarding_cards, incorrect_boarding_cards_version_one, incorrect_boarding_cards_version_two
from main import execute

class TestStringMethods(unittest.TestCase):

    def test_case_with_good_data(self):
        response = execute(boarding_cards)
        self.assertTrue(response['status'])

    def test_case_with_incorrect_data_version_one(self):
        response = execute(incorrect_boarding_cards_version_one)
        self.assertFalse(response['status'])

    def test_case_with_incorrect_data_version_two(self):
        response = execute(incorrect_boarding_cards_version_two)
        self.assertFalse(response['status'])

    def test_case_with_empty_data(self):
        response = execute([])
        self.assertFalse(response['status'])

if __name__ == '__main__':
    unittest.main()
