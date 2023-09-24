from datetime import datetime
import requests
import json
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class NotFoundPlayer(Exception):  # Исключение о том, что игрок не был найден
    pass

def driverRun(url=""):
    try:
        driver.get(url)
        driver.implicitly_wait(3)
        codeOfPage = driver.page_source
        soup = BeautifulSoup(codeOfPage, 'html.parser')
        some = soup.find("pre").text
        return some
    except Exception as ex:
        print(ex)
        return None



def getJsonInfoOfPlayer(id=0):  # Запрос информации об игроке
    try:
        jsonReqPlayer = json.loads(driverRun('https://swgoh.gg/api/player/' + str(id)))
        return jsonReqPlayer
    except:
        return None


def getInfoAboutGuild(id=''):  # Запрос информации о гильдии
    try:
        jsonReqGuild = json.loads(driverRun('https://swgoh.gg/api/guild-profile/' + id))
        return jsonReqGuild['data']['members']
    except:
        return None


# Получение информации по всем игрокам из гильдии
def getInfoAboutAllPlayers(allyCodes=[]):
    dictOfPlayers = {}
    for allyCode in allyCodes:
        dictWithGalacticPowerAndUnits = {}
        jsonReqPlayer = getJsonInfoOfPlayer(id=allyCode)
        dictWithGalacticPowerAndUnits['galactic_power'] = jsonReqPlayer['data']['galactic_power']
        dictWithGalacticPowerAndUnits['units'] = jsonReqPlayer['units']
        dictOfPlayers[jsonReqPlayer['data']['name']
                      ] = dictWithGalacticPowerAndUnits
    return dictOfPlayers

def getAllUnitsFromGame():
    try:
        jsonReqUnits = json.loads(driverRun('https://swgoh.gg/api/characters'))
        arrayUnits = []
        for unit in jsonReqUnits:
            arrayUnits.append(unit['name'])
        return arrayUnits
    except:
        return None

def getValidString(stringConfig=""):
    myString = ""
    if (stringConfig.find(':')==stringConfig.rfind(':')) and stringConfig.find(':')!=-1:
        i = 0
        while stringConfig[i] == ' ':
            i+=1
        while stringConfig[i] != ':':
            myString+=stringConfig[i]
            i+=1
        i-=1
        i = len(myString)-1
        while myString[i] == ' ':
            i-=1
        myString=myString[:i+1]
        i = stringConfig.find(':')
        myString+=stringConfig[i]
        i+=1
        while stringConfig[i] == ' ':
            i+=1
        while i < len(stringConfig):
            myString+=stringConfig[i]
            i+=1
        i = len(myString)-1
        while myString[i] == ' ':
            i-=1
        myString=myString[:i+1]
        return myString
    else: return 'InvalidString'

# Записываем все данные в Excel
def writeDataIntoExcelTable(dictOfPlayers={}, path=""):
    f = open('config_units.txt', 'r', encoding='UTF-8')
    data = f.read()
    unitsTuple = []
    for unit in data.split('\n'):
        unit = getValidString(stringConfig=unit)
        if unit != 'InvalidString':
            if unit not in unitsTuple:
                if unit != "": unitsTuple.append(unit)
    
    # Create a workbook and add a worksheet.
    # workbook = xlsxwriter.Workbook(path + 'statistics_'+ datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+ '.xlsx')
    workbook = xlsxwriter.Workbook('Units.xlsx')
    writeDataToSheet(workbook=workbook, dictOfPlayers=dictOfPlayers, unitsTuple=unitsTuple)
    arrayUnits = getAllUnitsFromGame()
    if arrayUnits:
        writeDataToSheet(workbook=workbook, dictOfPlayers=dictOfPlayers, unitsTuple=arrayUnits)
    workbook.close()

def writeDataToSheet(workbook, dictOfPlayers, unitsTuple):
    worksheet = workbook.add_worksheet()
    cell_format_style =workbook.add_format()
    cell_format_style.set_pattern(1)
    cell_format_style.set_border(style=1)
    cell_format_style.set_bg_color('#ffffff')
    cell_format_style.set_align('center')


    cell_format_yellow = workbook.add_format()
    cell_format_yellow.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_yellow.set_bg_color('#ffff00')
    cell_format_yellow.set_border(style=1)
    cell_format_yellow.set_align('center')

    cell_format_green = workbook.add_format()
    cell_format_green.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_green.set_bg_color('#92d050')
    cell_format_green.set_border(style=1)
    cell_format_green.set_align('center')

    cell_format_darkgreen = workbook.add_format()
    cell_format_darkgreen.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_darkgreen.set_bg_color('#00b050')
    cell_format_darkgreen.set_border(style=1)
    cell_format_darkgreen.set_align('center')

    cell_format_pink = workbook.add_format()
    cell_format_pink.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_pink.set_bg_color('#fde9d9')
    cell_format_pink.set_border(style=1)
    cell_format_pink.set_align('center')

    cell_format_blue = workbook.add_format()
    cell_format_blue.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_blue.set_bg_color('#00b0f0')
    cell_format_blue.set_border(style=1)
    cell_format_blue.set_align('center')

    cell_format_orange = workbook.add_format()
    cell_format_orange.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_orange.set_bg_color('#FF6600')
    cell_format_orange.set_border(style=1)
    cell_format_orange.set_align('center')

    cell_format_lightgreen = workbook.add_format()
    cell_format_lightgreen.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_lightgreen.set_bg_color('#c4d79b')
    cell_format_lightgreen.set_border(style=1)
    cell_format_lightgreen.set_align('center')

    cell_format_red = workbook.add_format({'num_format':"#,##0", 'bold': True})
    cell_format_red.set_pattern(1)
    cell_format_red.set_border(style=1)
    cell_format_red.set_bg_color('#ffffff')
    cell_format_red.set_align('center')

    cell_format_num = workbook.add_format({'num_format':"#,##0"})
    cell_format_num.set_pattern(1)
    cell_format_num.set_border(style=1)
    cell_format_num.set_bg_color('#ffffff')
    cell_format_num.set_align('center')


    worksheet.set_column(3,len(unitsTuple)+2, 7)
    worksheet.set_column('A:A', 3)
    worksheet.set_column('C:C', 13)
    row = 0
    col = 0

    worksheet.write(row, col, '№',cell_format_style)
    col += 1
    worksheet.write(row, col, 'Nickname',cell_format_style)
    col += 1
    worksheet.write(row, col, 'Galactic power',cell_format_style)
    col += 1
    for unit in unitsTuple:
        unit = unit.split(':')
        if len(unit)>1:
            worksheet.write(row, col, unit[1], cell_format_style)
        else:
            worksheet.write(row, col, unit[0], cell_format_style) 
        col += 1
    
    row += 1
    col = 0
    maxLengthNickname = 0
    legendCount = 0
    for player in dictOfPlayers.keys():
        if (len(player)>maxLengthNickname): maxLengthNickname = len(player)
        worksheet.write(row, col, row,cell_format_style)
        col += 1
        worksheet.write(row, col, player,cell_format_style)
        col += 1
        worksheet.write(row, col, dictOfPlayers[player]['galactic_power'],cell_format_num ) 
        col += 1
        for unit in unitsTuple:
            unit = unit.split(':')[0]
            try:
                if dictOfPlayers[player]['units'][unit]['galactic_legend']: legendCount += 1
                if getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) =='13+9' : 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_orange)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '13+8' : 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_blue)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '13+7' : 
                   worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_darkgreen)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) in ['13+4','13+5','13+6','13+3','13+2','13+1','13'] : 
                   worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_green)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '12': 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_lightgreen)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '11': 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_yellow)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) !=0 :
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit), cell_format_pink)
            except:
                worksheet.write(row, col, 'Нет', cell_format_pink)
            col += 1
        row += 1
        col=0
    if maxLengthNickname<5:
        worksheet.set_column('B:B', maxLengthNickname)
    else:
        worksheet.set_column('B:B', maxLengthNickname-2)
    worksheet.write(row, col, 'Лег', cell_format_red)
    worksheet.write(row, col+1, legendCount, cell_format_red)
    worksheet.write_formula(row, col+2, '=sum(C2:C%s' % str(len(dictOfPlayers)+1) + ')', cell_format_red)
    col += 3
    for i in range(3, len(unitsTuple)+3):
        diapazon = chr(ord('A')+i) if (i //
                                    26) < 1 else chr(ord('A')+((i//26)-1)) + chr(ord('A')+((i%26)))
        worksheet.write_formula(row, col, '=COUNTIF(' + diapazon + str(2) + ':' + diapazon + str(len(dictOfPlayers)+1) +',"<>Нет")', cell_format_red)
        col+=1


        


def getStringOfGearAndRelic(dictOfPlayers={}, player='', unit=''):
    gearLvl = dictOfPlayers[player]['units'][unit]['gear_level']
    if gearLvl == 13:
        return str(gearLvl) + '+' + str(dictOfPlayers[player]['units'][unit]['relic_tier'])
    else:
        stars = dictOfPlayers[player]['units'][unit]['stars']
        if stars == 7:
            return str(gearLvl)
        else:
            return str(gearLvl) + '(' + str(stars) +'*)'


def arrOfUnitsToDict(units=[]):  # Массив персонажей переделываем в словарь
    dictOfUnits = {}
    for unit in units:
        gearLvl = unit['data']['gear_level']
        lvlOfUnit = {}
        lvlOfUnit['gear_level'] = gearLvl
        lvlOfUnit['relic_tier'] = unit['data']['relic_tier']-2
        lvlOfUnit['stars'] = unit['data']['rarity']
        lvlOfUnit['galactic_legend'] = unit['data']['is_galactic_legend']
        dictOfUnits[unit['data']['name']] = lvlOfUnit
    return dictOfUnits


def getInfoFromSWGOH(id=0, needGuild=False, pathForSave=""):  # Основная функция
    global driver
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    driver = webdriver.Chrome('resources\chromedriver\chromedriver.exe', options=options)
    jsonPlayerInfo = getJsonInfoOfPlayer(id=id)
    if jsonPlayerInfo != None:
        dictOfPlayers = {}
        if needGuild:
            allyCodes = []
            members = getInfoAboutGuild(jsonPlayerInfo['data']['guild_id'])
            for member in members:
                allyCodes.append(member['ally_code'])
            dictOfPlayers = getInfoAboutAllPlayers(allyCodes=allyCodes)
        else:
            dictWithGalacticPowerAndUnits = {}
            dictWithGalacticPowerAndUnits['galactic_power'] = jsonPlayerInfo['data']['galactic_power']
            dictWithGalacticPowerAndUnits['units'] = jsonPlayerInfo['units']
            dictOfPlayers[jsonPlayerInfo['data']
                          ['name']] = dictWithGalacticPowerAndUnits
        for key in dictOfPlayers.keys():
            dictOfPlayers[key]['units'] = arrOfUnitsToDict(
                dictOfPlayers[key]['units'])
        print(dictOfPlayers)
        dictOfPlayers = sortDictByGalacticPower(dictPlayers=dictOfPlayers)
        writeDataIntoExcelTable(dictOfPlayers=dictOfPlayers, path=pathForSave)
        driver.close()
        driver.quit()
        return 0
    else:
        driver.close()
        driver.quit()
        raise NotFoundPlayer("Мы не смогли найти игрока")


def sortDictByGalacticPower(dictPlayers = {}):
    values = list(dictPlayers.values())
    for i in range(len(values)-1):
        for j in range(i, len(values)):
            if values[i]['galactic_power']<values[j]['galactic_power']: values[i],values[j] = values[j],values[i]
    newDict = {}
    for value in values:
        for player in dictPlayers.keys():
            if dictPlayers[player]['galactic_power'] == value['galactic_power']:
                newDict[player]=dictPlayers[player]
    return newDict

def main():
    # id = int(input('Enter id: '))
    # print("You need mana?")
    # needGuild = False
    # if (input().lower().find("y") != -1):
    #     needGuild = True
    try:
        getInfoFromSWGOH(id=785425257, needGuild=False)
    except Exception as ex:
        print(ex)



if __name__ == "__main__":
    main()
