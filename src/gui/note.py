from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class NoteWidget(QWidget):
    def __init__(self, note_name = "Note", note_text = ""):
        super().__init__()

        self.label = QLabel(note_name)
        self.contents = QTextEdit()

        buttons = QWidget()

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.contents.copy)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.contents.cut)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(copy_button)
        buttons_layout.addWidget(clear_button)
        buttons.setLayout(buttons_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.contents)
        main_layout.addWidget(buttons)
        self.setLayout(main_layout)