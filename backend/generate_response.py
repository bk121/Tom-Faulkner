# import pymongo
# import pandas as pd
# from pandas import DataFrame
# from tabulate import tabulate
# from dotenv import load_dotenv
# import sys
# import os

# sys.path.append(os.path.dirname(__file__))

# load_dotenv()
# username = os.getenv("MONGO_USERNAME")
# password = os.getenv("MONGO_PASSWORD")



# CONNECTION_STRING = "mongodb+srv://"+username+":"+password+"@cluster0.1zo8noj.mongodb.net/test"
# client = pymongo.MongoClient(CONNECTION_STRING)

# db = client["TF"]
# col = db["UK_dining_retail"]
# item_details = col.find()
# df = DataFrame(item_details).drop('_id', axis=1)


# def process(email):
#     if email=="":
#         return ""
#     try:
#         values = email.split()
#         new_df = df[(df['model']== values[0]) & (df['shape']==values[1]) & (df['size']==values[2])]
#         # new_df=new_df.drop('notes', axis=1)
#         return tabulate(new_df, showindex=False, headers=new_df.columns, maxcolwidths=[None, None, None, None, None, 30, 50, None])
#     except:
#         return "Please enter valid format"

