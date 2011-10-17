#!/usr/bin/env python

import csv
import string

mergeFile = open('m2list.csv', 'rU')   # Open old Clinic database.
mergeList = list(csv.reader(mergeFile, delimiter=',', quotechar='"'))   # Cast csv read to list.
mergeFile.close()


numFP = 0
numI = 0
numPD = 0
numAI = 0
numC = 0
numCD = 0
numD = 0
numEND = 0
numOTO = 0   # Ear, Nose, and Throat (Otolaryngology) -- Otology,Laryngology,Rhinology
numGE = 0
numGS = 0
numHEM = 0
numONC = 0
numID = 0
numNEP = 0
numN = 0
numOBG = 0
numOM = 0
numOPH = 0
numORS = 0   # Orthopedic Surgery. Orthopedics is not in OBME.
numPMR = 0
numDPM = 0   # Podiatry
numP = 0
numPY = 0   # Psychoanalysis or Psychosomatic Medicine
numPUD = 0
numRHU = 0
numSLM = 0   # Sleep Medicine (abbrv. made up)
numUC = 0   # Urgent Care (abbrv. made up)
numU = 0

total = 0 

for mergeRow in mergeList:
    spList = [s.strip() for s in mergeRow[10].split(',')]
    for specialty in spList:
        if specialty == 'Family Practice': numFP += 1
        if specialty == 'Internal Medicine': numI += 1
        if specialty == 'Pediatrics': numPD += 1
        if specialty == 'Allergy and Immunology': numAI += 1
        if specialty == 'Cardiology': numC += 1
        if specialty == 'Cardiovascular Diseases': numCD += 1
        if specialty == 'Dermatology': numD += 1
        if specialty == 'Endocrinology': numEND += 1
        if specialty == ('Otology' or 'Laryngology' or 'Rhinology'): numOTO += 1
        if specialty == 'Gastroenterology': numGE += 1
        if specialty == 'General Surgery': numGS += 1
        if specialty == 'Hematology': numHEM += 1
        if specialty == 'Oncology': numONC += 1
        if specialty == 'Infectious Diseases': numID += 1
        if specialty == 'Nephrology': numNEP += 1
        if specialty == 'Neurology': numN += 1
        if specialty == 'Obstetrics and Gynecology': numOBG += 1
        if specialty == 'Occupational Medicine': numOM += 1
        if specialty == 'Ophthalmology': numOPH += 1
        if specialty == 'Orthopedic Surgery': numORS += 1
        if specialty == 'Physical Medicine & Rehabilitation': numPMR += 1
        if specialty == 'Podiatry': numDPM += 1
        if specialty == 'Psychiatry': numP += 1
        if specialty == 'Psychoanalysis' or specialty == 'Psychosomatic Medicine': numPY += 1
        if specialty == 'Pulmonary Diseases': numPUD += 1
        if specialty == 'Rheumatology': numRHU += 1
        if specialty == 'Sleep Medicine': numSLM += 1
        if specialty == 'Urgent Care': numUC += 1
        if specialty == 'Urology': numU += 1

print 'FP : %s' % (numFP)
print 'I  : %s' % (numI)
print 'PD : %s' % (numPD)

print 'Total Primary:', numFP+numI+numPD, '\n'

print 'AI     : %s' % (numAI)
print 'C      : %s' % (numC)
print 'CD     : %s' % (numCD)
print 'D      : %s' % (numD)
print 'END    : %s' % (numEND)
print 'OTO    : %s' % (numOTO)
print 'GE     : %s' % (numGE)
print 'GS     : %s' % (numGS)
print 'HEM/ONC: %s' % (numHEM+numONC)
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

total = numFP + numI + numPD + numAI + numC + numCD + numD + numEND + numOTO + numGE + numGS + numHEM + numONC + numID + numNEP + numN + numOBG + numOM + numOPH + numORS + numPMR + numDPM + numP + numPY + numPUD + numRHU + numSLM + numUC + numU

print 'Total Specialty:', total - (numFP+numI+numPD), '\n'

print 'Total:', total

