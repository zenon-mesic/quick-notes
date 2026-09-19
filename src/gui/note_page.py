from gui.note import NoteWidget
from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)


class NotePageWidget(QWidget):
    def __init__(self, note_name = "Note", note_text = ""):
        super().__init__()

        main_layout = QVBoxLayout()

        row_layouts = [QHBoxLayout() for i in range(4)]
        for i in range(len(row_layouts)):
            for j in range(4):
                note_widget = NoteWidget(f"Note {4*i + j + 1}")
                row_layouts[i].addWidget(note_widget)
            row_widget = QWidget()
            row_widget.setLayout(row_layouts[i])
            main_layout.addWidget(row_widget)
        
        self.setLayout(main_layout)