import csv
import io
import sys

test_image_url = 'https://drive.google.com/open?id=1atcLItyeFJabUcFLzvfO0pjq_0fKl3pp&usp=drive_copy'
test_image_filename = 'YSB_Box_8_F1 Memo for S F Branch Mananger 昭和十年壱月十六日0002.tif'

# TODO: read filenames from Google Drive https://www.geeksforgeeks.org/python/get-list-of-files-and-folders-in-google-drive-storage-using-python/
# I copy-pasted them already, but we can use this to verify! (this time)

# TODO: read URL links, probably similar to above


# TODO: given a file, (scan with Cloud Vision API), output transcription
def transcribe(image_filename):
	"""Image file goes in, text comes out."""
	return "いくつかの日本語のテキスト"

image_file = test_image_filename
jpn_transcription = transcribe(image_file)
byte_str = jpn_transcription.encode('utf-8)')
print(f" - transcribe gives this ")

sys.stdout.buffer.write(byte_str)

# TODO: given text, (use Translation API), output translation.
#       it might be that we could do it directly from the Vision library I DUNNO
def translate_to_english(jpn_text):
	"""Japanese text goes in, English text comes out."""
	return 'Some English text'

eng_translation = translate_to_english(jpn_transcription)
print(f"\ntranslate_to_english gives: {eng_translation}.")

# TODO: input args for drive location, username + auth, ...?