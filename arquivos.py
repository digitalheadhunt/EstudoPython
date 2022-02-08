import requests

def save_img(url,num):
    
    file_name = "img"+num+".jpg"

	response = requests.get(url)
	file = open(file_name,"wb")
      
 	file.write(response.content)
	file.close()


