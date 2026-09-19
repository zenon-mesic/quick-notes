from PySide6.QtWidgets import QApplication

from gui.note_tabs import NoteTabsWidget


def test():
    app = QApplication()
    window = NoteTabsWidget()
    window.show()
    app.exec()

test()