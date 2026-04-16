import tba_api.api_client as api_client
from tba_api.award_types import AWARD_TYPES
import pandas as pd

team = "frc3937"

#print(AWARD_TYPES.keys())

team_number = int(team[3:])

df = pd.DataFrame(data=[[team_number] + [0]*len(AWARD_TYPES)], columns=["Team_Number"] + list(AWARD_TYPES.keys()))

#print(df)

awards = api_client.get_awards_from_team(team)

for award in awards:
    award_type = award["award_type"]
    #print(award_type)
    for key, value in AWARD_TYPES.items():
        if value == award_type:
            df[key] += 1

#print(df)
df.to_csv("frc3937_award_counts.csv", index=False)

