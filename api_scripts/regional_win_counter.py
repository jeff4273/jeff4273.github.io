import tba_api.api_client as api_client
from tba_api.award_types import AWARD_TYPES

#years = ["2007la", "2008la", "2009la", "2010la", "2011la", "2012la", "2013lake","2014lake","2015lake","2016lake", "2017lake", "2018lake", "2019lake", "2020lake", "2022lake", "2023lake", "2024lake", "2025lake", "2026lake"]
years = ["2013arfa", "2014arfa", "2015arfa", "2016arlr", "2017arli", "2018arli", "2019arli", "2020arli", "2022arli", "2023arli", "2024arli", "2025arli", "2026arli"]

results = {}

for year in years:
    data = api_client.get_awards_from_event(year)

    for award in data:
        if award['award_type'] == AWARD_TYPES["WINNER"]:
            print(award)
            for team in award['recipient_list']:
                team_num = team['team_key']
                results[team_num] = results.get(team_num, 0) + 1

sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

print(sorted_results)