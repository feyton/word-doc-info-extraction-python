from django.db import models
import os
import shutil
import re
from docx import *
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)
folder = os.listdir()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# VARIABLES FOR THE NEEDED INFORMATIONS:

request_name = []
requester_id = []
req_cell = []
req_village = []
req_sector = []
req_district = []
req_province = []
permit_num = []
req_address = []
quantity_transport = []
from_location = []
to_location = []
for_owner = []
for_village = []
for_cell = []
for_tel = []
transaport_car = []










for files in folder:
    name, ext = os.path.splitext(files)
    if ext == '.docx':
        document = Document(files)
        bolds=[]
        emails=[]
        phones=[]
        for para in document.paragraphs:
 
            #03.1 Find email and phone numbers within the paragraph text
            text = para.text
            # print(text)
            permit_type = re.findall(r'URUHUSHYA RWO GUTWARA(.*)', text)
            email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
            phone_list=re.findall(r'(?<=Tel).*',text)
            id_number = re.findall(r'[0-9]{16}', text)
            akagari = re.findall(r'AKAGARI:(.*)', text)
            names = re.findall(r'AMAZINA(.*)', text)
            cars = re.findall(r'IMODOKA IZABITWARA(.*)', text)
            sector = re.findall(r'AKARERE:(.*)', text)
            from_loc = re.findall(r'(AHOBIVA(.*)|AHO BIVA(.*))(AHOBIJYA|AHO BIJYA)', text)
            destination = re.findall(r'AHOBIJYA(.*)|AHO BIJYA(.*)', text)
            driver_name = re.findall(r'IZINA RY’UMUSHOFERI(.*)Tel', text)
            start_date = re.findall(r'Kuva ku wa (.*)Kugeza', text)
            end_date = re.findall(r'Kugeza ku wa (.*)', text)

            # SPECIFIC INFO
            for id_num in id_number:
                requester_id.append(id_num)
            for i in akagari:
                req_cell.append(i)
            for c in cars:
                transaport_car.append(c)
            # print(from_loc)
        #     for email in email_list:
        #         emails.append(email)
        
            for phone in phone_list:
                for_tel.append(phone)
            for perm in permit_type:
                permit_num.append(perm)
        #     #03.2 Find the bold style within the word document
        #     for run in para.runs:
        #         if run.bold :
        #             bolds.append(run.text)

        # print(emails)
        # print(phones)

# print(requester_id)
# print(for_tel)
# print(permit_num)
# print(req_cell)
# print(transaport_car)

out_put_result = {
    'destination': to_location,
    'usaba': request_name,
    'akagari': req_cell,
    'permit_number': permit_num,
    'id_usaba': requester_id
}

r = json.dumps(out_put_result)
loaded_r = json.loads(r)
print("\n",json.dumps(loaded_r,indent=4, sort_keys=False))