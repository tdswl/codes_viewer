from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QVariant
from viewer.database import DataBase
from viewer import config


class MainWindowViewModel(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._db = DataBase(config.DATABASE_PATH)
        self._search_string = ""
        self._selected_code = None
        self._codes = []

    searchStringResult = pyqtSignal()
    selectedCodeChanged = pyqtSignal()

    @pyqtSlot(QVariant)
    def selected_code_changed(self, code):
        self._selected_code = code
        self.selectedCodeChanged.emit()

    @pyqtSlot(str)
    def search(self, search_str):
        self._codes = self._db.search_code_by_string(search_str)
        self._search_string = search_str
        self.searchStringResult.emit()

    @pyqtProperty(str)
    def search_string(self):
        return self._search_string

    @pyqtProperty(QVariant)
    def codes(self):
        return QVariant(self._codes)

    @pyqtProperty(QVariant)
    def selected_code(self):
        return QVariant(self._selected_code)
