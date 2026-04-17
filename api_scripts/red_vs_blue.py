import csv
import tba_api.api_client as api_client

team = "frc3937"

years = api_client.get_years_active(team)

for year in years:
    red_wins = 0
    blue_wins = 0
    red_losses = 0
    blue_losses = 0
    blue_ties = 0
    red_ties = 0

    matches = api_client.get_matches_from_year_simple(team, year)
    for match in matches:
        if team in match["alliances"]["red"]["team_keys"]:
            if match["winning_alliance"] == "red":
                red_wins += 1
            elif match["winning_alliance"] == "blue":
                red_losses += 1
            else:
                red_ties += 1
        elif team in match["alliances"]["blue"]["team_keys"]:
            if match["winning_alliance"] == "blue":
                blue_wins += 1
            elif match["winning_alliance"] == "red":
                blue_losses += 1
            else:
                blue_ties += 1
    print(
        f"{year}: Red Wins: {red_wins}, Red Losses: {red_losses}, Red Ties: {red_ties}, "
        f"Blue Wins: {blue_wins}, Blue Losses: {blue_losses}, Blue Ties: {blue_ties}"
    )

    with open('red_vs_blue.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([year, red_wins, red_losses, red_ties, blue_wins, blue_losses, blue_ties])