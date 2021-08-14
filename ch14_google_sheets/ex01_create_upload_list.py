import ezsheets


'''
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
print(ss)
print(ss.title)
'''

# Create
'''
ss = ezsheets.createSpreadsheet('Title of my new spreadsheet')
print(ss.title)
'''

'''
ss = ezsheets.upload('my_spreadsheet.xlsx')
print(ss.title)
'''

print(ezsheets.listSpreadsheets())


14
WORKING WITH GOOGLE SHEETS
Image
Google Sheets, the free, web-based spreadsheet application available to anyone with a Google account or Gmail address, has become a useful, feature-rich competitor to Excel. Google Sheets has its own API, but this API can be confusing to learn and use. This chapter covers the EZSheets third-party module, documented at https://ezsheets.readthedocs.io/. While not as full featured as the official Google Sheets API, EZSheets makes common spreadsheet tasks easy to perform.

Installing and Setting Up EZSheets
You can install EZSheets by opening a new terminal window and running pip install --user ezsheets. As part of this installation, EZSheets will also install the google-api-python-client, google-auth-httplib2, and google-auth-oauthlib modules. These modules allow your program to log in to Google’s servers and make API requests. EZSheets handles the interaction with these modules, so you don’t need to concern yourself with how they work.

Obtaining Credentials and Token Files
Before you can use EZSheets, you need to enable the Google Sheets and Google Drive APIs for your Google account. Visit the following web pages and click the Enable API buttons at the top of each:

https://console.developers.google.com/apis/library/sheets.googleapis.com/
https://console.developers.google.com/apis/library/drive.googleapis.com/
You’ll also need to obtain three files, which you should save in the same folder as your .py Python script that uses EZSheets:

A credentials file named credentials-sheets.json
A token for Google Sheets named token-sheets.pickle
A token for Google Drive named token-drive.pickle
The credentials file will generate the token files. The easiest way to obtain a credentials file is to go to the Google Sheets Python Quickstart page at https://developers.google.com/sheets/api/quickstart/python/ and click the blue Enable the Google Sheets API button, as shown in Figure 14-1. You’ll need to log in to your Google account to view this page.

image
Figure 14-1: Obtaining a credentials.json file.

Clicking this button will bring up a window with a Download Client Configuration link that lets you download a credentials.json file. Rename this file to credentials-sheets.json and place it in the same folder as your Python scripts.

Once you have a credentials-sheets.json file, run the import ezsheets module. The first time you import the EZSheets module, it will open a new browser window for you to log in to your Google account. Click Allow, as shown in Figure 14-2.

image
Figure 14-2: Allowing Quickstart to access your Google account

The message about Quickstart comes from the fact that you downloaded the credentials file from the Google Sheets Python Quickstart page. Note that this window will open twice: first for Google Sheets access and second for Google Drive access. EZSheets uses Google Drive access to upload, download, and delete spreadsheets.

After you log in, the browser window will prompt you to close it, and the token-sheets.pickle and token-drive.pickle files will appear in the same folder as credentials-sheets.json. You only need to go through this process the first time you run import ezsheets.

If you encounter an error after clicking Allow and the page seems to hang, make sure you have first enabled the Google Sheets and Drive APIs from the links at the start of this section. It may take a few minutes for Google’s servers to register this change, so you may have to wait before you can use EZSheets.

Don’t share the credential or token files with anyone—treat them like passwords.

Revoking the Credentials File
If you accidentally share the credential or token files with someone, they won’t be able to change your Google account password, but they will have access to your spreadsheets. You can revoke these files by going to the Google Cloud Platform developer’s console page at https://console.developers.google.com/. You’ll need to log in to your Google account to view this page. Click the Credentials link on the sidebar. Then click the trash can icon next to the credentials file you’ve accidentally shared, as shown in Figure 14-3.

image
Figure 14-3: The Credentials page in the Google Cloud Platform developer’s console

To generate a new credentials file from this page, click the Create Credentials button and select OAuth client ID, also shown in Figure 14-3. Next, for Application Type, select Other and give the file any name you like. This new credentials file will then be listed on the page, and you can click on the download icon to download it. The downloaded file will have a long, complicated filename, so you should rename it to the default filename that EZSheets attempts to load: credentials-sheets.json. You can also generate a new credential file by clicking the Enable the Google Sheets API button mentioned in the previous section.

Spreadsheet Objects
In Google Sheets, a spreadsheet can contain multiple sheets (also called worksheets), and each sheet contains columns and rows of values. Figure 14-4 shows a spreadsheet titled “Education Data” containing three sheets titled “Students,” “Classes,” and “Resources.” The first column of each sheet is labeled A, and the first row is labeled 1.

image
Figure 14-4: A spreadsheet titled “Education Data” with three sheets

While most of your work will involve modifying the Sheet objects, you can also modify Spreadsheet objects, as you’ll see in the next section.

Creating, Uploading, and Listing Spreadsheets
You can make a new Spreadsheet object from an existing spreadsheet, a blank spreadsheet, or an uploaded spreadsheet. To make a Spreadsheet object from an existing Google Sheets spreadsheet, you’ll need the spreadsheet’s ID string. The unique ID for a Google Sheets spreadsheet can be found in the URL, after the spreadsheets/d/ part and before the /edit part. For example, the spreadsheet featured in Figure 14-4 is located at the URL https://docs.google.com/spreadsheets/d/1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU/edit#gid=151537240/, so its ID is 1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU.

NOTE

The specific spreadsheet IDs used in this chapter are for my Google account’s spreadsheets. They won’t work if you enter them into your interactive shell. Go to https://sheets.google.com/ to create spreadsheets under your account and then get the IDs from the address bar.

Pass your spreadsheet’s ID as a string to the ezsheets.Spreadsheet() function to obtain a Spreadsheet object for its spreadsheet:

>>> import ezsheets
>>> ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
>>> ss
Spreadsheet(spreadsheetId='1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
>>> ss.title
'Education Data'

For convenience, you can also obtain a Spreadsheet object of an existing spreadsheet by passing the spreadsheet’s full URL to the function. Or, if there is only one spreadsheet in your Google account with that title, you can pass the title of the spreadsheet as a string.

To make a new, blank spreadsheet, call the ezsheets.createSpreadsheet() function and pass it a string for the new spreadsheet’s title. For example, enter the following into the interactive shell:

>>> import ezsheets
>>> ss = ezsheets.createSpreadsheet('Title of My New Spreadsheet')
>>> ss.title
'Title of My New Spreadsheet'

To upload an existing Excel, OpenOffice, CSV, or TSV spreadsheet to Google Sheets, pass the filename of the spreadsheet to ezsheets.upload(). Enter the following into the interactive shell, replacing my_spreadsheet.xlsx with a spreadsheet file of your own:

>>> import ezsheets
>>> ss = ezsheets.upload('my_spreadsheet.xlsx')
>>> ss.title
'my_spreadsheet'

You can list the spreadsheets in your Google account by calling the listSpreadsheets() function. Enter the following into the interactive shell after uploading a spreadsheet:

>>> ezsheets.listSpreadsheets()
{'1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU': 'Education Data'}

The listSpreadsheets() function returns a dictionary where the keys are spreadsheet IDs and the values are the titles of each spreadsheet.

Once you’ve obtained a Spreadsheet object, you can use its attributes and methods to manipulate the online spreadsheet hosted on Google Sheets.

Spreadsheet Attributes
While the actual data lives in a spreadsheet’s individual sheets, the Spreadsheet object has the following attributes for manipulating the spreadsheet itself: title, spreadsheetId, url, sheetTitles, and sheets. Enter the following into the interactive shell:

ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
print(ss.title)             # The title of the spreadsheet.
ss.title = 'Class Data'     # Change the title.
print(ss.spreadsheetId)     # The unique ID (this is a read-only attribute).
print(ss.url)               # The original URL (this is a read-only attribute).
print(ss.sheetTitles)       # The titles of all the Sheet objects
print(ss.sheets)            # The Sheet objects in this Spreadsheet, in order.
print(ss[0])                # The first Sheet object in this Spreadsheet.
print(ss['Students'])       # Sheets can also be accessed by title.
del ss[0]                   # Delete the first Sheet object in this Spreadsheet.
print(ss.sheetTitles)       # The "Students" Sheet object has been deleted:
