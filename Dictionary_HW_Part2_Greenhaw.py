def main():
    infile = 'WorldSeriesWinners.txt' 
    infile = open('WorldSeriesWinners.txt','r')
    team_lines= infile.readline().rstrip('\n')
    
    
    year_team_dict = get_year_team_dict(infile, team_lines)
    name_wins_dict = get_name_wins_dict(year_team_dict)
    
    for team, num_wins in name_wins_dict.items():
        print('Team: ', team, '\tWins: ', num_wins)

    for year, team in year_team_dict.items():
        print ('Year: ', year, '\tTeam: ', team)


    year = int(input('Please enter a year between 1903 and 2009: '))
    if year >= 1903 and year <=2008 and year!= 1994 and year!=1904:
        print(year_team_dict[year], 'won the World Series in ', year, 'and has won the World Series a total of', name_wins_dict[year_team_dict[year]], 'times')
        
    else:
        print('The world series was not played in', year)
      

#create dictionary keys are years & values are team winner
def get_year_team_dict(infile, team_lines):
    
    year_team_dict = {}
    
    for year in range(1903, 2009):
        if year == 1904:
            year_team_dict[year] = "No World Series was played"
        elif year == 1994:
            year_team_dict[year] = "No World Series was played"
        else:
            year_team_dict[year] = team_lines
            team_lines = infile.readline().rstrip('\n')
    return year_team_dict

#create dictionary keys are names & values are # won
def get_name_wins_dict(year_team_dict):

    names_wins_dict = {}
    for year in range(1903, 2009):
        team = year_team_dict[year]
        if not team in names_wins_dict:
            names_wins_dict[team] = 1
        else:
            names_wins_dict[team] = names_wins_dict[team] + 1
        
    return names_wins_dict

main()