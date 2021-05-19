import cx_Freeze
import os
import sys
base=None

if sys.platform=='win32':
    base="Win32GUI"

os.environ['TCL_LIBRARY']=r"C:\Users\user\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\user\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"


executables=[cx_Freeze.Executable("NotesMaker.py", base=base, icon='icon.ico')]


cx_Freeze.setup(
    name= "TextWithMe Notes Maker",

    options={'build_exe' : {"packages":["tkinter","os"],"include_files":["tcl86t.dll","tk86t.dll","icon.ico"]}},
    version="0.1",
    description="Tkinter Application",
    executables=executables 
)
# print(sys.version_info())