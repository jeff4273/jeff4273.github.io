import tba_api.api_client as api_client

team = ""

results = {}

client = api_client.TBAClient()
events = client.get_events_from_team(team)


for event in events:
    if event["event_type"] == 3:
        ranking = client.get_rankings_from_event(event["key"])
        for current_team in ranking["rankings"]:
            if current_team["team_key"] == team:
                results[event["key"]] = current_team["rank"]

print("Year: Rank\n------------")        
for event_key, rank in results.items():
    print(f"{event_key[:4]}: {rank}")