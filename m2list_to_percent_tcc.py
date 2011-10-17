#!/usr/bin/env python

import csv
import string

m2File = open('m2list.csv', 'rU')   # Open new OBME database.
m2List = list(csv.reader(m2File, delimiter=',', quotechar='"'))   # Cast csv read to list.
m2File.close()

m2ListSorted = sorted(m2List, key=lambda k: (k[3].lower(), k[1].lower()))   # Sort by last, then first name.

# TODO: alphabetize, then categorize by specialty.

# General care
listFP     = []
listI      = []
listPD     = []

# Specialty care
listAI     = []
listC      = []
listCD     = []
listD      = []
listEND    = []
listOTO    = []
listGE     = []
listGS     = []
listHEMONC = []
listID     = []
listNEP    = []
listN      = []
listOBG    = []
listOM     = []
listOPH    = []
listORS    = []
listPMR    = []
listDPM    = []
listP      = []
listPY     = []
listPUD    = []
listRHU    = []
listSLM    = []
listUC     = []
listU      = []


for row in m2ListSorted:
    if row[10]   == 'Family Practice':                      listFP.append(row)
    elif row[10] == 'Internal Medicine':                    listI.append(row)
    elif row[10] == 'Pediatrics':                           listPD.append(row)
    elif row[10] == 'Allergy and Immunology':               listAI.append(row)
    elif row[10] == 'Cardiology':                           listC.append(row)
    elif row[10] == 'Cardiovascular Disease':               listCD.append(row)
    elif row[10] == 'Dermatology':                          listD.append(row)
    elif row[10] == 'Endocrinology':                        listEND.append(row)
    elif row[10] == ('Otology' or \
                    'Laryngology' or \
                    'Rhinology'):                           listOTO.append(row)
    elif row[10] == 'Gastroenterology':                     listGE.append(row)
    elif row[10] == 'General Surgery':                      listGS.append(row)
    elif row[10] == ('Hematology' or \
                    'Oncology'):                            listHEMONC.append(row)
    elif row[10] == 'Infectious Diseases':                  listID.append(row)
    elif row[10] == 'Nephrology':                           listNEP.append(row)
    elif row[10] == 'Neurology':                            listN.append(row)
    elif row[10] == 'Obstetrics and Gynecology':            listOBG.append(row)
    elif row[10] == 'Occupational Medicine':                listOM.append(row)
    elif row[10] == 'Ophthalmology':                        listOPH.append(row)
    elif row[10] == 'Orthopedic Surgery':                   listORS.append(row)
    elif row[10] == 'Physical Medicine & Rehabilitation':   listPMR.append(row)
    elif row[10] == 'Podiatry':                             listDPM.append(row)
    elif row[10] == 'Psychiatry':                           listP.append(row)
    elif row[10] == ('Psychoanalysis' or \
                    'Psychosomatic Medicine'):              listPY.append(row)
    elif row[10] == 'Pulmonary Diseases':                   listPUD.append(row)
    elif row[10] == 'Rheumatology':                         listRHU.append(row)
    elif row[10] == 'Sleep Medicine':                       listSLM.append(row)
    elif row[10] == 'Urgent Care':                          listUC.append(row)
    elif row[10] == 'Urology':                              listU.append(row)

m2ListSorted = []
m2ListSorted.append(['Title', 'First Name', 'Middle Name', 'Last Name', 'Company', 'Address 1', 'Address 2', 'City', 'State', 'Zip', 'Specialty', 'Birthyear', 'County'])
m2ListSorted.extend(listFP)
m2ListSorted.extend(listI)
m2ListSorted.extend(listPD)
m2ListSorted.extend(listAI)
m2ListSorted.extend(listC)
m2ListSorted.extend(listCD)
m2ListSorted.extend(listD)
m2ListSorted.extend(listEND)
m2ListSorted.extend(listOTO)
m2ListSorted.extend(listGE)
m2ListSorted.extend(listGS)
m2ListSorted.extend(listHEMONC)
m2ListSorted.extend(listID)
m2ListSorted.extend(listNEP)
m2ListSorted.extend(listN)
m2ListSorted.extend(listOBG)
m2ListSorted.extend(listOM)
m2ListSorted.extend(listOPH)
m2ListSorted.extend(listORS)
m2ListSorted.extend(listPMR)
m2ListSorted.extend(listDPM)
m2ListSorted.extend(listP)
m2ListSorted.extend(listPY)
m2ListSorted.extend(listPUD)
m2ListSorted.extend(listRHU)
m2ListSorted.extend(listSLM)
m2ListSorted.extend(listUC)
m2ListSorted.extend(listU)

def writeFile(listname, filename):
    outFile = open(filename+'.csv', 'wb')   # Open file to write.
    writer = csv.writer(outFile, delimiter=',', quotechar='"')
    writer.writerows(listname)
    outFile.close()

writeFile(m2ListSorted, "m2listsorted")

