from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

from gui.note import NoteWidget


class NotePageWidget(QWidget):
    def __init__(self, clipboard):
        super().__init__()

        main_layout = QVBoxLayout()

        row_layouts = [QHBoxLayout() for i in range(4)]
        for i in range(len(row_layouts)):
            for j in range(4):
                note_widget = NoteWidget(f"Note {4*i + j + 1}", "", clipboard)
                row_layouts[i].addWidget(note_widget)
            row_widget = QWidget()
            row_widget.setLayout(row_layouts[i])
            main_layout.addWidget(row_widget)
        
        self.setLayout(main_layout)