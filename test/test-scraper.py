import unittest
from scraper.sports.rugby import scrape_rugby_fixtures

class TestScraper(unittest.TestCase):
    def test_rugby_scraper(self):
        fixtures = scrape_rugby_fixtures()
        self.assertIsInstance(fixtures, list)
        if fixtures:
            self.assertIn('date', fixtures[0])
            self.assertIn('teams', fixtures[0])
            self.assertIn('competition', fixtures[0])

if __name__ == '__main__':
    unittest.main()