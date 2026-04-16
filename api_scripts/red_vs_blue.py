import csv
import api_client

team = "frc3937"

years = api_client.get_years_active(team)

for year in years:
    redWins = 0
    blueWins = 0
    redLosses = 0
    blueLosses = 0
    blueTies = 0
    redTies = 0

    matches = api_client.get_matches_from_year_simple(team, year)
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

    with open('red_vs_blue.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([year, redWins, redLosses, redTies, blueWins, blueLosses, blueTies])