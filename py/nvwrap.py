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

from py3nvml.py3nvml import *

def handle_err(err):
    if (err.value == NVML_ERROR_NOT_SUPPORTED):
        return "Not available"
    else:
        return "???"

def nvwrap_Init():
    nvmlInit()

def nvwrap_Shutdown():
    nvmlShutdown()

def nvwrap_GetAllDevices():
    devlist = []
    dev_count = nvmlDeviceGetCount()
    for i in range(dev_count):
        handle = nvmlDeviceGetHandleByIndex(i)
        devlist.append("Device {}: {}".format(i, nvmlDeviceGetName(handle)))
    return devlist

def nvwrap_GetDriverVersion():
    drvver = "Version {}".format(nvmlSystemGetDriverVersion())
    return drvver

def nvwrap_GetTotalMem(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    inf = nvmlDeviceGetMemoryInfo(handle)
    total_mem = "{} MiB".format(inf.total >> 20)
    return total_mem

def nvwrap_GetDeviceSerial(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetSerial(handle)
        serial = "{}".format(inf)
    except NVMLError as err:
        serial = handle_err(err)
    return serial

def nvwrap_GetPcieGen(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetMaxPcieLinkGeneration(handle)
        max_pcie_gen = "{}".format(inf)
    except NVMLError as err:
        max_pcie_gen = handle_err(err)
    return max_pcie_gen

def nvwrap_GetPcieWidth(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetMaxPcieLinkWidth(handle)
        max_pcie_width = "x{}".format(inf)
    except NVMLError as err:
        max_pcie_width = handle_err(err)
    return max_pcie_width

def nvwrap_GetTempShutdown(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetTemperatureThreshold(handle, NVML_TEMPERATURE_THRESHOLD_SHUTDOWN)
        max_temp = "{} °C".format(inf)
    except NVMLError as err:
        max_temp = handle_err(err)
    return max_temp

def nvwrap_GetTempSlowdown(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetTemperatureThreshold(handle, NVML_TEMPERATURE_THRESHOLD_SLOWDOWN)
        sd_temp = "{} °C".format(inf)
    except NVMLError as err:
        sd_temp = handle_err(err)
    return sd_temp

def nvwrap_GetPowerLimit(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetPowerManagementLimit(handle) / 1000.0
        power_limit = '%.2f W' % inf
    except NVMLError as err:
        power_limit = handle_err(err)
    return power_limit

### Current / realtime ###
def nvwrap_GetCurrPcieGen(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetCurrPcieLinkGeneration(handle)
        curr_pcie_gen = "{}".format(inf)
    except NVMLError as err:
        curr_pcie_gen = "???"
    return curr_pcie_gen

def nvwrap_GetCurrPcieWidth(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetCurrPcieLinkWidth(handle)
        curr_pcie_width = "x{}".format(inf)
    except NVMLError as err:
        curr_pcie_width = "???"
    return curr_pcie_width

def nvwrap_GetCurrMemory(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetMemoryInfo(handle)
        curr_mem = "{} MiB".format(inf.used >> 20)
    except NVMLError as err:
        curr_mem = "???"
    return curr_mem

def nvwrap_GetCurrTemp(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)
        temp = "{} °C".format(inf)
    except NVMLError as err:
        temp = "???"
    return temp

def nvwrap_GetOpTemp(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetTemperatureThreshold(handle, NVML_TEMPERATURE_THRESHOLD_GPU_MAX)
        max_temp = "{} °C".format(inf)
    except NVMLError as err:
        max_temp = "???"
    return max_temp

def nvwrap_GetCurrGraphicsClock(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetClockInfo(handle, NVML_CLOCK_GRAPHICS)
        clock = "{} MHz".format(inf)
    except NVMLError as err:
        clock = "???"
    return clock

def nvwrap_GetCurrSMClock(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetClockInfo(handle, NVML_CLOCK_SM)
        clock = "{} MHz".format(inf)
    except NVMLError as err:
        clock = "???"
    return clock

def nvwrap_GetCurrMemoryClock(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetClockInfo(handle, NVML_CLOCK_MEM)
        clock = "{} MHz".format(inf)
    except NVMLError as err:
        clock = "???"
    return clock

def nvwrap_GetCurrVideoClock(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetClockInfo(handle, NVML_CLOCK_VIDEO)
        clock = "{} MHz".format(inf)
    except NVMLError as err:
        clock = "???"
    return clock

def nvwrap_GetCurrPower(dev):
    handle = nvmlDeviceGetHandleByIndex(dev)
    try:
        inf = nvmlDeviceGetPowerUsage(handle) / 1000.0
        power = '%.2f W' % inf
    except NVMLError as err:
        power = "???"
    return power