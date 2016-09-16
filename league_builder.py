
import csv
import sys

player_list = 'soccer_players.csv'
team_list = [{'Team': 'Dragons', 'Time': 'March 17, 1pm'},
			{'Team': 'Sharks', 'Time': 'March 17, 3pm'},
			{'Team': 'Raptors', 'Time': 'March 18, 1pm'}]
letter_contents = '''Dear {}, 

Your child {} has been selected to participate in Battle Royale as part of the {} team. 
The first practice is on {} and ambulances will be standing by. 
Please ensure all weapons and armor are updated and equipped before this time. 

宜しくお願い致します。

ビートたけし
'''


def get_file_data(filename):
	# get the file data and return a list of dictionaries with child data
	# quit if the file doesn't exist
	try:
		with open(filename) as csvfile:
			filedata = csv.DictReader(csvfile)
			return list(filedata)
	except IOError:
		print('File {} does not exist'.format(filename))
		sys.exit()

def team_picker(kidslist, teams):
	# add a team to each kid in a cycle based on the number of teams
	kids_with_teams = []
	for num, kid in enumerate(kidslist):
		index = num % 3
		kid['Team'] = teams[index]['Team']
		kid['Time'] = teams[index]['Time']
		kids_with_teams.append(kid)
	return kids_with_teams


def sort_kids(kidslist, got_experience):
	# return a list of kids with/out soccer experience
	sorted_kids = []
	for kid in kidslist:
		if kid['Soccer Experience'] == got_experience:
			sorted_kids.append(kid)
	return sorted_kids


def write_letters(kidslist):
	# take dict with kid info and write out files
	for kid in kidslist:
		# print('{} {} {}'.format(kid['Name'], kid['Team'], kid['Soccer Experience']))
		filename = kid['Name'].lower().replace(' ','_') + '.txt'
		with open(filename,'w') as file:
			file.write(letter_contents.format(kid['Guardian Name(s)'], kid['Name'], kid['Team'], kid['Time']))


if __name__ == '__main__':

	# Get the kid raw data
	raw_kids = get_file_data(player_list)

	# Divide them into experienced and inexperienced groups
	experienced_kids = sort_kids(raw_kids, 'YES')
	inexperienced_kids = sort_kids(raw_kids, 'NO')

	# Put them into teams and add their first game time
	experienced_kids = team_picker(experienced_kids, team_list)
	inexperienced_kids = team_picker(inexperienced_kids, team_list)

	# Put them all back together
	kids = experienced_kids + inexperienced_kids

	# Write the letters
	write_letters(kids)




