import os
import dropbox
from dropbox.files import WriteMode



class Transferdata:
    def __init__ (self,accesstoken):
        self.accesstoken = accesstoken

    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.accesstoken)
        for root,dirs,files in os.walk(filefrom):
            for filename in files:
                localPath = os.path.join(root,filename)
                relativePath = os.path.relpath(localPath,filefrom)
                dropboxpath = os.path.join(fileto,relativePath)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dropboxpath,mode = WriteMode('overwrite'))
    

def main():
    accesstoken = 'rzD0fKhc3IEAAAAAAAAAAZN-4PbhxeX_tIk68IB8EX_3tLCG61Cl19Byk-YVYFta'
    data1 = Transferdata(accesstoken)

    filefrom = input("ENTER THE FOLDER TO UPLOAD")
    fileto = input("ENTER THE COMPLET DROPBOX PATH")

    data1.upload_file(filefrom,fileto)
    print("FOLDER UPLOADED")

main()
