## comentario
import requests
import configparser
import json
from telegramsend import * 
#load variables
config = configparser.ConfigParser()
config.read('config.ini')
#variables
estado = 1
cmx = config["CONFIG"]["CMX"]
cmx_user = config["CONFIG"]["CMX_USER"]
cmx_pass = config["CONFIG"]["CMX_PASS"]
token_id = config["CONFIG"]["TOKEN_ID"]
group_id = config["CONFIG"]["GROUP_ID"]
message1 = config["CONFIG"]["MESSAGE1"]
message2 = config["CONFIG"]["MESSAGE2"]
counter_client = "api/location/v2/clients/count"
url_counter=cmx+counter_client
try:
        api_counter = requests.request(method="GET", timeout=3 , url=url_counter, auth=(cmx_user, cmx_pass), verify=False)
except:
        estado = 0
        print(estado)
        telegramsend(token_id,group_id,message1)
if estado == 1:
        try:
                datos = json.loads(api_counter1.text)
        except:
                estado = 0
                print(estado)
                telegramsend(token_id,group_id,message2)

