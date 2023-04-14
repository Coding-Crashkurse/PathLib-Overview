from pathlib import PurePath, PurePosixPath, PureWindowsPath

pfad = PurePath("dokumente/unterlagen")

posix_pfad = PurePosixPath("dokumente/unterlagen")
windows_pfad = PureWindowsPath("dokumente\\unterlagen")

print("Verzeichnisname:", pfad.parent)
print("Basename:", pfad.name)

posix_aus_windows = PurePosixPath(windows_pfad)
windows_aus_posix = PureWindowsPath(posix_pfad)

print("Posix aus Windows:", posix_aus_windows)
print("Windows aus Posix:", windows_aus_posix)