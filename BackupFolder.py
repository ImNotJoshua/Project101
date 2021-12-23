import dropbox
import os 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, source, destination):
        dbx =  dropbox.Dropbox(self.access_token)
        for folder, subFolders, files in os.walk(source):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                dropboxPath = os.path.relpath(localPath, source)
                finalDropboxPath = os.path.join(destination, dropboxPath)
                
        with open(localPath, 'rb') as f:
            dbx.files_upload(f.read(), finalDropboxPath)

def main():
    access_token = 'sl.A-tv-rDHDFO2BiJRECopmsMFEKHyttnfSiFRBUDpfqumBsqqxTFPZC40KtEwdPFaP8FjwSgsFNZcz-1kuMff5w-TKjMPFavDq5-zeYe5XM0JzMsdIuISDacdf-Qprpt1f-ExW9E'
    transferData =  TransferData(access_token)

    source = input("enter source file name with address")
    destination = input("enter destination file name address")

    transferData.upload_file(source, destination)
    print("Your file has been successfully uploaded")

if __name__ == '__main__':
    main()

