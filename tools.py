# Tools for Tropical cyclones naming

import re
import pandas as pd
from itertools import chain
from ipywidgets import FileUpload, SelectMultiple, RadioButtons, Button
from IPython.display import display
import functools
from tqdm.notebook import tqdm
tqdm.pandas()


#####################################################################################################################
# EXTRACTING ALL THE TC NAMES FROM THE DATABASE 

EXTRA = True

# Load the database of Tropical Cyclones names
info_df = pd.read_excel('TC-names.xlsx', sheet_name = 'Information')

# Define how to read the file 
to_skip = [0,1] # sheets to skip, as they contain information on the database and not actual TC names
if not EXTRA : to_skip.append(len(info_df) + 1)
num_sheets = len(info_df) + 2
all_sheets = list(range(num_sheets))

# Read the file
all_df = pd.read_excel('TC-names.xlsx', sheet_name = all_sheets)

# Function to return the incides of the sheets to read
def filter_sheet_indices(all_sheets, to_skip) :
    temp_all_sheets = all_sheets.copy()
    for idx in to_skip : 
        temp_all_sheets.remove(idx)
    return temp_all_sheets

# Function to clean the list of TC names
def clean_list(all_names) :
    # remove some formatting errors
    all_names = [str(name).strip('\xa0') for name in all_names]
    # remove duplicates
    all_names = list(set(all_names))
    # remove `nan` if exists
    while 'nan' in all_names : all_names.remove('nan')
    # return the sorted list
    return sorted(all_names)

# Function to extract all TC names from the database
def extract_all_names(all_sheets, to_skip) :
    all_names = []
    for sheet_idx in filter_sheet_indices(all_sheets, to_skip) :
        sheet_names = all_df[sheet_idx].values.flatten()
        all_names.append(sheet_names)
    return clean_list(list(chain(*all_names)))

# Extract all TC names existing in the database
all_names = extract_all_names(all_sheets, to_skip)
lw_tc_names = [name.lower() for name in all_names]

# For a given event_name, extract the TC name(s) 
def extract_tc_name(event_name) :
    matches = []
    for word in re.findall('[a-zA-Z]+-*[a-zA-Z]+', event_name) : 
        try: 
            idx = lw_tc_names.index(word.lower())
            matches.append(all_names[idx])
        except: continue
    return matches

#####################################################################################################################
# Apply to input file

myupload = FileUpload(accept='.xlsx', multiple=False)

#display(myupload) #INN

def get_sheets_selection(myupload) : 
    # first, we save a copy of the uploaded file locally as `output.xlsx`
    with open('output.xlsx', 'wb') as output_file: 
        for uploaded_filename in myupload.value:
            content = myupload.value[uploaded_filename]['content']   
            output_file.write(content) 
    # then we read its sheet names
    truc = pd.ExcelFile('output.xlsx')
    # and we ask the user to select which sheets are of interest
    sheets_selection = SelectMultiple(
        options=truc.sheet_names,
        value=truc.sheet_names,
        description='Sheetnames',
        disabled=False
    )
    return sheets_selection

#sheets_selection = get_sheets_selection(myupload) #INN
#display(sheets_selection) #INN

def get_columns_selection(sheets_selection) : 
    # list of the sheets of interest
    sheets = list(sheets_selection.value)
    # read the sheets of interest
    data = pd.read_excel('output.xlsx', sheet_name = sheets)
    # for each sheet, we want to know which column contains the events names
    column_widgets = []
    for sheet in sheets :
        df = data[sheet]
        display(df)
        column_selection = RadioButtons(options = df.columns, description='Columns', disabled=False)
        column_widgets.append(column_selection)
        display(column_selection)
    return column_widgets

#column_widgets = get_columns_selection(sheets_selection) #INN

def parse_names(sheets_selection, column_widgets) : 
    # name of the column of interest in each sheet
    columns = [column_widget.value for column_widget in column_widgets]
    # list of the names of the sheets
    sheetnames = list(sheets_selection.value) 
    with pd.ExcelWriter('output.xlsx', mode = 'a', engine = 'openpyxl', if_sheet_exists = 'replace') as writer:
        for sheet, column in zip(sheetnames, columns) :
            sheet_data = pd.read_excel('output.xlsx', sheet_name = sheet)
            sheet_data['TC names'] = sheet_data[column].apply(extract_tc_name)
            sheet_data = sheet_data.explode('TC names')
            sheet_data.to_excel(writer, sheet_name = sheet)
