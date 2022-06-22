import time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Медиа плеер')
        self.setGeometry(100, 100, 100, 100)
        self._setup_ui()

    def _setup_ui(self):
        self.central_widget = QWidget(self)
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.user_action = -1
        self.play_button = QPushButton()
        self.player = MediaPlayer()
        self.play_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        self.pause_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
        self.dir_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon)
        self.play_button.setIcon(self.play_icon)
        self.play_button.clicked.connect(self.play_pause_button_clicked)
        self.ok_button = QPushButton()
        self.dir = QPushButton()
        self.dir.setIcon(self.dir_icon)
        self.dir.clicked.connect(self.dir_button_clicked)
        self.url_text = QLineEdit()
        self.ok_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogYesButton)
        self.ok_button.setIcon(self.ok_icon)
        self.ok_button.clicked.connect(self.change_url)
        self.volume = QDial()
        self.volume.setMaximum(100)
        self.volume.setMinimum(0)
        self.volume.setValue(int(self.player.current_volume * 100))
        self.volume.valueChanged.connect(self.sliderMoved)
        self.central_widget_layout.addWidget(self.url_text)
        self.central_widget_layout.addWidget(self.dir)
        self.central_widget_layout.addWidget(self.ok_button)
        self.central_widget_layout.addWidget(self.play_button)
        self.central_widget_layout.addWidget(self.volume)

    def sliderMoved(self):
        self.player.current_volume = self.volume.value() / 100
        self.player.audio_output.setVolume(self.player.current_volume)

    def change_url(self):
        url = self.url_text.text()

        if url is not None:
            self.url_text.clear()
            self.player.stop()
            self.player.setSource(QUrl(url))
            self.player.play()
            print('Станция изменена')
        else:
            print('Вы не ввели адрес')

    def play(self):
        self.play_button.setIcon(self.pause_icon)
        self.user_action = 1
        self.player.setSource(QUrl("ncs.mp3"))
        self.player.play()

    def pause(self):
        self.play_button.setIcon(self.play_icon)
        self.user_action = 2
        self.player.pause()

    def unpause(self):
        self.play_button.setIcon(self.pause_icon)
        self.user_action = 1
        self.player.play()

    def play_pause_button_clicked(self):
        if self.user_action <= 0:
            self.play()
        elif self.user_action == 1:
            self.pause()
        elif self.user_action == 2:
            self.unpause()

    def dir_button_clicked(self):
        path = QFileDialog.getOpenFileName()[0]
        self.url_text.clear()
        self.player.stop()
        self.player.setSource(QUrl(path))
        self.player.play()


class MediaPlayer(QMediaPlayer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_output = QAudioOutput()
        self.setAudioOutput(self.audio_output)
        self.audioOutput().setVolume(0.3)
        self.current_volume = self.audio_output.volume()

    def play(self):
        super().play()
        print('Запущено')

    def pause(self):
        super().pause()
        print('Остановлено')


if __name__ == '__main__':
    app = QApplication([])
    ex = MainWindow()
    ex.show()
    app.exec()
