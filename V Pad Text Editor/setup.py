import cx_Freeze
import sys
import os
base = None

if sys.platform =='win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = r"C:\Users\91759\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\91759\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executable = [cx_Freeze.Executable("Amit_programe.py",base=base,icon='icon.ico')]

cx_Freeze.setup(
    name ="Vpad Text Editor",
    options = {"build_exe":{"packages":['tkinter',"os"],'include_files':["icon.ico",'tcl86t.dll','tk86t.dll','icon2']}},
    version ="0.1",
    description = "Tkinter Application",
    executables = executable
    )