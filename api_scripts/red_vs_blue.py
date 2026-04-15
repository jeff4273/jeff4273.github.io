import requests
import csv
import api_key


BASE_URL = "https://www.thebluealliance.com/api/v3"
API_KEY = api_key.get_api_key()
team = "frc3937"

HEADERS = {
    "X-TBA-Auth-Key": API_KEY
}

def get_years_active(team_key):
    url = f"{BASE_URL}/team/{team_key}/years_participated"
    response = requests.get(url, headers=HEADERS)

    return response.json()

def get_matches_from_year(team_key, year):
    url = f"{BASE_URL}/team/{team_key}/matches/{year}/simple"
    response = requests.get(url, headers=HEADERS)

    return response.json()

years = get_years_active(team)

for year in years:
    redWins = 0
    blueWins = 0
    redLosses = 0
    blueLosses = 0
    blueTies = 0
    redTies = 0

    matches = get_matches_from_year(team, year)
    for match in matches:
        if team in match["alliances"]["red"]["team_keys"]:
            if match["winning_alliance"] == "red":
                redWins += 1
            elif match["winning_alliance"] == "blue":
                redLosses += 1
            else:
                redTies += 1
        elif team in match["alliances"]["blue"]["team_keys"]:
            if match["winning_alliance"] == "blue":
                blueWins += 1
            elif match["winning_alliance"] == "red":
                blueLosses += 1
            else:
                blueTies += 1
    print(f"{year}: Red Wins: {redWins}, Red Losses: {redLosses}, Red Ties: {redTies}, Blue Wins: {blueWins}, Blue Losses: {blueLosses}, Blue Ties: {blueTies}")
    #Write to csv
    with open('red_vs_blue.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([year, redWins, redLosses, redTies, blueWins, blueLosses, blueTies])