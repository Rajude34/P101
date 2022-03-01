import dropbox
class TransferData :
    def __init__(self,accessToken) :
        self.accessToken = accessToken
    def upload_file(self,fileFrom,fileTo) :
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom,"rb")
        dbx.files_upload(f.read(),fileTo)

def main() :
    accessToken = "sl.BCnWk4l13M4U-6fqIXD3-x_e_GDmijVi2KK0bDomPZIJ7AOAGph9tVT8RpUbyChSR5iQuKYaktYDEJvpx0cF7wCIQnvITrMSgqZYGrMP9vi5BhxUq2Z4EgMluAm-zSsq2aiSHIsPY99w"
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the file to transfer")
    fileTo = input("Enter the full path to upload to dropbox")
    transferData.upload_file(fileFrom,fileTo)
    print("File has been moved")
main()
        
