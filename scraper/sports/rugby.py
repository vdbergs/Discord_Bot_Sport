import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_rugby_fixtures():
    url = "https://supersport.com/rugby/fixtures"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Avoid bot detection
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        fixtures = []
        # Example selector (adjust based on actual site structure)
        for match in soup.select('.match-row'):  # Hypothetical selector
            date = match.select_one('.date').text.strip()
            teams = match.select_one('.teams').text.strip()
            competition = match.select_one('.competition').text.strip()
            fixtures.append({
                'date': datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d'),
                'teams': teams,
                'competition': competition
            })
        return fixtures
    except Exception as e:
        print(f"Error scraping fixtures: {e}")
        return []