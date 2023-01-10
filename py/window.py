# AsGreenAsPossible [AGAP]
# Copyright (c) 2023 Jan Kowalewicz <jan.kowalewicz@web.de; jan@nitroosit.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QFormLayout, QLabel)
from PyQt6.QtCore import QSize
from nvwrap import * # NVML wrapper

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_interface()

    def init_interface(self):
        self.setWindowTitle('AsGreenAsPossible')
        self.setFixedSize(QSize(600, 400))

        central = QWidget()
        main_layout = QHBoxLayout() # central layout
        left_layout = QVBoxLayout() # static informations
        right_layout = QVBoxLayout() # realtime informations

        # left_layout
        devbox = QComboBox()
        devbox.setFixedWidth(300)
        devbox.addItems(nvwrap_GetAllDevices())
        left_layout.addWidget(devbox)

        # rt_widget & right_layout
        rt_widget = QWidget() # todo => pyfile
        rt_widget.setFixedWidth(350)
        rt_widget.setLayout(right_layout)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(rt_widget)

        central.setLayout(main_layout)
        self.setCentralWidget(central)