from gui import *
from swgoh_parser import getInfoFromSWGOH
from swgoh_parser import NotFoundPlayer
import threading
import sys


class ParserThread(threading.Thread):
    def __init__(self, id, needGuild, pathForSave, mainWindow):
        super().__init__()
        self.PlayerId = id
        self.PlayerNeedGuild = needGuild
        self.PlayerPathForSave = pathForSave
        self.window = mainWindow
        self.exception = None

    def run(self):
        print('run')
        try:
            getInfoFromSWGOH(
                id=self.PlayerId, needGuild=self.PlayerNeedGuild, pathForSave=self.PlayerPathForSave)
            killResources(ui=self.window)
            time.sleep(3)
            self.window.progressBar.setValue(100)
            time.sleep(5)
            self.window.progressBar.setValue(0)
            self.window.checkBox_2.setChecked(False)
            # self.window.show_popup_success()
            # self.window.progressBar.setValue(0)
        except NotFoundPlayer as ex:
            self.exception = ex
        except Exception as ex:
            self.exception = ex

    def join(self, timeout=None):
        threading.Thread.join(self, timeout=timeout)
        # Since join() returns in caller thread
        # we re-raise the caught exception
        # if any was caught
        if self.exception:
            raise self.exception


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
    myThread.start()


    # Обработка ошибок
    try:
        print('in try')
        myThread2.join(1)
        time.sleep(2)
        # myThread2.join()
        # ui.show_popup_success()

    except NotFoundPlayer as ex:
        print(ex)
        killResources(ui=ui)
        ui.show_popup()
        ui.progressBar.setValue(0)
    except Exception as ex:
        print(ex)
        killResources(ui=ui)
        ui.show_popup_ex()
        ui.progressBar.setValue(0)


def main():
    import sys
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
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
