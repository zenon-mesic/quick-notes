from PySide6.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from gui.note_page import NotePageWidget


class NoteTabsWidget(QWidget):
    def __init__(self, note_name = "Note", note_text = ""):
        super().__init__()

        tabs = QTabWidget()
        for i in range(10):
            note_page = NotePageWidget()
            tabs.addTab(note_page, f"Page {i+1}")
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(tabs)
        self.setLayout(main_layout)