# Reads the .csv file for the Oka repo and fills in the 4 columns based on the Oka code
import csv
import io

###################################
### Define the Oka code lookups ###
###################################

# The prefix of the Oka code.
language = {
	'C': 'Chinese',
	'E': 'English',
	'EJ': 'English & Japanese',
	'F': 'French',
	'J': 'Japanese',
	'S': 'Spanish',
}

# The first digit of the Oka code. (Lists start numbering from 0.)
subject_matter = [
	'Others',
	'History',
	'Social Science: Politics',
	'Social Science: Economy/Finances',
	'Literature',
	'Philosophy',
	'Language',
	'Agriculture, Industry, etc.',
	'Art, Customs, etc.',
	'Children,'
]

# The second digit of the Oka code.
topic = [
	'General',
	'History-Fiction',
	'Essay, Diary, Poetry, etc.',
	'Biography',
	'Social Problems',
	'Education',
	'Religion',
	'Immigration',
	'Arts & Crafts, Sports, etc.',
	'Others',
]

# The third digit of the Oka code
geographic_ethnic = [
	'Miscellaneous',
	'United States/American',
	'Japan/Japanese',
	'Japan-U.S./Japanese American',
	'Canada/Canadian',
	'Japan-Canada/Japanese Canadian',
	'U.S./Asian',  # TODO: this is a bit different from theh other ones, double-check that it's correct
	'Central & South America',
	'Asia',
	'Europe',
]


def parse(oka_code):
	"""Reads the prefix and first 3 digits of the Oka code.

	Input: Oka code, e.g. `J 123.45`
	Returns: the words that describe what the code means for
	language, topic, subject matter, geographic/ethnic.
	"""
	# Separate the prefix letter and the 3 digits after it
	lang = oka_code[0]
	if oka_code[1] == ' ':
		(s, t, g) = [int(x) for x in oka_code[2:5]]  # skip the space after the prefix
	else:
		(s, t, g) = [int(x) for x in oka_code[1:4]]

	return (language[lang], subject_matter[s], topic[t], geographic_ethnic[g])


################################################################
### Read the spreadsheet and write data to the 4 new columns ###
################################################################

repo_file_path = "in.csv"
outfile = "out.csv"
def read_write(input_file_path, output_file_path):
	"""Takes the path of the file that has the spreadsheet and does stuff."""
	with open(input_file_path, mode = "r", encoding="utf-8") as file:
		csv_reader = csv.DictReader(file)  # Uses column names as dictionary keys

		with open(output_file_path, 'w', newline='') as csvfile:
			for row in csv_reader:
				if row['OKA CODE']:  # if it's not an empty row, process it
					generated_words = parse(row['OKA CODE'])

					# Write generated data to a new file
					writer = csv.writer(csvfile)
					writer.writerow(generated_words)
				else:  # otherwise it's an empty row, so write a blank row
					writer.writerow(['', '', '', ''])
	print(f"Done! See results in {output_file_path}.")

#################
### Test runs ###
#################

# the_words = parse("J 362.4/001")
# print(the_words)

# print(prefix_language["EJ"])

read_write(repo_file_path, outfile)
