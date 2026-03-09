# Scan and transcribe, and try to translate

## Objective
The source is a Google Drive directory containing image files which are scans of documents typed or hand-written in Japanese: https://drive.google.com/drive/folders/1xeusaL_dbVq0ai3yiTV03Hs3-JvqpU6i The goal is to fill in a spreadsheet with:
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
There is a file size limit on what can be processed using the the APIs. However, it seems to be ok if uploaded from Google Cloud Storage.
One option is to upload the large scanned files to Google Cloud Storage, process it, then delete it from cloud storage (because it costs more money to store it over time).
- [ ] Figure out programmatic cloud storage operations:
  - [ ] Upload from Google Drive locations
  - [ ] Delete from GCP blob storage
- [ ] Be able to scan a file and get the text of it.
  - e.g. Use Cloud Vision to scan for transcription of Japanese. https://docs.cloud.google.com/vision/docs/ocr
  - [ ] Write the transcription to file, e.g. into one "cell" of a .csv file.
- [ ] Translate from Japanese to English. This does not depend on having the transcription written out to file, could be in-memory. But we need to transcription eventually anyway.
  - e.g. Use Cloud Translation API https://docs.cloud.google.com/translate/docs/reference/rest
  - [ ] Write the translated text back to the .csv file

- [X] Google Cloud Platform: Sign up for free trial, on personal account: we have 90 days starting 2026-Feb-18
  - [ ] hopefully we can run it on the free tier. https://docs.cloud.google.com/free/docs/free-cloud-features it's here somewhere https://console.cloud.google.com/
