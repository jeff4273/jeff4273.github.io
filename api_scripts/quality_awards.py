import csv
import API_Scripts.tba_api.api_client as api_client
from API_Scripts.tba_api.award_types import AWARD_TYPES

def count_quality_awards(team_key):
    awards = api_client.get_awards_from_team(team_key)
    #print(awards)
    count = 0
    for award in awards:
        if award["award_type"] == AWARD_TYPES["QUALITY"]:  
            count += 1
            #print(count)

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

    # Input and output CSV files
    input_csv = "frc_quality_awards_ranking.csv"
    output_csv = "frc_quality_awards_ranking_ties_fixed.csv"

    # Read the existing CSV
    teams = []
    with open(input_csv, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            teams.append({
                "team_number": row["Team Number"],
                "count": int(row["Quality Awards"])
            })

    # Sort descending by award count just in case
    teams.sort(key=lambda x: x["count"], reverse=True)

    # Assign tie-aware ranks (standard competition ranking)
    last_count = None
    last_rank = 0
    for i, team in enumerate(teams, start=1):
        if team["count"] != last_count:
            rank = i
            last_rank = rank
            last_count = team["count"]
        else:
            rank = last_rank  # same rank for ties
        team["rank"] = rank

    # Write the new CSV
    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Team Number", "Quality Awards"])
        for team in teams:
            writer.writerow([team["rank"], team["team_number"], team["count"]])

    print(f"Done! Saved tie-corrected CSV to {output_csv}")

if __name__ == "__main__":
    main()