from django.core.management.base import BaseCommand
import json
from applications.user.models import User, Adoptante

import httplib2
import os

from django.core.mail import send_mail


import random
from django.utils.crypto import get_random_string

from apiclient import discovery
from google.oauth2 import service_account

class Command(BaseCommand):
    help = 'Este comando permite registrar a los usuarios que llenaron el formularion en la aplicación móvil.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello World!!")

        try:
            scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
            #secret_file = os.path.join(os.getcwd(), 'credentials.json')
            
            secret_file = '../Agapet_Backend/applications/user/management/commands/credentials.json'
            #print(secret_file)
            spreadsheet_id = "1aQA0lDWeypFvWcCvHDlTgatKvsIg70Tfvt1bhNv2r58"
            range_name = 'A:X'

            credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
            service = discovery.build('sheets', 'v4', credentials=credentials)

            x=service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
            #print(x)

            headers = x["values"][0]
            body = x["values"][1:]
            
            for idx, element in enumerate(body):
                #print(idx, element) 
                if(element[1] is not None):
                    print(element[1])
                    usuarios = User.objects.buscar_correo(element[1])
                    if(not usuarios):
                        #password_temp = random.randint(0,99999999)
                        password_temp=get_random_string(length=8)
                        print(password_temp)
                    
                        user = User.objects.create_user_adp(
                            name=element[2],
                            lastname=element[3],
                            email = element[1],
                            direction = element[6],
                            phone = element[7],
                            age = 0
                        )
                        #print("string",str(password_temp))
                        #user.set_password(str(password_temp))
                        user.set_password(password_temp)
                        user.save()
                        Adoptante.objects.create(user=user)

        except OSError as e:
            print(e)