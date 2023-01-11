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

from PyQt6.QtWidgets import (QWidget, QGroupBox, QLabel, QVBoxLayout, QFormLayout)
from PyQt6.QtGui import QFont
from nvwrap import *

class RealtimeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_widget()
    
    def init_widget(self):
        self.setFixedWidth(350)

        valfont = QFont()
        valfont.setBold(True)

        main_layout = QVBoxLayout()

        ## Clock Speed
        clock_group = QGroupBox("Clock Speed")
        clocklayout = QFormLayout()
        self.CurrentClockGraphicsLbl = QLabel()
        self.CurrentClockGraphicsLbl.setFont(valfont)
        self.CurrentClockSMLbl = QLabel()
        self.CurrentClockSMLbl.setFont(valfont)
        self.CurrentClockMemLbl = QLabel()
        self.CurrentClockMemLbl.setFont(valfont)
        self.CurrentClockVideoLbl = QLabel()
        self.CurrentClockVideoLbl.setFont(valfont)
        clocklayout.addRow("Graphics:", self.CurrentClockGraphicsLbl)
        clocklayout.addRow("SM:", self.CurrentClockSMLbl)
        clocklayout.addRow("Memory:", self.CurrentClockMemLbl)
        clocklayout.addRow("Video:", self.CurrentClockVideoLbl)
        clock_group.setLayout(clocklayout)

        ## Memory
        mem_group = QGroupBox("Memory (VRAM)")
        memlayout = QVBoxLayout()
        self.CurrentMemLbl = QLabel(self)
        self.CurrentMemLbl.setFont(valfont)
        self.TotalMemLbl = QLabel()
        memlayout.addWidget(self.CurrentMemLbl)
        memlayout.addWidget(self.TotalMemLbl)
        mem_group.setLayout(memlayout)

        ## Temperature
        temp_group = QGroupBox("Temperature")
        templayout = QVBoxLayout()
        self.CurrentTempLbl = QLabel()
        self.CurrentTempLbl.setFont(valfont)
        self.MaxOpTempLbl = QLabel()
        templayout.addWidget(self.CurrentTempLbl)
        templayout.addWidget(self.MaxOpTempLbl)
        temp_group.setLayout(templayout)

        # Power
        power_group = QGroupBox("Power Usage (W)")
        powerlayout = QVBoxLayout()
        self.CurrentPowerDrawLbl = QLabel(self)
        self.CurrentPowerDrawLbl.setFont(valfont)
        self.MaxPowerDrawLbl = QLabel()
        powerlayout.addWidget(self.CurrentPowerDrawLbl)
        powerlayout.addWidget(self.MaxPowerDrawLbl)
        power_group.setLayout(powerlayout)

        main_layout.addWidget(clock_group)
        main_layout.addWidget(mem_group)
        main_layout.addWidget(temp_group)
        main_layout.addWidget(power_group)
        self.setLayout(main_layout)
    
    def update_vars(self, dev):
        nvmlInit()
        self.CurrentClockGraphicsLbl.setText(nvwrap_GetCurrGraphicsClock(dev))
        self.CurrentClockSMLbl.setText(nvwrap_GetCurrSMClock(dev))
        self.CurrentClockMemLbl.setText(nvwrap_GetCurrMemoryClock(dev))
        self.CurrentClockVideoLbl.setText(nvwrap_GetCurrVideoClock(dev))
        self.CurrentMemLbl.setText(nvwrap_GetCurrMemory(dev))
        self.TotalMemLbl.setText(nvwrap_GetTotalMem(dev))
        self.CurrentTempLbl.setText(nvwrap_GetCurrTemp(dev))
        self.MaxOpTempLbl.setText(nvwrap_GetOpTemp(dev))
        self.CurrentPowerDrawLbl.setText(nvwrap_GetCurrPower(dev))
        self.MaxPowerDrawLbl.setText(nvwrap_GetPowerLimit(dev))