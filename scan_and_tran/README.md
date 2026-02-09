# Scan and transcribe, and try to translate

## Objective
The source is a Google Drive directory containing image files which are scans of documents typed or hand-written in Japanese. The goal is to fill in a spreadsheet with:
- Collection ID (the name of the image file, without `.tif` extension).
- The translation to English.
- Transcription of the Japanese text.
- URL link to the Drive location of that file.

The objective of what we're doing here is to provide a starting point for people with language proficiency to confirm and correct these transcriptions and translations.

## Steps to do the thing we want to do
- [ ] Get the filenames into the Sheet.
- [ ] Get the URLs into the Sheet.
- [ ] Figure out how to use Google Cloud Vision library (the thing that runs Google lens), e.g. if using Python, it would be https://pypi.org/project/google-cloud-vision/ and you could try the tutorial project https://github.com/googlecodelabs/cloud-vision-python
  - [ ] Be able to scan a file and get the text of it.
  - [ ] Write it the transcription, e.g. into a .csv file
- [ ] Figure out how to use Cloud Translation API (the thing behind Google Translate) https://docs.cloud.google.com/translate/docs/reference/rest
  - [ ] Be able to translate some text.
  - [ ] Be able to translate the text from a scanned file from above.
  - [ ] Write the translation to the same file.
- [ ] Repeat!
- Oh at some point get a cloud account, hopefully we can run it on the free tier. https://docs.cloud.google.com/free/docs/free-cloud-features it's here somewhere https://console.cloud.google.com/