from datetime import datetime
import requests
import json
import xlsxwriter
from pysondb import db
from time import sleep
from transliterate import translit
from xlsx2html import xlsx2html


def has_russian_letters(word):
    for letter in word:
        if 'а' <= letter <= 'я' or 'А' <= letter <= 'Я':
            return True
    return False


class NotFoundPlayer(Exception):  # Исключение о том, что игрок не был найден
    pass


def driverRun(url=""):
    try:
        user_agent = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        return requests.get(url, headers=user_agent).text
    except Exception as ex:
        print(ex)
        return None


def getJsonInfoOfPlayer(id=0):  # Запрос информации об игроке
    try:
        a = db.getDb("db_main.json")
        jsonReqPlayer = json.loads(driverRun(a.getByQuery({"name": "api"})[0]["value"] +
                                             a.getByQuery({"name": "player"})[0]["value"] + str(id)))
        jsonNotFoundPlayer = json.loads("""{"detail":"Not found."}""")
        if jsonReqPlayer == jsonNotFoundPlayer:
            return False
        else:
            return jsonReqPlayer
    except:
        return None


def getInfoAboutGuild(id=''):  # Запрос информации о гильдии
    try:
        a = db.getDb("db_main.json")
        jsonReqGuild = json.loads(driverRun(a.getByQuery({"name": "api"})[0]["value"] +
                                            a.getByQuery({"name": "guild"})[0]["value"] + id))
        return jsonReqGuild['data']['members']
    except:
        return None


# Получение информации по всем игрокам из гильдии
def getInfoAboutAllPlayers(allyCodes=[]):
    dictOfPlayers = {}
    fixedAllyCodes = []
    a = db.getDb("db_config.json")
    doc_type = a.getByQuery({"type": "extension"})[0]["data"]
    for code in allyCodes:
        if str(code) == "None":
            continue
        fixedAllyCodes.append(code)

    for allyCode in fixedAllyCodes:
        dictWithGalacticPowerAndUnits = {}
        jsonReqPlayer = getJsonInfoOfPlayer(id=allyCode)
        dictWithGalacticPowerAndUnits['galactic_power'] = jsonReqPlayer['data']['galactic_power']
        dictWithGalacticPowerAndUnits['units'] = jsonReqPlayer['units']

        if has_russian_letters(jsonReqPlayer['data']['name']) and doc_type == "html":
            dictOfPlayers[translit(jsonReqPlayer['data']['name'], language_code='ru', reversed=True)
            ] = dictWithGalacticPowerAndUnits
        else:
            dictOfPlayers[jsonReqPlayer['data']['name']
            ] = dictWithGalacticPowerAndUnits
    return dictOfPlayers


def getAllUnitsFromGame():
    try:
        a = db.getDb("db_main.json")
        jsonReqUnits = json.loads(driverRun(a.getByQuery({"name": "api"})[0]["value"] +
                                            a.getByQuery({"name": "characters"})[0]["value"]))
        arrayUnits = []
        for unit in jsonReqUnits:
            arrayUnits.append(unit['name'])
        return arrayUnits
    except:
        return None


def getValidString(stringConfig=""):
    myString = ""
    if (stringConfig.find(':') == stringConfig.rfind(':')) and stringConfig.find(':') != -1:
        i = 0
        while stringConfig[i] == ' ':
            i += 1
        while stringConfig[i] != ':':
            myString += stringConfig[i]
            i += 1
        i -= 1
        i = len(myString) - 1
        while myString[i] == ' ':
            i -= 1
        myString = myString[:i + 1]
        i = stringConfig.find(':')
        myString += stringConfig[i]
        i += 1
        while stringConfig[i] == ' ':
            i += 1
        while i < len(stringConfig):
            myString += stringConfig[i]
            i += 1
        i = len(myString) - 1
        while myString[i] == ' ':
            i -= 1
        myString = myString[:i + 1]
        return myString
    else:
        return 'InvalidString'


# Записываем все данные в Excel
def writeDataIntoExcelTable(dictOfPlayers={}, path=""):
    a = db.getDb("db_config.json")
    req = a.getByQuery({"type": "presets"})
    # print(dictOfPlayers.keys())
    presets = []
    if req:
        presets = req[0]["data"]

    if presets:
        active = next((item for item in presets if item["active"]), None)
        if active:
            all_units = active["data"]
        else:
            all_units = presets[0]["data"]

        unitsTuple = [unit["name"] for unit in all_units if unit["type"] == "unit"]
        # Create a workbook and add a worksheet.
        full_path = path + 'statistics_' + datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        workbook = xlsxwriter.Workbook(full_path + '.xlsx')
        writeDataToSheet(workbook=workbook, dictOfPlayers=dictOfPlayers, unitsTuple=unitsTuple)
        arrayUnits = getAllUnitsFromGame()
        if arrayUnits:
            writeDataToSheet(workbook=workbook, dictOfPlayers=dictOfPlayers, unitsTuple=arrayUnits)
        workbook.close()
        doc_type = a.getByQuery({"type": "extension"})[0]["data"]
        print(1)
        if doc_type == 'html':
            print(2)
            xlsx2html(full_path + '.xlsx', full_path + '.html')
            print(3)
    else:
        raise Exception()


def writeDataToSheet(workbook, dictOfPlayers, unitsTuple):
    orange = "#ff6600"
    blue = "#00b0f0"
    darkgreen = "#00b050"
    green = "#92d050"
    lightgreen = "#c4d79b"
    yellow = "#ffff00"
    pink = "#fde9d9"

    a = db.getDb("db_config.json")
    req = a.getByQuery({"type": "colors"})
    if req:
        colors = req[0]["data"]
        orange = next((item["hex"] for item in colors if item["name"] == "orange"), orange)
        blue = next((item["hex"] for item in colors if item["name"] == "blue"), blue)
        darkgreen = next((item["hex"] for item in colors if item["name"] == "darkgreen"), darkgreen)
        green = next((item["hex"] for item in colors if item["name"] == "green"), green)
        lightgreen = next((item["hex"] for item in colors if item["name"] == "lightgreen"), lightgreen)
        yellow = next((item["hex"] for item in colors if item["name"] == "yellow"), yellow)
        pink = next((item["hex"] for item in colors if item["name"] == "pink"), pink)

    worksheet = workbook.add_worksheet()
    cell_format_style = workbook.add_format()
    cell_format_style.set_pattern(1)
    cell_format_style.set_border(style=1)
    cell_format_style.set_bg_color('#ffffff')
    cell_format_style.set_align('center')

    cell_format_yellow = workbook.add_format()
    cell_format_yellow.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_yellow.set_bg_color(yellow)
    cell_format_yellow.set_border(style=1)
    cell_format_yellow.set_align('center')

    cell_format_green = workbook.add_format()
    cell_format_green.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_green.set_bg_color(green)
    cell_format_green.set_border(style=1)
    cell_format_green.set_align('center')

    cell_format_darkgreen = workbook.add_format()
    cell_format_darkgreen.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_darkgreen.set_bg_color(darkgreen)
    cell_format_darkgreen.set_border(style=1)
    cell_format_darkgreen.set_align('center')

    cell_format_pink = workbook.add_format()
    cell_format_pink.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_pink.set_bg_color(pink)
    cell_format_pink.set_border(style=1)
    cell_format_pink.set_align('center')

    cell_format_blue = workbook.add_format()
    cell_format_blue.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_blue.set_bg_color(blue)
    cell_format_blue.set_border(style=1)
    cell_format_blue.set_align('center')

    cell_format_orange = workbook.add_format()
    cell_format_orange.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_orange.set_bg_color(orange)
    cell_format_orange.set_border(style=1)
    cell_format_orange.set_align('center')

    cell_format_lightgreen = workbook.add_format()
    cell_format_lightgreen.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_lightgreen.set_bg_color(lightgreen)
    cell_format_lightgreen.set_border(style=1)
    cell_format_lightgreen.set_align('center')

    cell_format_red = workbook.add_format({'num_format': "#,##0", 'bold': True})
    cell_format_red.set_pattern(1)
    cell_format_red.set_border(style=1)
    cell_format_red.set_bg_color('#ffffff')
    cell_format_red.set_align('center')

    cell_format_num = workbook.add_format({'num_format': "#,##0"})
    cell_format_num.set_pattern(1)
    cell_format_num.set_border(style=1)
    cell_format_num.set_bg_color('#ffffff')
    cell_format_num.set_align('center')

    worksheet.set_column(3, len(unitsTuple) + 2, 7)
    worksheet.set_column('A:A', 3)
    worksheet.set_column('C:C', 13)
    row = 0
    col = 0

    worksheet.write(row, col, 'N', cell_format_style)
    col += 1
    worksheet.write(row, col, 'Nickname', cell_format_style)
    col += 1
    worksheet.write(row, col, 'GP', cell_format_style)
    col += 1
    a = db.getDb("db_config.json")
    doc_type = a.getByQuery({"type": "extension"})[0]["data"]
    for unit in unitsTuple:
        unit = unit.split(':')
        if len(unit) <= 1:
            worksheet.write(row, col, unit[0], cell_format_style)
        else:
            if has_russian_letters(unit[1]) and doc_type == 'html':
                unit[1] = translit(unit[1], language_code='ru', reversed=True)
            worksheet.write(row, col, unit[1], cell_format_style)
        col += 1

    row += 1
    col = 0
    maxLengthNickname = 0
    legendCount = 0
    global_galactic_power = 0
    crutoe_chislo_123 = [0] * len(unitsTuple)
    for player in dictOfPlayers.keys():
        counter = -1
        if (len(player) > maxLengthNickname): maxLengthNickname = len(player)
        worksheet.write(row, col, row, cell_format_style)
        col += 1
        worksheet.write(row, col, player, cell_format_style)
        col += 1
        worksheet.write(row, col, dictOfPlayers[player]['galactic_power'], cell_format_num)
        global_galactic_power += dictOfPlayers[player]['galactic_power']
        col += 1
        for unit in unitsTuple:
            counter += 1
            unit = unit.split(':')[0]
            try:
                if dictOfPlayers[player]['units'][unit]['galactic_legend']:
                    legendCount += 1

                value = getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit)
                if (value.partition('+')[1] == '+' and
                        int(value.partition('+')[0]) >= 13 and
                        int(value.partition('+')[2]) >= 9):
                    worksheet.write(row, col, value, cell_format_orange)
                elif value == '13+8':
                    worksheet.write(row, col, value, cell_format_blue)
                elif value == '13+7':
                    worksheet.write(row, col, value, cell_format_darkgreen)
                elif value in ['13+6', '13+5', '13+4', '13+3', '13+2', '13+1']:
                    worksheet.write(row, col, value, cell_format_green)
                elif value in ['12', '13', '13+0']:
                    worksheet.write(row, col, value, cell_format_lightgreen)
                elif value.partition('(')[0].rstrip() == '11':
                    worksheet.write(row, col, value, cell_format_yellow)
                elif value != 0:
                    worksheet.write(row, col, value, cell_format_pink)
                crutoe_chislo_123[counter] += 1
            except:
                if doc_type == 'html':
                    worksheet.write(row, col, 'No', cell_format_pink)
                else:
                    worksheet.write(row, col, 'Нет', cell_format_pink)
            col += 1
        row += 1
        col = 0
    if maxLengthNickname < 5:
        worksheet.set_column('B:B', maxLengthNickname)
    else:
        worksheet.set_column('B:B', maxLengthNickname - 2)
    if doc_type == 'html':
        worksheet.write(row, col, 'Leg', cell_format_red)
    else:
        worksheet.write(row, col, 'Лег', cell_format_red)
    worksheet.write(row, col + 1, str(legendCount), cell_format_red)
    worksheet.write(row, col + 2, format_number(global_galactic_power), cell_format_red)
    col += 3
    counter_2 = 0
    for i in range(3, len(unitsTuple) + 3):
        diapazon = chr(ord('A') + i) if (i //
                                         26) < 1 else chr(ord('A') + ((i // 26) - 1)) + chr(ord('A') + ((i % 26)))
        worksheet.write(row, col, crutoe_chislo_123[counter_2], cell_format_red)
        col += 1
        counter_2+=1


def format_number(n):
    return '{:,}'.format(n)


def getStringOfGearAndRelic(dictOfPlayers={}, player='', unit=''):
    gearLvl = dictOfPlayers[player]['units'][unit]['gear_level']
    if gearLvl == 13:
        return str(gearLvl) + '+' + str(dictOfPlayers[player]['units'][unit]['relic_tier'])
    else:
        stars = dictOfPlayers[player]['units'][unit]['stars']
        if stars == 7:
            return str(gearLvl)
        else:
            return str(gearLvl) + '(' + str(stars) + '*)'


def arrOfUnitsToDict(units=[]):  # Массив персонажей переделываем в словарь
    dictOfUnits = {}
    for unit in units:
        gearLvl = unit['data']['gear_level']
        lvlOfUnit = {}
        lvlOfUnit['gear_level'] = gearLvl
        lvlOfUnit['relic_tier'] = unit['data']['relic_tier'] - 2
        lvlOfUnit['stars'] = unit['data']['rarity']
        lvlOfUnit['galactic_legend'] = unit['data']['is_galactic_legend']
        dictOfUnits[unit['data']['name']] = lvlOfUnit
    return dictOfUnits


def getInfoFromAPI(id=0, needGuild=False, pathForSave=""):  # Основная функция
    jsonPlayerInfo = getJsonInfoOfPlayer(id=id)
    if jsonPlayerInfo:
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
        dictOfPlayers = sortDictByGalacticPower(dictPlayers=dictOfPlayers)
        writeDataIntoExcelTable(dictOfPlayers=dictOfPlayers, path=pathForSave)
        print(4)
        return 0
    elif jsonPlayerInfo != None:
        raise NotFoundPlayer("Мы не смогли найти игрока")
    else:
        raise Exception


def sortDictByGalacticPower(dictPlayers={}):
    values = list(dictPlayers.values())
    for i in range(len(values) - 1):
        for j in range(i, len(values)):
            if values[i]['galactic_power'] < values[j]['galactic_power']: values[i], values[j] = values[j], values[i]
    newDict = {}
    for value in values:
        for player in dictPlayers.keys():
            if dictPlayers[player]['galactic_power'] == value['galactic_power']:
                newDict[player] = dictPlayers[player]
    return newDict


def main():
    try:
        getInfoFromAPI(id=785425257, needGuild=False)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
