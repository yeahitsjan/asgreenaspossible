## AsGreenAsPossible
![pythonver](https://img.shields.io/badge/python-3.11-blue?style=flat-square&logo=python) ![ver](https://img.shields.io/badge/version-0.0.0-green?style=flat-square) 

<img src="https://raw.githubusercontent.com/yeahitsjan/asgreenaspossible/develop/resources/icon.png" width="96" height="96" align="right">


> **WARNING:** Currently not ready for production use. Not all features are implemented.

AGAP tries to display various static & realtime informations about your NVIDIA GPU in a simple window. It uses [py3nvml](https://github.com/fbcotter/py3nvml) under the hood.

![screenshot 11.01.23](https://raw.githubusercontent.com/yeahitsjan/asgreenaspossible/develop/resources/screenshot_110123.PNG)

Currently supported features:
- Device List (show all GPUs)
- Device Serial (where applicable)
- System Driver Version
- Current, total & used VRAM
- Current & Supported PCIe Generation
- Current & Supported PCIe Lanes
- Current, Shutdown & Slowdown temperatures
- Power Draw & Power Limit
- Realtime clock speeds (Graphics, SM, Memory, Video)

## Run

AGAP uses PyQt6 for UI and py3nvml for NVIDIA informations. You can install both via pip:
```
$ pip install pyqt6 py3nvml
```

You can then run from the ``py`` directory:
```
$ python main.py
```

**When the application has a usable state, I will also provide binaries.**

## License

MIT.

```
AsGreenAsPossible (AGAP)
Copyright (c) 2023 Jan Kowalewicz <jan.kowalewicz@web.de, jan@nitroosit.de>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```