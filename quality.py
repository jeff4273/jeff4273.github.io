import requests
import csv
import time

API_KEY = "F5CQwbGuceE3Zc5d97Gm0VEuzdXoLqrbkYbThdSd3HlaKEEWZ2y7wejsnBzgVCGY"
BASE_URL = "https://www.thebluealliance.com/api/v3"

HEADERS = {
    "X-TBA-Auth-Key": API_KEY
}

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
        time.sleep(0.2)  # be nice to API

    return teams


def count_quality_awards(team_key):
    url = f"{BASE_URL}/team/{team_key}/awards"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching awards for {team_key}")
        return 0

    awards = response.json()

    count = 0
    for award in awards:
        if award["award_type"] == 17:  # Quality Award
            count += 1

    return count


def main():
    teams = get_all_teams()

    results = []

    for i, team in enumerate(teams):
        team_key = team["key"]
        team_number = team["team_number"]

        count = count_quality_awards(team_key)

        results.append((team_number, count))

        if i % 100 == 0:
            print(f"{i+1}/{len(teams)} - Team {team_number}: {count}")

        #time.sleep(0.2)

    # Sort descending by award count
    results.sort(key=lambda x: x[1], reverse=True)

    # Write CSV
    with open("frc_quality_awards_ranking.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Team Number", "Quality Awards"])

        for rank, (team_number, count) in enumerate(results, start=1):
            writer.writerow([rank, team_number, count])

    print("Done! Saved to frc_quality_awards_ranking.csv")


if __name__ == "__main__":
    main()