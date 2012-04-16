__author__ = 'Dyachkov'

def setWallpaper( bmp ):
	import win32api, win32con, win32gui
	k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
	win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0")
	win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp, 1+2)

path = 'C:\\Users\\Dyachkov\\Pictures\\winter-wallpaper-47.jpg'

setWallpaper(path)