import unittest
import analyze_number as az

class TestAnalyzeNumber(unittest.TestCase):
    def setUp(self):
        self.an = az.AnalyzeNumber()

    def test_is_prime(self):
        self.assertTrue(self.an.is_prime(13))
        self.assertFalse(self.an.is_prime(10))
        self.assertFalse(self.an.is_prime(1))

    def test_is_perfect(self):
        self.assertTrue(self.an.is_perfect(28))
        self.assertFalse(self.an.is_perfect(10))

    def test_is_armstrong(self):
        self.assertTrue(self.an.is_armstrong(153))
        self.assertFalse(self.an.is_armstrong(100))

    def test_find_prime_number(self):
        self.assertEqual(self.an.find_prime_number([2, 3, 4, 5]), [2, 3, 5])

    def test_analyze_num_range(self):
        result = self.an.analyze_num_range([6, 28, 153])
        self.assertEqual(result["Perfect"], 2)
        self.assertEqual(result["Armstrong"], 1)

    # Uncomment this if format_analysis exists in your class
    # def test_format_analysis(self):
    #     sample = {
    #         "Prime": 2, "list_prime": [2, 3],
    #         "Perfect": 1, "list_perfect": [6],
    #         "Armstrong": 1, "list_armstrong": [153]
    #     }
    #     formatted = self.an.format_analysis(sample)
    #     self.assertIn("Prime Count: 2", formatted)
    #     self.assertIn("Perfect Count: 1", formatted)
    #     self.assertIn("Armstrongs: [153]", formatted)

if __name__ == "__main__":
    unittest.main(verbosity=2)