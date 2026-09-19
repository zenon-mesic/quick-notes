from PySide6.QtWidgets import QApplication

from gui.note_tabs import NoteTabsWidget


def test():
    app = QApplication()
    clipboard = app.clipboard()
    window = NoteTabsWidget(clipboard)
    window.show()
    app.exec()

test()