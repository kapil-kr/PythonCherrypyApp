import csv
import zipfile, urllib.request, shutil
from datetime import date, timedelta


def GetfileName():    
    yesterday = date.today() - timedelta(1)
    str = yesterday.strftime('%d%m%y')
    #sample: EQ130618_CSV.ZIP'
    #fName = 'EQ'+da + mo + str(now.year%100)+'_CSV.ZIP'
    fName = 'EQ' + str + '_CSV.ZIP'
    return fName



def downloadFile():
    fileName = GetfileName()
    url = 'https://www.bseindia.com/download/BhavCopy/Equity/' + fileName
    #print(url)
    #url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ130618_CSV.ZIP'
    with urllib.request.urlopen(url) as response, open(fileName, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        with zipfile.ZipFile(fileName) as zf:
            zf.extractall()

  
def fileReader():
    equityFN = GetfileName()
    fields = []
    rows = []
    with open(equityFN, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows,fields
        #print("Total no. of rows: %d"%(csvreader.line_num))
 
downloadFile()
# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))
 
#  printing first 5 rows
#print('\nFirst 5 rows are:\n')
#for row in rows[:5]:
    # parsing each column of a row
#    for col in row:
#        print("%10s"%col),
#    print('\n')

#print(rows[:5])