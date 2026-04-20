import tba_api.api_client as api_client
from tba_api.award_types import AWARD_TYPES
import pandas as pd

team = "frc254"

client = api_client.TBAClient()

team_number = int(team[3:])

df = pd.DataFrame(
    data=[[team_number] + [0] * len(AWARD_TYPES)],
    columns=["Team_Number"] + list(AWARD_TYPES.keys()),
)

last_skipped_event = None

awards = client.get_awards_from_team(team)

for award in awards:
    award_type = award["award_type"]
    for key, value in AWARD_TYPES.items():

        event = award["event_key"]
        invalid = False

        if event == last_skipped_event:
            invalid = True
        elif client.get_event_info_simple(event)["event_type"] in [99, 100, -1]:
            print(f"Skipping {event} for {team} due to invalid event type")
            last_skipped_event = event
            invalid = True

        if value == award_type and not invalid:
            df[key] += 1

df.to_csv(f"frc{team_number}_award_counts.csv", index=False)

