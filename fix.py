import csv

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