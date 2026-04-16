import time

import requests
import tba_api.api_key as api_key

class TBAClient:
    BASE_URL = "https://www.thebluealliance.com/api/v3"
    API_KEY = api_key.get_api_key()

    HEADERS = {
        "X-TBA-Auth-Key": API_KEY
    }
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)


    def get_years_active(self,team_key):
        if not self.valid_team_key(team_key):
            print(f"Invalid team key: {team_key}")
            return 0

        url = f"{self.BASE_URL}/team/{team_key}/years_participated"
        response = self.session.get(url)

        if response.status_code != 200:
            print(f"Error fetching years active for {team_key}")
            return 0

        return response.json()

    def get_team_info(self, team_key):
        if not self.valid_team_key(team_key):
            print(f"Invalid team key: {team_key}")
            return 0

        url = f"{self.BASE_URL}/team/{team_key}"
        response = self.session.get(url)

        if response.status_code != 200:
            print(f"Error fetching team info for {team_key}")
            return 0

        return response.json()

    def get_matches_from_year_simple(self, team_key, year):
        if not self.valid_team_key(team_key):
            print(f"Invalid team key: {team_key}")
            return 0

        url = f"{self.BASE_URL}/team/{team_key}/matches/{year}/simple"
        response = self.session.get(url)

        if response.status_code != 200:
            print(f"Error fetching matches for {team_key}")
            return 0

        return response.json()

    def get_awards_from_team(self, team_key):
        if not self.valid_team_key(team_key):
            print(f"Invalid team key: {team_key}")
            return 0

        url = f"{self.BASE_URL}/team/{team_key}/awards"
        response = self.session.get(url)

        if response.status_code != 200:
            print(f"Error fetching awards for {team_key}")
            return 0

        return response.json()

    def get_awards_from_event(self, event_key):
        url = f"{self.BASE_URL}/event/{event_key}/awards"
        response = self.session.get(url)

        if response.status_code != 200:
            print(f"Error fetching awards for {event_key}")
            return 0

        return response.json()


    def get_all_teams(self):
        teams = []
        page = 0

        while True:
            url = f"{self.BASE_URL}/teams/{page}"
            response = self.session.get(url)

            if response.status_code != 200:
                print("Error fetching teams:", response.status_code)
                break

            data = response.json()
            if not data:
                break

            teams.extend(data)
            print(f"Fetched page {page}, total teams: {len(teams)}")

            page += 1
            time.sleep(0.2)  

        return teams

    def valid_team_key(self, team_key):
        if not team_key.startswith("frc"):
            return False
        return True