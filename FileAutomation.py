#! /usr/bin/python3
import os
import shutil

foldersName = [
            "01-Videos", "10-Not-known", "06-PDFs",      
            "05-Compressed-Files", "02-Audio", 
            "07-Micorsoft-Office", "03-Images",
            "04-Executable", "08-Python-Files",
            "09-C-Cpp_Files"
            ]
imageTypes = (".png", ".jpg", ".jpeg", ".gif", ".tff", ".raw") #images
vidoesTypes = (".mp4", ".mpg", ".avi", ".webm", ".mkv") #videos
audioTypes = (".mp3", ".mpa", ".wav", ".ogg") #audio
compressedTypes = (
                ".zip", ".tar", ".rar", ".iso",
                ".z", ".tar.gz", ".arj", ".deb",
                ".pkg", ".rpm"
                )#compressed

pdfType = ".pdf"
pyType = (".py", ".pyc")
C_CppTypes = (".c", ".cpp")
OfficeTypes = (".doc", ".docx", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx")
execTypes = (".exe", ".bat", ".bin", ".cmd", ".com", ".scr", ".vb")

class FilesArrange:
    DirectoryFileNames = []
    def __init__(self) -> None:
        print("Program Opened Success")
    
    def MoveToFolder(self, Path):
        for file in self.DirectoryFileNames:
            if(file.lower().endswith(imageTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/03-Images")
            
            elif(file.lower().endswith(pdfType)):
                shutil.move(f"{Path}/{file}", f"{Path}/06-PDFs")

            elif(file.lower().endswith(vidoesTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/01-Videos")
            
            elif(file.lower().endswith(audioTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/02-Audio")
            
            elif(file.lower().endswith(compressedTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/05-Compressed-Files")
            
            elif(file.lower().endswith(pyType)):
                shutil.move(f"{Path}/{file}", f"{Path}/08-Python-Files")
            
            elif(file.lower().endswith(C_CppTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/09-C-Cpp_Files")
            
            elif(file.lower().endswith(OfficeTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/07-Micorsoft-Office")
            
            elif(file.lower().endswith(execTypes)):
                shutil.move(f"{Path}/{file}", f"{Path}/04-Executable")

            else:
                shutil.move(f"{Path}/{file}", f"{Path}/10-Not-known")

    def DirectoryList(self, Path):
        self.DirectoryFileNames = os.listdir(Path)
        for folder in foldersName:
            try:
                os.mkdir(f"{path}/{folder}")
                print(f"Folder Created with Name {folder}")
            except:
                print(f"Can't make folder '{folder}' it may be maded before")

    def __del__(self) -> None :
        print("Awesome Programe is finished :)")
    

obj = FilesArrange()
path = input("Enter path to be organized : ")
obj.DirectoryList(path)
obj.MoveToFolder(path)
# print(obj.DirectoryFileNames)
