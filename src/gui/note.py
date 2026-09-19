from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class NoteWidget(QWidget):
    def __init__(self, note_name, note_text, clipboard):
        super().__init__()

        self.clipboard = clipboard

        self.label = QLabel(note_name)
        self.contents = QTextEdit()
        self.contents.setAcceptRichText(False)

        buttons = QWidget()

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_note_content)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.copy_note_content)
        clear_button.clicked.connect(self.contents.clear)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(copy_button)
        buttons_layout.addWidget(clear_button)
        buttons.setLayout(buttons_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.contents)
        main_layout.addWidget(buttons)
        self.setLayout(main_layout)
    
    def copy_note_content(self):
        note_text = self.contents.toPlainText()
        if note_text != "":
            self.clipboard.setText(note_text)