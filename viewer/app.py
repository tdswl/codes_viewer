import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from viewer.viewmodels.mainwindow_vm import MainWindowViewModel

if __name__ == '__main__':
    # Create an instance of the application
    app = QGuiApplication(sys.argv)
    # Create QML engine
    engine = QQmlApplicationEngine()
    # Create a calculator object
    mainwindow_vm = MainWindowViewModel()
    # And register it in the context of QML
    engine.rootContext().setContextProperty("mainwindowVm", mainwindow_vm)
    # Load the qml file into the engine
    engine.load(QUrl('views/mainwindow.qml'))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
