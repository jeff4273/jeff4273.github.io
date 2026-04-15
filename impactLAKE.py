import requests
import csv


BASE_URL = "https://www.thebluealliance.com/api/v3"
API_KEY = "F5CQwbGuceE3Zc5d97Gm0VEuzdXoLqrbkYbThdSd3HlaKEEWZ2y7wejsnBzgVCGY"

HEADERS = {
    "X-TBA-Auth-Key": API_KEY
}

years = ["2007la", "2008la", "2009la", "2010la", "2011la", "2012la", "2013lake","2014lake","2015lake","2016lake", "2017lake", "2018lake", "2019lake", "2020lake", "2022lake", "2023lake", "2024lake", "2025lake", "2026lake"]
#years = ["2013arfa", "2014arfa", "2015arfa", "2016arlr", "2017arli", "2018arli", "2019arli", "2020arli", "2022arli", "2023arli", "2024arli", "2025arli", "2026arli"]

for year in years:
    url = f"{BASE_URL}/event/{year}/awards"
    response = requests.get(url, headers=HEADERS)

    data = response.json()

    #print(data)
    for award in data:
        if award['award_type'] == 0:  
            url = f"{BASE_URL}/team/{award['recipient_list'][0]['team_key']}"
            response = requests.get(url, headers=HEADERS)
            teamData = response.json()
            print(award['recipient_list'][0]['team_key'], award["name"], year, teamData["state_prov"])
            
