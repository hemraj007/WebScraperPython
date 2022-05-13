# install required libraries
# python 3.x
# pip install requests
# pip install beautifulsoup4
# pip install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for j in range(1, 5116):
    url = 'https://www.medindia.net/patients/doctor_search/dr_result.asp?alpha=&page=' +str(j)+ '&dr_name=&city=&state=&pincode=&Specialist='
    req = requests.get(url)
    if(req.status_code==200):
        soup = BeautifulSoup(req.content, "html.parser")
    
        res = soup.findAll(attrs = {'class': 'vert-small-margin'})
        res1 = soup.findAll(attrs = {'class': 'border-bottom box-shadow vert-medium-margin'})

        # do for all entries in one page
        for i in range(0, len(res)):
            # Extract Name & Affiliation 
            res = soup.findAll(attrs = {'class': 'vert-small-margin'})
            Name_aff = res[i].text.split(",")
            if(len(Name_aff) > 1):
                Name = Name_aff[0]
                Affiliation = Name_aff[1]
            else:
                Name = Name_aff[0]
                Affiliation = ""
    
            # Extract Specialization & Adress
            p_list = res1[i].findAll("p")

            if(len(p_list) > 1):
                Specialization = p_list[0].text
                Address = p_list[1].text
            else:
                Specialization =""
                Address = p_list[0].text
    
            data.append([Name, Affiliation, Specialization, Address])
        print("Page Number: ", j)
    else:
        print("url Not Found ", i)
        
df = pd.DataFrame(data, columns = ['Doctor_Name', 'Clinic/Affiliation', 'Specialization', 'Address'])
df.to_csv('Doctors_DB.csv')