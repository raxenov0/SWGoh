from gui import *
from api_parser import getInfoFromAPI, NotFoundPlayer
import threading
import sys
import os


class ParserThread(QThread):
    def __init__(self, id, needGuild, pathForSave, mainWindow):
        super().__init__()
        self.PlayerId = id or "000000000"
        self.PlayerNeedGuild = needGuild
        self.PlayerPathForSave = pathForSave
        self.window = mainWindow

    exception = pyqtSignal()
    notFound = pyqtSignal()
    completed = pyqtSignal()

    def run(self):
        print('run')
        try:
            getInfoFromAPI(
                id=self.PlayerId, needGuild=self.PlayerNeedGuild, pathForSave=self.PlayerPathForSave)
            killResources(ui=self.window)
            self.window.checkBox_2.setChecked(False)
            # self.window.show_popup_success()
            # self.window.progressBar.setValue(0)
            self.completed.emit()
        except NotFoundPlayer as ex:
            self.notFound.emit()
        except Exception as ex:
            self.exception.emit()


class GuiThread(threading.Thread):
    def __init__(self, mainWindow):
        super().__init__()
        self.window = mainWindow

    def run(self):
        print('run')
        self.exception = None
        self.window.startProgressBar()


def killResources(ui):
    ui.thread1.stop()
    ui.thread2.stop()
    ui.pushButton.setEnabled(True)
    ui.pushButton_2.setEnabled(True)
    ui.lineEdit.setEnabled(True)
    ui.checkBox.setEnabled(True)
    ui.checkBox_2.setChecked(False)


def swCall():
    myThread2 = ParserThread(id=ui.lineEdit.text().replace(
        '-', ''), needGuild=ui.checkBox.isChecked(), pathForSave=ui.lineEdit_2.text() + '/', mainWindow=ui)
    myThread2.start()
    myThread = GuiThread(mainWindow=ui)
    myThread2.completed.connect(swCallSuccess)
    myThread2.exception.connect(swCallExc)
    myThread2.notFound.connect(swCallNotFound)
    myThread.start()
    # time.sleep(2)
    # myThread2.join()
    # ui.show_popup_success()


def swCallSuccess():
    killResources(ui=ui)
    ui.progressBar.setValue(100)
    time.sleep(0.2)
    ui.show_popup_success()
    ui.progressBar.setValue(0)


def swCallExc():
    killResources(ui=ui)
    ui.show_popup_ex()
    ui.progressBar.setValue(0)


def swCallNotFound():
    killResources(ui=ui)
    ui.show_popup()
    ui.progressBar.setValue(0)


def setupDatabaseJSON():
    import json
    from pysondb import db

    with open('db_main.json') as inp:
        data = json.load(inp)

    if 'data' not in data:
        data['data'] = []
        with open('db_main.json', 'w') as output:
            json.dump(data, output)

    with open('db_config.json') as inp:
        data = json.load(inp)

    if 'data' not in data:
        data['data'] = []
        with open('db_config.json', 'w') as output:
            json.dump(data, output)

    a = db.getDb("db_config.json")
    data = a.getAll()

    colors = next((item['data'] for item in data if item['type'] == 'colors'), [])
    if not next((item for item in colors if item['name'] == 'orange'), False):
        colors.insert(0, {"name": "orange", "hex": "#ff6600", "value": "13+9 и выше", "type": "color"})
    if not next((item for item in colors if item['name'] == 'blue'), False):
        colors.insert(1, {"name": "blue", "hex": "#00b0f0", "value": "13+8", "type": "color"})
    if not next((item for item in colors if item['name'] == 'darkgreen'), False):
        colors.insert(2, {"name": "darkgreen", "hex": "#00b050", "value": "13+7", "type": "color"})
    if not next((item for item in colors if item['name'] == 'green'), False):
        colors.insert(3, {"name": "green", "hex": "#92d050", "value": "13+1 — 13+6", "type": "color"})
    if not next((item for item in colors if item['name'] == 'lightgreen'), False):
        colors.insert(4, {"name": "lightgreen", "hex": "#c4d79b", "value": "12; 13+0", "type": "color"})
    if not next((item for item in colors if item['name'] == 'yellow'), False):
        colors.insert(5, {"name": "yellow", "hex": "#ffff00", "value": "11", "type": "color"})
    if not next((item for item in colors if item['name'] == 'pink'), False):
        colors.insert(6, {"name": "pink", "hex": "#fde9d9", "value": "1 — 10; Нет", "type": "color"})

    item = next((item for item in data if item['type'] == 'colors'), False)
    if not item:
        data.append({"data": colors, "type": "colors", "id": 0})

    a.deleteAll()
    a.addMany(data)


def main():
    import sys
    import ctypes

    setupDatabaseJSON()
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('ico.ico'))
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(swCall)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
