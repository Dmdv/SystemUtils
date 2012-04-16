__author__ = 'Dyachkov'

try:
    import win32pdh
    print("win32pdh imported")
except ImportError:
    print('No performance data helper installed')