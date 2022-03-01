import dropbox
import os 
from dropbox.files import WriteMode
class TransferData :
    def __init__(self,accessToken) :
        self.accessToken = accessToken
    def upload_file(self,fileFrom,fileTo) :
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom) :
            for fileName in files :
                localPath = os.path.join(root,fileName)
                relative_path = os.path.relpath(localPath,fileFrom)
                dropbox_path = os.path.join(fileTo, relative_path)
            with open(localPath, 'rb') as f :
                dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

     

def main() :
    accessToken = "sl.BCnWk4l13M4U-6fqIXD3-x_e_GDmijVi2KK0bDomPZIJ7AOAGph9tVT8RpUbyChSR5iQuKYaktYDEJvpx0cF7wCIQnvITrMSgqZYGrMP9vi5BhxUq2Z4EgMluAm-zSsq2aiSHIsPY99w"
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the folder to transfer")
    fileTo = input("Enter the full path to upload to dropbox")
    transferData.upload_file(fileFrom,fileTo)
    print("Folder has been moved")
main()
        
