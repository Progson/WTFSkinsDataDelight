from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

typeOfGame = "crash" 
typeOfData = "partial"

if len(sys.argv) >= 2:
    arg1 = sys.argv[1]
    if arg1 == "-crash" or arg1 == "-roulette":
        typeOfGame = arg1[1:]
    else:
        print("wrong argument used, use -crash or -roulette")
        sys.exit(0)
    if len(sys.argv) == 3:
        arg2 = sys.argv[2]
        if arg2 == "-full" or arg2 == "-partial":
            typeOfData = arg2[1:]
        else:
            print("wrong second argument used, use -full or -partial")
            sys.exit(0)
else:
    print("use argument -crash or -roulette")
    sys.exit(0)



nameOfFolder = "bets"

try:
    os.mkdir(nameOfFolder)
    print(f"Utworzono folder o nazwie '{nameOfFolder}'.")
except FileExistsError:
    print(f"Folder o nazwie '{nameOfFolder}' już istnieje.")
except Exception as e:
    print("Wystąpił błąd:", str(e))


sciezka_folderu = os.path.join(os.path.dirname(__file__), "bets")
driver = webdriver.Chrome()
HiBetNumber = 6546445

if typeOfData == "full" :
    url ="https://www.wtfskins.com/"+typeOfGame+"/history/round/"
else:
    url = "https://www.wtfskins.com/"+typeOfGame+"/history/"
    HiBetNumber = 10723




driver.get("https://www.wtfskins.com")
checkboxes = driver.find_elements(By.XPATH , '//input[@type="checkbox"]')
checkboxes[0].click()
checkboxes[1].click()
time.sleep(2)

reloads = 0
i = -1
while i < 20000:
    i+=1
    betNumber = HiBetNumber-i
    fullUrl = url + str(betNumber)
    driver.get(fullUrl)
    print("loading" + str(HiBetNumber-i))
    try:
        partOfxpathToControlElement = typeOfGame
        if(typeOfData == "full"):
            if(typeOfGame == "crash"):
                partOfxpathToControlElement += "-history"
            partOfxpathToControlElement += "-round/div/div[2]/table/tbody/tr[3]/td[2]"
        else:
            partOfxpathToControlElement += "-history/div/div/app-" + typeOfGame
            if(typeOfGame == "crash"):
                partOfxpathToControlElement += "-history"
            partOfxpathToControlElement += "-round-preview[1]/div/div[3]"

        elem = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div[1]/div/div/app-"+partOfxpathToControlElement)) )
        if elem:
            print(str(betNumber) + "sucses")
            try:
                reloads = 0
                filename = typeOfGame + "_"+typeOfData + "_"+ str(betNumber) + ".html"
                pelna_sciezka_pliku = os.path.join(sciezka_folderu, filename)
                
                
                with open(pelna_sciezka_pliku , "w") as plik:
                    plik.write(driver.page_source)
                print("file " + typeOfGame + str(betNumber) + ".html succesfully saved")
            except Exception as e:
                print("writting error", str(e))
            
    except  Exception as e:
        print("loading error at " + str(betNumber))
        if reloads < 8 and i>0:
            reloads +=1
            print("reload " + str(reloads))
            i-=1
    
 
driver.quit()
