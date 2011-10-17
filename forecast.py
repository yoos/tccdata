#!/usr/bin/env python

import csv
import string

mergeFile = open('m2list.csv', 'rU')   # Open old Clinic database.
mergeList = list(csv.reader(mergeFile, delimiter=',', quotechar='"'))   # Cast csv read to list.
mergeFile.close()


numFP  = [0, 0, 0, 0, 0, 0]
numI   = [0, 0, 0, 0, 0, 0]
numPD  = [0, 0, 0, 0, 0, 0]
numAI  = [0, 0, 0, 0, 0, 0]
numC   = [0, 0, 0, 0, 0, 0]
numCD  = [0, 0, 0, 0, 0, 0]
numD   = [0, 0, 0, 0, 0, 0]
numEND = [0, 0, 0, 0, 0, 0]
numOTO = [0, 0, 0, 0, 0, 0]   # Ear, Nose, and Throat (Otolaryngology) -- Otology,Laryngology,Rhinology
numGE  = [0, 0, 0, 0, 0, 0]
numGS  = [0, 0, 0, 0, 0, 0]
numHEM = [0, 0, 0, 0, 0, 0]
numONC = [0, 0, 0, 0, 0, 0]
numID  = [0, 0, 0, 0, 0, 0]
numNEP = [0, 0, 0, 0, 0, 0]
numN   = [0, 0, 0, 0, 0, 0]
numOBG = [0, 0, 0, 0, 0, 0]
numOM  = [0, 0, 0, 0, 0, 0]
numOPH = [0, 0, 0, 0, 0, 0]
numORS = [0, 0, 0, 0, 0, 0]   # Orthopedic Surgery. Orthopedics is not in OBME.
numPMR = [0, 0, 0, 0, 0, 0]
numDPM = [0, 0, 0, 0, 0, 0]   # Podiatry
numP   = [0, 0, 0, 0, 0, 0]
numPY  = [0, 0, 0, 0, 0, 0]   # Psychoanalysis or Psychosomatic Medicine
numPUD = [0, 0, 0, 0, 0, 0]
numRHU = [0, 0, 0, 0, 0, 0]
numSLM = [0, 0, 0, 0, 0, 0]   # Sleep Medicine (abbrv. made up)
numUC  = [0, 0, 0, 0, 0, 0]   # Urgent Care (abbrv. made up)
numU   = [0, 0, 0, 0, 0, 0]

total = 0 

columnToUpdate = 0

for mergeRow in mergeList:
    discard = False
    if mergeRow[0] == 'Dr.':
        columnToUpdate = 0   # Even if doctorate.
    else:
        columnToUpdate = 1   # Odd if not.

    if mergeRow[12] == 'Benton': columnToUpdate += 0
    elif mergeRow[12] == 'Linn': columnToUpdate += 2
    elif mergeRow[12] == 'Lincoln': columnToUpdate += 4
    else: discard = True   # Discard if not in BT, LC, or LI.

    spList = [s.strip() for s in mergeRow[10].split(',')]
    if not discard:
        for specialty in spList:
            # NOTE: The tally resulting from this will exceed the number of doctors available if at least one doctor specializes in multiple fields.
            if specialty == 'Family Practice':                    numFP[columnToUpdate] += 1
            if specialty == 'Internal Medicine':                  numI[columnToUpdate] += 1
            if specialty == 'Pediatrics':                         numPD[columnToUpdate] += 1
            if specialty == 'Allergy and Immunology':             numAI[columnToUpdate] += 1
            if specialty == 'Cardiology':                         numC[columnToUpdate] += 1
            if specialty == 'Cardiovascular Disease':             numCD[columnToUpdate] += 1
            if specialty == 'Dermatology':                        numD[columnToUpdate] += 1
            if specialty == 'Endocrinology':                      numEND[columnToUpdate] += 1
            if specialty == ('Otology' or \
                             'Laryngology' or \
                             'Rhinology'):                        numOTO[columnToUpdate] += 1
            if specialty == 'Gastroenterology':                   numGE[columnToUpdate] += 1
            if specialty == 'General Surgery':                    numGS[columnToUpdate] += 1
            if specialty == 'Hematology':                         numHEM[columnToUpdate] += 1
            if specialty == 'Oncology':                           numONC[columnToUpdate] += 1
            if specialty == 'Infectious Diseases':                numID[columnToUpdate] += 1
            if specialty == 'Nephrology':                         numNEP[columnToUpdate] += 1
            if specialty == 'Neurology':                          numN[columnToUpdate] += 1
            if specialty == 'Obstetrics and Gynecology':          numOBG[columnToUpdate] += 1
            if specialty == 'Occupational Medicine':              numOM[columnToUpdate] += 1
            if specialty == 'Ophthalmology':                      numOPH[columnToUpdate] += 1
            if specialty == 'Orthopedic Surgery':                 numORS[columnToUpdate] += 1
            if specialty == 'Physical Medicine & Rehabilitation': numPMR[columnToUpdate] += 1
            if specialty == 'Podiatry':                           numDPM[columnToUpdate] += 1
            if specialty == 'Psychiatry':                         numP[columnToUpdate] += 1
            if specialty == ('Psychoanalysis' or \
                             'Psychosomatic Medicine'):           numPY[columnToUpdate] += 1
            if specialty == 'Pulmonary Diseases':                 numPUD[columnToUpdate] += 1
            if specialty == 'Rheumatology':                       numRHU[columnToUpdate] += 1
            if specialty == 'Sleep Medicine':                     numSLM[columnToUpdate] += 1
            if specialty == 'Urgent Care':                        numUC[columnToUpdate] += 1
            if specialty == 'Urology':                            numU[columnToUpdate] += 1


numPY  = [4, 0, 0, 0, 0, 0]
numSLM = [4, 1, 0, 0, 0, 1]
numUC  = []

print 'FP : %s' % (numFP)
print 'I  : %s' % (numI)
print 'PD : %s' % (numPD)

print 'Total Primary:', sum(numFP)+sum(numI)+sum(numPD), '\n'

print 'AI     : %s' % (numAI)
print 'C      : %s' % (numC)
print 'CD     : %s' % (numCD)
print 'D      : %s' % (numD)
print 'END    : %s' % (numEND)
print 'OTO    : %s' % (numOTO)
print 'GE     : %s' % (numGE)
print 'GS     : %s' % (numGS)
print 'HEM/ONC: %s' % ([numHEM[x] + numONC[x] for x in range(6)])
print 'ID     : %s' % (numID)
print 'NEP    : %s' % (numNEP)
print 'N      : %s' % (numN)
print 'OBG    : %s' % (numOBG)
print 'OM     : %s' % (numOM)
print 'OPH    : %s' % (numOPH)
print 'ORS    : %s' % (numORS)
print 'PMR    : %s' % (numPMR)
print 'DPM    : %s' % (numDPM)
print 'P      : %s' % (numP)
print 'PY     : %s' % (numPY)
print 'PUD    : %s' % (numPUD)
print 'RHU    : %s' % (numRHU)
print 'SLM    : %s' % (numSLM)
print 'UC     : %s' % (numUC)
print 'U      : %s' % (numU)

total = sum(numFP) + sum(numI) + sum(numPD) + sum(numAI) + sum(numC) + sum(numCD) + sum(numD) + sum(numEND) + sum(numOTO) + sum(numGE) + sum(numGS) + sum(numHEM) + sum(numONC) + sum(numID) + sum(numNEP) + sum(numN) + sum(numOBG) + sum(numOM) + sum(numOPH) + sum(numORS) + sum(numPMR) + sum(numDPM) + sum(numP) + sum(numPY) + sum(numPUD) + sum(numRHU) + sum(numSLM) + sum(numUC) + sum(numU)

print 'Total Specialty:', total - (sum(numFP)+sum(numI)+sum(numPD)), '\n'

print 'Total:', total

