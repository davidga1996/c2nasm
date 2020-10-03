import sys
import os
import shutil
from pathlib import Path

class C2NASM:
    def __init__(self, argv):
        #formato
        #nasm -f elf test.asm
        self.format = ""
        self.system = ""
        self.objet  = ""
        self.file   = ""
        self.out    = ""
        self.execut = ""
        self.getData(argv)


    def getData(self, argv):
        if len(argv) == 1:
            #verificar su valor
            if argv[0] == "--version":
                print("NASM    version 2.15.05 compiled on Aug 28 2020")
        elif len(argv) == 2 or len(argv) == 3 and not "win32" in argv:
            if argv[0] == "new":
                self.new(argv)
        else :
            for arg in argv:
                if arg == "-f":
                    self.format = arg
                elif  arg == "win32" or arg == "elf32":
                    self.system = arg
                elif arg == "-fwin32":
                    self.format = "-f"
                    self.system = "win32"
                elif arg == "-felf32":
                    self.format = "-f"
                    self.system = "elf32"
                elif arg == "-o":
                    self.objet = arg
                elif arg[-5:] == ".nasm":
                    self.file = arg
                elif arg[-2:] == ".o":
                    self.out = arg
                elif arg[-4:] == ".exe":
                    self.execut = arg
            self.generate()
        
    def new(self, arg):
        out = "out"

        if len(arg) == 3:
            out = arg[2]

        #crear carpeta
        if not os.path.isdir(os.getcwd() + "/" + out):
            #si no existe la carpeta creala
            os.mkdir(os.getcwd() + "/" + out)

        if os.path.isfile(arg[1]):
            os.system(str.format("gcc -m32 -S -masm=intel -Os -o {0}nasm {0}c", arg[1][:-1]))
            #crea el archio
            nasm = arg[1][:-1] + "nasm"
            #mover archivo
            shutil.move(nasm, out + "/" + nasm)
        

    def generate(self):
        #genera el objeto.o
        if  self.format == "-f" and self.system == "win32" and self.file[-5:] == ".nasm":
            if os.path.isfile(self.file):
                path = Path(os.getcwd())
                file = str(path.parent) + "/" + self.file[:-5]
                
                if self.out != "" and self.objet == "-o":
                    os.system(str.format("gcc -c {0}.c -o {1}", file, os.getcwd() + "/" + self.out))
                else:
                    os.system(str.format("gcc -c {0}.c -o {1}.o", file, os.getcwd() +  "/" + self.file[:-5]))
            else:
                print(str.format("nasm: fatal: unable to open input file `{0}' No such file or directory", self.file))
            




def run():
    c2nams = C2NASM(sys.argv[1:])




if __name__ == "__main__" :
    run()
