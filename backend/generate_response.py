import pymongo
import pandas as pd
from pandas import DataFrame
from tabulate import tabulate
from dotenv import load_dotenv
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))

load_dotenv()
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")



CONNECTION_STRING = "mongodb+srv://"+username+":"+password+"@cluster0.1zo8noj.mongodb.net/test"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client["TF"]
uk_dining_retail = db["UK_dining_retail"]
item_details = uk_dining_retail.find()
df_uk_dining_retail = DataFrame(item_details).drop('_id', axis=1)


def process(email):
    if email=="":
        return ""
    try:
        data=json.loads(email)
        new_df = df_uk_dining_retail[(df_uk_dining_retail['model']== data['model']) & (df_uk_dining_retail['shape']==data['shape']) & (df_uk_dining_retail['size']==data['size'])]
        return tabulate(new_df, showindex=False, headers=new_df.columns, maxcolwidths=[None, None, None, None, None, 30, 50, None])
    except Exception as e:
        print(e)
        return "Please enter valid format"

