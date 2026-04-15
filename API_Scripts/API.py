import time

import requests
import key


BASE_URL = "https://www.thebluealliance.com/api/v3"
API_KEY = key.get_api_key()

HEADERS = {
    "X-TBA-Auth-Key": API_KEY
}

def get_years_active(team_key):
    url = f"{BASE_URL}/team/{team_key}/years_participated"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching years active for {team_key}")
        return 0

    return response.json()

def get_team_info(team_key):
    url = f"{BASE_URL}/team/{team_key}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching team info for {team_key}")
        return 0

    return response.json()

def get_matches_from_year_simple(team_key, year):
    url = f"{BASE_URL}/team/{team_key}/matches/{year}/simple"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching matches for {team_key}")
        return 0

    return response.json()

def get_awards_from_team(team_key):
    url = f"{BASE_URL}/team/{team_key}/awards"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching awards for {team_key}")
        return 0

    return response.json()

def get_awards_from_event(event_key):
    url = f"{BASE_URL}/event/{event_key}/awards"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching awards for {event_key}")
        return 0

    return response.json()

def get_all_teams():
    teams = []
    page = 0

    while True:
        url = f"{BASE_URL}/teams/{page}"
        response = requests.get(url, headers=HEADERS)

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