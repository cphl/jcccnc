# Scan and transcribe, and try to translate

## Objective
The source is a Google Drive directory containing image files which are scans of documents typed or hand-written in Japanese. The goal is to fill in a spreadsheet with:
- Collection ID (the name of the image file, without `.tif` extension).
- The translation to English.
- Transcription of the Japanese text.
- URL link to the Drive location of that file.

The objective of what we're doing here is to provide a starting point for people with language proficiency to confirm and correct these transcriptions and translations.

## Requirements to run the thing
- Python
- python libraries, if you don't want to have to download the sheet yourself: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
- ...


## Steps to do the thing we want to do
- [x] Get the filenames into the Sheet. --> use copy-paste, then we don't need to do authentication and avoid security risks. To copy the filenames, highlight and the do Ctrl-Shift-C (otherwise it copies the URLs which is good for the next step, but not this one). Paste it in a text editor that can do Find-and-Replace to remove the `.tif` file extension. Paste that into the column!
  - [ ] Future work: automate the retrieval of the filenames https://www.geeksforgeeks.org/python/get-list-of-files-and-folders-in-google-drive-storage-using-python/
- [x] Get the URLs into the Sheet --> easy to just copy-paste from the Drive directory (and then we don't have to do authentication / authorization stuff)
- [ ] Future work: automate the retrieval of the Drive links for the files.
- [ ] Figure out how to use Google Cloud Vision library (the thing that runs Google lens), e.g. if using Python, it would be https://pypi.org/project/google-cloud-vision/ and you could try the tutorial project https://github.com/googlecodelabs/cloud-vision-python
  - [ ] Be able to scan a file and get the text of it. https://docs.cloud.google.com/vision/docs/ocr
  - [ ] Write the transcription to file, e.g. into one "cell" of a .csv file.
- [ ] Figure out how to use Cloud Translation API (the thing behind Google Translate) https://docs.cloud.google.com/translate/docs/reference/rest
  - [ ] Be able to translate some text.
  - [ ] Be able to translate the text from a scanned file from above.
  - [ ] Write the translation to file, e.g. into another cell of the same .csv mentioned above.
- [ ] Repeat!
- [ ] Oh at some point get a cloud account.
  - [X] Sign up for free trial, on personal account: we have 90 days starting 2026-Feb-18
  - [ ] hopefully we can run it on the free tier. https://docs.cloud.google.com/free/docs/free-cloud-features it's here somewhere https://console.cloud.google.com/
