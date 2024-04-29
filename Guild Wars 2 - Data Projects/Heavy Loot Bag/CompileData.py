#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import os

def ParseFileNames(FileNames):
    """
    Retrieve data from file names
    """
    
    # Get file information from filenames
    FileDates = FileNames.str[:10]
    FileDescription = FileNames.str[13:-4]
    FileDataType = FileDescription.str.strip('0123456789() ')

    # Find which files are Mystic Forging weapons
    ExoticsFiles = pd.Series(FileNames[FileDataType.values == 'Exotics'])

    # Get salvaged item data from file information
    SalvageFiles = pd.Series(FileNames[FileDataType.values != 'Exotics'])
    SalvageDescription = pd.Series(FileDescription[FileDataType.values != 'Exotics'])
    SalvageNumber = (SalvageDescription.str[:5]).str.strip()
    SalvageType = pd.Series(FileDataType[SalvageFiles.index])

    # Store salvaged item in a dataframe
    SalvageItems = pd.DataFrame(data = {'Files': SalvageFiles, 
                                          'Item':  SalvageType, 
                                          'Number': SalvageNumber})
    
    return ExoticsFiles, SalvageItems


def ConcatCSVData(ItemName, DirPath, FileList, SalvageQty):
    """
    Join CSV data from multiple item files into a single dataframe
    """
    
    Data = pd.DataFrame()
    
    # Get data from each CSV file for the specified item
    for indFile in range(0,len(FileList)):
        indRawData = FileList.index[indFile]
        CSVData = pd.read_csv(DirPath + FileList[indRawData],
                             index_col='Name')
        if 'Quantity' in CSVData.columns:
            CSVData = CSVData.rename(columns={'Quantity': 'Total'})
        Data = pd.concat([Data, CSVData['Total'].rename(indFile)], axis=1).fillna(0).astype(int)
    
    # Add column for salvaged item quantities
    SalvageQty = pd.DataFrame(SalvageQty).reset_index(drop=True).transpose()  
    SalvageQty.rename(index={"Number":ItemName}, inplace=True)
    Data = pd.concat([SalvageQty, Data], axis=0)
    
    # Rename index column for tables
    Data.index.name = 'Sample'
    
    return Data

# Name of item of interest
DirPath = os.path.dirname(__file__).replace('\\', '/') + '/CSV Files/'

FileNames = pd.Series(os.listdir(DirPath))
ItemName = 'Heavy Loot Bag'

# Get all salvage files and item quantities for the item of interest
SalvageFiles = ParseFileNames(FileNames)[1]
FileList = SalvageFiles[SalvageFiles.Item == ItemName].Files
SalvageQty = SalvageFiles[SalvageFiles.Item == ItemName].Number.astype(int)

# Join salvage data into a single CSV
if len(FileList) > 0:
    Data = ConcatCSVData(ItemName, DirPath, FileList, SalvageQty).fillna(0).astype(int)
    Data.to_csv(ItemName+'.csv', index=True, index_label='Sample', header=True)
    print('Data compilation successful!')
    input('Press Enter to exit')
else: 
    print('No data for item ' + ItemName + ' was found.')
    input('Press Enter to exit')
