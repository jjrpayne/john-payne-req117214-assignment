import unittest
import supplement_calculator

class TestSupplementCalculator(unittest.TestCase):
    def test_single_no_children(self):
        in_data = {
            "id": 1,
            "numberOfChildren": 0,
            "familyComposition": "single",
            "familyUnitInPayForDecember": True
        }
        out_data = {
            "id": 1,
            "isEligible": True,
            "baseAmount": 60.0,
            "childrenAmount": 0.0,
            "supplementAmount": 60.0
        }
        self.assertEqual(supplement_calculator.calculate(in_data), out_data)

    def test_couple_no_children(self):
        in_data = {
            "id": 1,
            "numberOfChildren": 0,
            "familyComposition": "couple",
            "familyUnitInPayForDecember": True
        }
        out_data = {
            "id": 1,
            "isEligible": True,
            "baseAmount": 120.0,
            "childrenAmount": 0.0,
            "supplementAmount": 120.0
        }
        self.assertEqual(supplement_calculator.calculate(in_data), out_data)

    def test_single_children(self):
        in_data = {
            "id": 1,
            "numberOfChildren": 2,
            "familyComposition": "single",
            "familyUnitInPayForDecember": True
        }
        out_data = {
            "id": 1,
            "isEligible": True,
            "baseAmount": 60.0,
            "childrenAmount": 40.0,
            "supplementAmount": 100.0
        }
        self.assertEqual(supplement_calculator.calculate(in_data), out_data)

    def test_couple_children(self):
        in_data = {
            "id": 1,
            "numberOfChildren": 2,
            "familyComposition": "couple",
            "familyUnitInPayForDecember": True
        }
        out_data = {
            "id": 1,
            "isEligible": True,
            "baseAmount": 120.0,
            "childrenAmount": 40.0,
            "supplementAmount": 160.0
        }
        self.assertEqual(supplement_calculator.calculate(in_data), out_data)

    def test_ineligible(self):
        in_data = {
            "id": 1,
            "numberOfChildren": 2,
            "familyComposition": "couple",
            "familyUnitInPayForDecember": False
        }
        out_data = {
            "id": 1,
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
        self.assertEqual(supplement_calculator.calculate(in_data), out_data)

    def test_invalid_family_composition(self):
        in_data = {
            "id": 1,
            "numberOfChildren": 1,
            "familyComposition": "abc",
            "familyUnitInPayForDecember": True
        }
        with self.assertRaises(Exception) as e:
            supplement_calculator.calculate(in_data)
        self.assertTrue("Invalid familyComposition value" in str(e.exception))

if __name__ == '__main__':
    unittest.main()