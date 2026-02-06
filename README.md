# jcccnc

## How to use

### Prerequisite

You need to have Python on your computer.

### What to do
Here is ONE way to make it work.

1. Download a copy of the Oka Repository spreadsheet as a .csv file to your computer, call it "in.csv" for simplicity, and put it somewhere you'll remember. Note that when you download, it only takes one of the tabs, not the entire spreadsheet.
2. Save oka_code_writer.py on to your computer (from here, github is here). Put it in the same place as the .csv file.
3. Run it. On windows, open `cmd` from the start menu, cd to the directory the files are in, and run `python oka_code_writer.py`. I can't remember what the command is on other operating systems. THe same? idk lul
4. It should complete right away with the result being in a file called `out.csv` you don't need to open it.
5. Go back to the Oka Repo sheet and click on the first cell in the column "Prefix (Language". Assuming you haven't filled any of this in yet, it'll be an empty cell. (Hmm, i don't have a way to start partway down the sheet yet...)
6. Go to File > Import > Upload > {select `out.csv` from your computer (and open}
7. On the "Import file" dialogue, "Import location", select the drop down option for "Replace data at selected cell". For "Separator type" pick "Comma". Click "Import data"
8. Since I haven't made a full test suite for all the codes yet, I eyeballed the data to check that it was alright.
9. Note that since we can only download one tab at a time, this will need to be repeated for each tab in the sheet.

## Future work... maybe
- full test suite for all the code variations.
- either a diff tool or instructions to check a diff to verify previously entered data.
- error handling in case we have unexpected format of input data.
- custom column header entry
- stick this on a web interface so people don't have to download and run things on their own computer.
