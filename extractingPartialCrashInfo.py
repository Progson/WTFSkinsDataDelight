import re
import sys
import os

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

nameOfFolder = "bets"
NumberOfPages = 20000
lostPages = 0

filename = "data.csv"
pathToFolderWithWebsites = os.path.join(os.path.dirname(__file__), "bets")
pathToFileWithData = filename

with open(pathToFileWithData, "w", encoding="utf-8") as file:
    pass 

#finding lines with interesting data
#371 first bet number 371+3 month 374+3 377 mult 380 date 
#+6 next betnumber

#in some of them first number is 443
firstLine = 370
firstLineInWeirdFiles = 442
dataPattern = r'\d+,\d+,x\d+(\.\d+)?,\d+.\d{2}.\d{4},\d{2}:\d{2}:\d{2}'

for page in range(NumberOfPages+1):
    if(page == 0):
        continue
    nameOfHtmlFile = "\crash_partial_"+ str(page) + ".html"
    try:
        with open(pathToFolderWithWebsites + nameOfHtmlFile, "r", encoding="iso-8859-1") as input_file:
            dataToSave = ""
            lines = input_file.readlines()
            line = firstLine
            for j in range (50):
                selected_line1 = lines[line]
                line+=6
                selected_line2 = lines[line]
                line+=3
                selected_line3 = lines[line]
                line+=6
                dataOfOneBet = str(page) + "," +selected_line1 + ","+selected_line2 + ","+selected_line3
                dataOfOneBet = re.sub(r'\s+', '', dataOfOneBet).strip()
                if not(re.fullmatch(dataPattern, dataOfOneBet)):
                    line = firstLineInWeirdFiles
                    selected_line1 = lines[line]
                    line+=6
                    selected_line2 = lines[line]
                    line+=3
                    selected_line3 = lines[line]
                    dataOfOneBet = str(page) + "," +selected_line1 + ","+selected_line2 + ","+selected_line3
                    dataOfOneBet = re.sub(r'\s+', '', dataOfOneBet).strip()
                if not(re.fullmatch(dataPattern, dataOfOneBet)):
                    print(dataOfOneBet)
                    lostPages +=1
                dataToSave += dataOfOneBet + "\n"
            try:
                with open(pathToFileWithData , "a" , encoding="utf-8") as plik:
                    plik.write(dataToSave)
                    print(dataToSave + color_text("\n------------------------------------->",33) + color_text("sucessfuly saved",32))
            except Exception as e:
                print("writting error", str(e))
                
    except Exception as e:
        print("file opening error", str(e))
print("number of lost pages:" + str(lostPages))
sys.exit(1)
