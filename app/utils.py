import urllib.request
import json
import ssl
import os
import json
ssl._create_default_https_context = ssl._create_unverified_context 

class task:
    def create_metafile(self,url,folder):

        try:
            response = urllib.request.urlopen(url) 
            data = response.read().decode('UTF-8')
            path=os.path.join('output/', folder)
            os.mkdir(path)  
            file = open(path+'/metadata.json',"w")
            file.write(data)
            jsonData=json.loads(data)

            response = urllib.request.urlopen(jsonData['download_url'])
            data = response.read()
            f = open(path+'/image.jpg','wb') 
  
            # Storing the image data inside the data variable to the file 
            f.write(data) 
            f.close()

        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read()) 

