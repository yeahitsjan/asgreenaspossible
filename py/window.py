# AsGreenAsPossible
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

from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QFormLayout, QLineEdit)
from PyQt6.QtCore import QSize
from nvwrap import * # NVML wrapper

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_interface()
        self.init_vars()

    def init_interface(self):
        self.setFixedSize(QSize(600, 400))

        central = QWidget()
        main_layout = QHBoxLayout() # central layout
        left_layout = QVBoxLayout() # static informations
        right_layout = QVBoxLayout() # realtime informations

        ### left_layout ###
        # Device Combobox
        self.devbox = QComboBox()
        self.devbox.setFixedWidth(300)
        left_layout.addWidget(self.devbox)
        
        form = QFormLayout()
        # Device Serial
        self.serialline = QLineEdit()
        self.serialline.setReadOnly(True)
        form.addRow("Serial:", self.serialline)
        # System Driver version
        self.drvline = QLineEdit()
        self.drvline.setReadOnly(True)
        form.addRow("Driver version:", self.drvline)
        # Total VRAM
        self.vramline = QLineEdit()
        self.vramline.setReadOnly(True)
        form.addRow("Total memory:", self.vramline)
        # PCIe Gen
        self.pciegenline = QLineEdit()
        self.pciegenline.setReadOnly(True)
        self.pciegenline.setToolTip("The PCIe Generation the GPU is supporting. This <b>does not</b> show the <b>current</b> PCIe Generation.")
        form.addRow("PCIe Generation:", self.pciegenline)
        # PCIe Width
        self.pciewidthline = QLineEdit()
        self.pciewidthline.setReadOnly(True)
        self.pciewidthline.setToolTip("The PCIe Width Lane the GPU is supporting. This <b>does not</b> show the <b>current</b> PCIe Width.")
        form.addRow("PCIe Width:", self.pciewidthline)
        # Shutdown Temperature
        self.maxtempline = QLineEdit()
        self.maxtempline.setReadOnly(True)
        form.addRow("Shutdown Temperature:", self.maxtempline)
        # Slowdown Temperature
        self.sdtempline = QLineEdit()
        self.sdtempline.setReadOnly(True)
        form.addRow("Slowdown Temperature:", self.sdtempline)
        # Power Limit
        self.powlimitline = QLineEdit()
        self.powlimitline.setReadOnly(True)
        form.addRow("Power Limit:", self.powlimitline)

        left_layout.addLayout(form)

        # rt_widget & right_layout
        rt_widget = QWidget() # todo => pyfile
        rt_widget.setFixedWidth(350)
        rt_widget.setLayout(right_layout)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(rt_widget)

        central.setLayout(main_layout)
        self.setCentralWidget(central)
    
    def init_vars(self):
        nvwrap_Init()
        self.devbox.addItems(nvwrap_GetAllDevices())
        self.serialline.setText(nvwrap_GetDeviceSerial(self.devbox.currentIndex()))
        self.drvline.setText(nvwrap_GetDriverVersion())
        self.vramline.setText(nvwrap_GetTotalMem(self.devbox.currentIndex()) + " MiB")
        self.pciegenline.setText(nvwrap_GetPcieGen(self.devbox.currentIndex()))
        self.pciewidthline.setText(nvwrap_GetPcieWidth(self.devbox.currentIndex()))
        self.maxtempline.setText(nvwrap_GetTempShutdown(self.devbox.currentIndex()))
        self.sdtempline.setText(nvwrap_GetTempSlowdown(self.devbox.currentIndex()))
        self.powlimitline.setText(nvwrap_GetPowerLimit(self.devbox.currentIndex()))
        nvwrap_Shutdown()