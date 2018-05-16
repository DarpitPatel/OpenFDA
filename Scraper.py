import requests
import csv
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import sys
import sklearn.metrics

count = 1
start_date = []
end_date = []
f = open('output.txt', 'w')
csv = open('output.csv', "w") 
medicinename= sys.argv[1]


while count < 10:
    
  skip=1000*count
  URL = 'https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:'+medicinename+'&limit=100&skip='+str(skip)
  data = requests.get(URL).json()
  
  for result in data.get('results', []):


    row=""
    bin2int=""
    if('medicinalproduct' in str(result['patient']['drug'][0])):
        medicinalproduct=result['patient']['drug'][0]['medicinalproduct']
        f.write('medicinalproduct|') 
        f.write(medicinalproduct)
        f.write('|')
        row += medicinalproduct + ","        
    else:
      continue
    if('patientsex' in str(result['patient'])):
        patientsex=result['patient']['patientsex']
        f.write('patientsex|') 
        f.write(patientsex)
        f.write('|')
        row += patientsex + ","
    else:
      continue
    if(('patientonsetage' in str(result['patient'])) and (str(result['patient']['patientonsetage']) != 'None')):
        patientonsetage=result['patient']['patientonsetage']
        f.write('patientonsetage| ') 
        f.write(str(patientonsetage))
        f.write('|')
        row += str(patientonsetage) + ","
    else:
      continue
    if('seriousnessdeath' in str(result)):
        seriousnessdeath= result['seriousnessdeath']
        f.write('seriousnessdeath|')        
        f.write(seriousnessdeath)
        f.write('|')
        row += seriousnessdeath + ","
        bin2int += seriousnessdeath
    else:
        f.write('seriousnessdeath|')        
        f.write('0')
        f.write('|')
        row += "0" + ","
        bin2int += "0"
    if('seriousnessdisabling' in str(result)):
        seriousnessdisabling= result['seriousnessdisabling']
        f.write('seriousnessdisabling|')        
        f.write(seriousnessdisabling)
        f.write('|')
        row += seriousnessdisabling + ","
        bin2int += seriousnessdisabling
    else:
        f.write('seriousnessdisabling|')        
        f.write('0')
        f.write('|')
        row += "0" + ","
        bin2int += "0"
    if('seriousnesshospitalization' in str(result)):
        seriousnesshospitalization= result['seriousnesshospitalization']
        f.write('seriousnesshospitalization|')        
        f.write(seriousnesshospitalization)
        f.write('|')
        row += seriousnesshospitalization + ","
        bin2int += seriousnesshospitalization
    else:
        f.write('seriousnesshospitalization|')        
        f.write('0')
        f.write('|')
        row += "0" + ","
        bin2int += "0"
    if('seriousnesslifethreatening' in str(result)):
        seriousnesslifethreatening= result['seriousnesslifethreatening']
        f.write('seriousnesslifethreatening|')        
        f.write(seriousnesslifethreatening)
        f.write('|')
        row += seriousnesslifethreatening + ","
        bin2int += seriousnesslifethreatening
    else:
        f.write('seriousnesslifethreatening|')        
        f.write('0')
        f.write('|')
        row += "0" + ","
        bin2int += "0"
    if('seriousnessother' in str(result)):
        seriousnessother= result['seriousnessother']
        f.write('seriousnessother|')        
        f.write(seriousnessother)
        f.write('|')
        row += seriousnessother + ","
        bin2int += seriousnessother
    else:
        f.write('seriousnessother|')        
        f.write('0')
        f.write('|')
        row += "0" + ","
        bin2int += "0"

    
    csv.write(row)
    csv.write(str(int(bin2int, 2)))
    f.write('\n')    
    csv.write('\n') 
  count=count+1
  
f.close();
csv.close();
