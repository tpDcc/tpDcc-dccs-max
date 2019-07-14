# tpMaxLib

3ds Max implementation for tpDccLib and tpQtLib packages.

Also, this module contains a lot of utilities functions and classes to work with 3ds Max Python APIs (MaxPlus and pymxs)

## Installation
### Manual
1. Clone/Download tpMaxLib anywhere in your PC (If you download the repo, you will need to extract
the contents of the .zip file).
2. Copy **tpMaxLib** folder located inside **source** folder in a path added to **sys.path**

### Automatic
Automatic installation for tpMaxLib is not finished yet.

## Usage

### Initialization Code

1. If tpDccLib or tpQtLib packages are being used, tpMaxLib will be automatic imported during the initialization
of those packages.

2. If tpDccLib and tpQtLib are not found in your sys.path, you will need to initialize manually tpMaxLib.
```python
import tpMaxLib
tpMaxLib.init()
```

### Reloading
For development purposes, you can enable reloading system, so 
you can reload tpMaxLib sources without the necessity of restarting
your Python session. Useful when working with DCCs.

1. If tpDccLib and tpQtLib packages are being used, tpMaxLib will be automatic reload by tpDccLib and tpQtLib reload systems.

2. If tpDccLib and tpQtLib are not found, you will need to reload tpMaxLib manually.
```python
import tpMaxLib
reload(tpMaxLib)
tpMaxLib.init(True)
```

### Enabling debug log
By default, tpMaxLib logger only logs warning messages. To enable all log messages
you can set TPMAXLIB_DEV environment variables to 'True'
```python
import os

os.environ['TPMAXLIB_DEV'] = 'True'
import tpMaxLib
tpMaxLib.init()
```
