import csv
import api_client
from award_types import AWARD_TYPES

def count_quality_awards(team_key):
    awards = api_client.get_awards_from_team(team_key)
    #print(awards)
    count = 0
    for award in awards:
        if award["award_type"] == AWARD_TYPES["QUALITY"]:  
            count += 1
            print(count)

    return count


def main():
    teams = api_client.get_all_teams()

    results = []

    for i, team in enumerate(teams):
        team_key = team["key"]
        team_number = team["team_number"]

        count = count_quality_awards(team_key)

        results.append((team_number, count))

        if i % 100 == 0:
            print(f"{i+1}/{len(teams)} - Team {team_number}: {count}")


    results.sort(key=lambda x: x[1], reverse=True)

    with open("frc_quality_awards_ranking.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Team Number", "Quality Awards"])

        for rank, (team_number, count) in enumerate(results, start=1):
            writer.writerow([rank, team_number, count])

    print("Done! Saved to frc_quality_awards_ranking.csv")


if __name__ == "__main__":
    main()