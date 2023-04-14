from pathlib import Path

cwd = Path.cwd()

unterpfad = cwd / "subdir"

print(unterpfad.exists())
print(unterpfad.is_dir())

if not unterpfad.exists():
    unterpfad.mkdir()

neue_datei = unterpfad / "neue_datei.txt"
neue_datei.touch()

neue_datei.rename(unterpfad / "renamed.txt")

for datei in unterpfad.iterdir():
    print(datei)

if (unterpfad / "renamed.txt").exists():
    (unterpfad / "renamed.txt").unlink()

### Pfadmanipulationen

unterpfad = Path("../subdir")
print("----------------------")
# print(unterpfad)
# print(unterpfad.absolute())
# print(unterpfad.absolute().parent)
print(unterpfad.resolve())

#
# for datei in unterpfad.glob('**/*'):
#     if datei.is_file() and datei.suffix == ".txt":
#         print(datei)



