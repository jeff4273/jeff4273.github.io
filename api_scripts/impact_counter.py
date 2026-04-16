import tba_api.api_client as api_client

years = ["2007la", "2008la", "2009la", "2010la", "2011la", "2012la", "2013lake","2014lake","2015lake","2016lake", "2017lake", "2018lake", "2019lake", "2020lake", "2022lake", "2023lake", "2024lake", "2025lake", "2026lake"]
#years = ["2013arfa", "2014arfa", "2015arfa", "2016arlr", "2017arli", "2018arli", "2019arli", "2020arli", "2022arli", "2023arli", "2024arli", "2025arli", "2026arli"]

for year in years:
    data = api_client.get_awards_from_event(year)

    #print(data)
    for award in data:
        if award['award_type'] == 0:  
            teamData = api_client.get_team_info(award['recipient_list'][0]['team_key'])
            #print(teamData)
            print(award['recipient_list'][0]['team_key'], award["name"], year, teamData["state_prov"])
            
