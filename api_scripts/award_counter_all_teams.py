import tba_api.api_client as api_client
from tba_api.award_types import AWARD_TYPES
import pandas as pd

client = api_client.TBAClient()

teams = client.get_all_teams()

rows = []

for team in teams:
    awards = client.get_awards_from_team(team['key'])

    row = {key: 0 for key in AWARD_TYPES.keys()}
    row["Team_Number"] = int(team["key"][3:])

    for award in awards:
        award_type = award["award_type"]
        for key, value in AWARD_TYPES.items():
            if value == award_type:
                row[key] += 1

    if row["Team_Number"] % 100 == 0:
        print(row)

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("frc_award_counts.csv", index=False)