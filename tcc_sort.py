#!/usr/bin/env python

import csv
import string

#TODO: in program, keep all data in OBME format.

oldFile = open('oldlist.csv', 'rU')   # Open old Clinic database.
oldList = list(csv.reader(oldFile, delimiter=',', quotechar='"'))   # Cast csv read to list.
oldFile.close()

newFile = open('newlist.csv', 'rU')   # Open new OBME database.
newList = list(csv.reader(newFile, delimiter=',', quotechar='"'))   # Cast csv read to list.
newFile.close()

def writeFile(listname, filename):
    outFile = open(filename+'.csv', 'wb')   # Open file to write.
    writer = csv.writer(outFile, delimiter=',', quotechar='"')
    writer.writerows(listname)
    outFile.close()



### Begin filter ###

rowNum = 0
colNum = 0
incompleteList = []

for col in newList[0]:
    # print '%-3s: %s' % (colNum, col)   # Print column indices for newList.
    colNum += 1
del newList[0]   # Delete non-data row.

newListLen = len(newList)
print "\nProcessing %s entries from 2011 OBME database...\n" % (newListLen)

numNotActive = 0
numWrongLicense = 0
numWrongCounty = 0
numWrongState = 0   # Was not in instructions, but some entries have mismatching county and state.
numWrongZip = 0
numWrongSpecialty = 0

for row in newList:   # NOTE that in memory, row is separate from newList[rowNum].
    colNum = 0
    emptyCols = []
    for col in row:
        row[colNum] = col.strip()   # Strip leading and trailing whitespace from entries.
        # print '%-20s: %s' % (header[colNum], col)
        colNum += 1

    # Look for rows with incomplete data.
    if row[25] == '': emptyCols.append(25)
    if row[26] == '': emptyCols.append(26)
    if row[21] == '': emptyCols.append(21)
    if row[32] == '': emptyCols.append(32)
    
    if len(emptyCols) > 0:
        row.append(emptyCols)
        incompleteList.append(row)
 
    # Remove inactive physicians.
    try:
        if row[25] != 'Active':
            newList[rowNum] = 0
            # row = 0   # Uncomment to see deletion count after each filter.
            numNotActive += 1
    except TypeError:   # Specify TypeError so you can notice other errors.
        pass
    
    # Filter by license type.
    try:
        if row[26] == ('AC License' or \
                       'EMT2 License' or \
                       'EMT3 License' or \
                       'EMT4 License' or \
                       'ES License'):
            newList[rowNum] = 0
            # row = 0
            numWrongLicense += 1
    except TypeError:
        pass

    # Filter by county.
    try:
        if row[21] != 'Benton' and \
           row[21] != 'Lincoln' and \
           row[21] != 'Linn' and \
           row[21] != 'Polk' and \
           row[21] != 'Marion' and \
           row[21] != 'Lane':
            newList[rowNum] = 0
            # row = 0
            numWrongCounty += 1
    except TypeError:
        pass

    # Filter by state.
    try:
        if row[18] != 'OR':
            newList[rowNum] = 0
            # row = 0
            numWrongState += 1
    except TypeError:
        pass

    # Filter by zip code.
    try:
        if (row[21] == 'Polk' and (row[19] != '97361' and \
                                   row[19] != '97351' and \
                                   row[19] != '97338')) or \
           (row[21] == 'Lane' and (row[19] != '97448' and \
                                   row[19] != '97446' and \
                                   row[19] != '97348')) or \
           (row[21] == 'Marion' and row[19] != '97304'):
            newList[rowNum] = 0   # Mark for deletion.
            # row = 0
            numWrongZip += 1
    except TypeError:
        pass
    
    # Filter by specialty (some physicians have multiple specialties separated by commas).
    try:
        spList = [s.strip() for s in row[32].split(',')]
        for specialty in spList:
            if specialty == ('Acupuncture' or 'Addictionology' or 'Addiction Medicine' or 'Broncho-Esophagology' or 'Bloodbanking' or 'Claims Adjudicator' or 'Clinical Pathology' or 'Dermatopathology' or 'Diagnostic Radiology' or 'Emergency Medicine' or 'Forensic Pathology' or 'Medical Genetics' or 'Hospital Administration' or 'Hypnosis' or 'Industrial Medicine' or 'Legal Medicine' or 'Nuclear Medicine' or 'Nuclear Radiology' or 'Occupational Medicine' or 'Oral Surgery' or 'Pathology' or 'Pediatric Radiology' or 'Pharmacology' or 'Psychiatry Neurology' or 'Psychoanalysis' or 'Psychosomatic Medicine' or 'Radioisotopic Pathology' or 'Therapeutic Radiology' or 'Traumatic Surgery'):
                newList[rowNum] = 0
                # row = 0
                numWrongSpecialty += 1
    except TypeError:
        pass

    rowNum += 1

newList[:] = [x for x in newList if x != 0]   # Remove all instances of 0. Note that at this point, newList still contains all 38 fields of the OBME database. This needs to be trimmed/merged.

print "Inactive           : %s" % (numNotActive)
print "Wrong license type : %s" % (numWrongLicense)
print "Wrong county       : %s" % (numWrongCounty)
print "Wrong state        : %s" % (numWrongState)
print "Wrong zip code     : %s" % (numWrongZip)
print "Wrong specialty    : %s" % (numWrongSpecialty)

print "\nOf %s, deleted %s rows, keeping %s.\n" % (rowNum, newListLen-len(newList), len(newList))

writeFile(newList, "newlistafterfilter")



### Process incompleteList ###

print "%s entries from OBME database have insufficient data to be safely filtered. Matching names from old list with incomplete entries...\n" % (len(incompleteList))

rowNum = 0
keepList = []

for incRow in incompleteList:
    for oldRow in oldList:
        if oldRow[1] == incRow[0] and oldRow[2] == incRow[1] and oldRow[3] == incRow[2]:
            keepList.append(incRow)
            break
        else:
            pass

print "%s matches found. The rest has been discarded.\n" % (len(keepList))

writeFile(incompleteList, "incompletelist")
writeFile(keepList, "keeplist")



### Begin merge ###

rowNum = 0
colNum = 0
m1List = []
delList = []
oldDupNum = 0
oldUniqueNum = 0

# m1List.append([])   # Append empty list to m1List.
for col in oldList[0]:
    # print '%-3s: %s' % (colNum, col)   # Print column indices for oldList.
    # m1List[0].append(col)   # Populate label row of m1List.
    colNum += 1
del oldList[0]   # Delete non-data row.

print "\nMerging %s entries from old list with %s from filtered OBME database...\n" % (len(oldList), len(newList))

# m1List[0].append('BIRTHYEAR')

# Merge in old entries first.
for oldRow in oldList:
    dupExists = False
    for newRow in newList:
        if oldRow[1] == newRow[0] and oldRow[2] == newRow[1] and oldRow[3] == newRow[2]:   # Match first, middle, and last names.
            dupExists = True
            break
    for keepRow in keepList:
        if oldRow[1] == keepRow[0] and oldRow[2] == keepRow[1] and oldRow[3] == keepRow[2]:   # Check to see if name from oldList is in keepList.
            dupExists = True
            # print "Keeping: %s %s %s" % (keepRow[0], keepRow[1], keepRow[2])
            break
    # TODO: Multiple choices for dupExists -- If entry is in newList, check to see if it should be updated. If entry is in keepList (i.e., incomplete), keep the old data.
    if dupExists:   # Do for every duplicate entry.
        m1Row = []
        m1Row.append(oldRow[0])   # Title
        m1Row.append(oldRow[1])   # First name
        m1Row.append(oldRow[2])   # Middle name
        m1Row.append(oldRow[3])   # Last name

        # if oldRow[4] == newRow[9]:   # Check if company name is same
        #     m1List[mergeNum][4] = oldRow[4]   # Keep old data.
        # else:
        #     m1List[mergeNum][4] = newRow[9]   # Keep new data.
        #     print "%s %s %s now works at %s." % (oldRow[1], oldRow[2], oldRow[3], checkoldRow[9])
        #     # TODO: rearrange address/company names? Need address recognition system to sort into proper fields.

        m1Row.append(oldRow[4])   # Company
        m1Row.append(oldRow[5])   # addr1
        m1Row.append(oldRow[6])   # addr2

        m1Row.append(oldRow[7])   # City
        m1Row.append(oldRow[8])   # State
        m1Row.append(oldRow[9])   # Zip
        m1Row.append(oldRow[10])   # Specialty  TODO: need lookup table for specialty codes.
        m1Row.append(newRow[6])   # Birthyear
        m1Row.append(newRow[21])   # County
        m1List.append(m1Row)   # Add row to m1List.
        newList.remove(newRow)   # Remove duplicate row from newList.
        oldDupNum += 1
    elif not dupExists:
    #     print "%s %s %s cannot be found in the 2011 OBME database." % (oldRow[1], oldRow[2], oldRow[3])
        delList.append(oldRow)   # Add old entry to deletion list.
        oldUniqueNum += 1

for newRow in newList:
    m1Row = []
    m1Row.append(newRow[5])   # Title
    m1Row.append(newRow[0])   # First name
    m1Row.append(newRow[1])   # Middle name
    m1Row.append(newRow[2])   # Last name
    m1Row.append(newRow[15])   # Company
    m1Row.append(newRow[9])   # addr1
    m1Row.append(newRow[10])   # addr2
    m1Row.append(newRow[17])   # City
    m1Row.append(newRow[18])   # State
    m1Row.append(newRow[19])   # Zip
    m1Row.append(newRow[32])   # Specialty
    m1Row.append(newRow[6])   # Birthyear
    m1Row.append(newRow[21])   # County
    m1List.append(m1Row)   # Add reordered newRow to m1List.

print "\nOf %s in old list, %s are in filtered OBME database, leaving %s for deletion and %s in merge list 1.\n" % (len(oldList), oldDupNum, oldUniqueNum, len(m1List))

# for entry in delList:
#     print "Deleting: %s %s %s" % (entry[1], entry[2], entry[3])

writeFile(m1List, "m1list")
writeFile(delList, "dellist")



### Process Ms. Corwin's PA/FNP list ###

pfFile = open('pafnp.csv', 'rU')   # Open Ms. Corwin's PA and FNP database.
pfList = list(csv.reader(pfFile, delimiter=',', quotechar='"'))   # Cast csv read to list.
pfFile.close()

rowNum = 0
colNum = 0
m2List = []   # Merge #2
m2DupNum = 0
pfDelNum = 0

for col in pfList[0]:
    # print '%-3s: %s' % (colNum, col)   # Print column indices for pfList.
    colNum += 1
del pfList[0]   # Delete non-data row.

print "\nMerging %s entries from first merge with %s entries from PA/FNP list...\n" % (len(m1List), len(pfList))

for row in pfList:
    colNum = 0
    emptyCols = []
    for col in row:
        row[colNum] = string.strip(col)   # Strip leading and trailing whitespace from entries.
        colNum += 1

for m1Row in m1List:
    for pfRow in pfList:
        dupExists = False
        if m1Row[1] == pfRow[0] and m1Row[2] == pfRow[1] and m1Row[3] == pfRow[2]:   # Match first, middle, and last names.
            row2Del = pfRow
            dupExists = True
            m2DupNum += 1
            # print "%s %s is a duplicate." % (pfRow[0], pfRow[2])
            break
        else:
            pass
    if dupExists:
        pfList.remove(row2Del)

m2List.extend(m1List)   # Add m1List to m2List.

for pfRow in pfList:
    keepThisRow = False
    if (pfRow[9] == '' and pfRow[10] == '' and pfRow[11] == '' and pfRow[12] == ''):   # Check for incompleteness (added by hand by Ms. Corwin).
        keepThisRow = True
    if pfRow[5] == '1':   # FTE
        keepThisRow = True
    if (pfRow[35] == 'Family Medicine' or pfRow[35] == 'Internal Medicine') and pfRow[34] == 'O':   # Specialty and inpatient/outpatient status.
        keepThisRow = True

    if keepThisRow:
        m2Row = []
        m2Row.append(pfRow[7])   # Title
        m2Row.append(pfRow[0])   # First name
        m2Row.append(pfRow[1])   # Middle name
        m2Row.append(pfRow[2])   # Last name
        m2Row.append(pfRow[17])   # Company
        m2Row.append(pfRow[11])   # addr1
        m2Row.append(pfRow[12])   # addr2
        m2Row.append(pfRow[19])   # City
        m2Row.append(pfRow[20])   # State
        m2Row.append(pfRow[21])   # Zip
        m2Row.append(pfRow[35])   # Specialty
        m2Row.append(pfRow[8])   # Birthyear
        m2Row.append(pfRow[23])   # County
        m2List.append(m2Row)   # Add reordered pfRow to m2List.
    elif not keepThisRow:
        pfDelNum += 1

print "From %s in merge list 1, %s are in PA/FNP list. Deleting %s from PA/FNP list, leaving %s in final merge list.\n" % (len(m1List), m2DupNum, pfDelNum, len(m2List))

m2List.insert(0, ['Title', 'First Name', 'Middle Name', 'Last Name', 'Company', 'Address 1', 'Address 2', 'City', 'State', 'Zip', 'Specialty', 'Birthyear', 'County'])

writeFile(m2List, "m2list")

