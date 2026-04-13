import os

class FileManager:
  
    def __init__(self,file_name):
    self.file_name = file_name
    open(self.file_name,'w').close()
    print("文件已经关闭")
