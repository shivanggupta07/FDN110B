#------------------------------------------#
# Title: CDInventory.py
# Desc: Mod. of starter script to use dictionaries (Assignment_05)
# Change Log: (Who, When, What)
# SGupta, 2021-Aug-08, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            dicRow1 = {}
            lstRow = row.strip().split(',')
            dicRow1 = {'ID': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow1)
            print(lstRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
    
        # 2. Add data to the table (2d-list) each time the user wants to add data
        userInputDict = {}
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        userInputDict = {'ID': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(userInputDict)
        pass
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row)
        pass
    elif strChoice == 'd':
        # functionality of deleting an entry
        userId = input("what ID do you want to delete? : ")
        for dicRow in lstTbl: 
            if int(userId) == dicRow['ID']:
                del lstTbl[lstTbl.index(dicRow)]
                print("\ndicRow got deleted", userId)
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')
