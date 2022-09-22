import pandas as pd 
import math
import numpy as np
from openpyxl import load_workbook
nan=float("nan")
wb = load_workbook(filename = '../../master.xlsx')
ws = wb['UK-R-Dining Tables']
df=pd.DataFrame(ws.values, columns=['blank1','model','blank2','shape','size','dimensions','top_1','top_2','top_3'])
df=df.fillna(value=np.nan)

df = df.drop([0,1], axis=0)
df = df.reset_index(drop=True)

df = df.drop(['blank1','blank2'], axis=1)

df.insert(4, 'height', np.nan)
df.insert(5, 'price', np.nan)
df.insert(6, 'top', np.nan)
df.insert(10, 'notes', np.nan)
df.insert(11, 'pad', np.nan)

df = df.drop(df.index[528:550], axis=0)
df.loc[len(df)]=['     ',np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]



#### Make sure dfs are correct ####

# df2 = pd.read_excel(open('../../../master.xlsx', 'rb'), sheet_name='UK-R-Dining Tables')
# with open("diff.txt", 'w') as f:
    # f.write(df.compare(df2).to_string())
    # f.write(df.to_string())

# df=df2

df.to_csv('before.csv')



#### Sort models and shapes ####

models=df['model'].tolist()
shapes=df['shape'].tolist()


new_models=[]
new_shapes=[]

model=""
shape=""
get_shape=False
for m,s in zip(models, shapes):
    m=str(m).strip()
    if m!="Rectangular" and m!="Round" and m!="Oval" and m!="Lozenge-shaped" and m!="Oval single pedestal base" and m!='nan':
        model=m
        shape=""
        new_models.append(model)
        new_shapes.append(shape)
        get_shape=True
    else:
        if get_shape==True:
            shape=m
            get_shape=False
        new_models.append(model)
        new_shapes.append(shape)
    exit


df['model']=new_models
df['shape']=new_shapes



#### Sort Heights ####

dimensions=df['dimensions'].tolist()

new_heights=[]
height=""
for d in dimensions:
    if str(d)[0]=='C':
        height=d
    new_heights.append(height)

df['height']=new_heights




#### Notes ####



notes=df['notes'].tolist()
sizes=df['size'].tolist()
top_2=df['top_2'].tolist()
shapes=df['shape'].tolist()

new_notes=[]

new_addition=False
addition_txt=""

for n, s, t_2, sh in zip(notes, sizes, top_2, shapes):
    s=str(s).strip()
    t_2=str(t_2).strip()
    if sh=="":
        new_notes.append(addition_txt)
        addition_txt=""
    else:
        if s!="S" and s!="M" and s!="L" and s!="XL" and s!="Size" and s!="nan" and s!="":
            if addition_txt != "":
                addition_txt=addition_txt+" "
            addition_txt=addition_txt+s+" "
            if t_2!="nan":
                addition_txt=addition_txt+t_2
        new_notes.append(n)

final_notes=[]
note=""
for n, sh in zip(reversed(new_notes), reversed(shapes)):
    sh=str(sh).strip()
    if sh=="" or sh=="nan":
        note=n
    final_notes.insert(0,note)

df['notes']=final_notes


#### Material Exclusions ####

top_1=df['top_1'].tolist()
top_2=df['top_2'].tolist()
top_3=df['top_3'].tolist()

new_top_1=[]
new_top_2=[]
new_top_3=[]

exclusion_1=""
exclusion_2=""
exclusion_3=""

for t1, t2, t3 in zip(reversed(top_1), reversed(top_2), reversed(top_3)):
    t1=str(t1).strip()
    t2=str(t2).strip()
    t3=str(t3).strip()
    if exclusion_1=="":
        new_top_1.insert(0, t1)
    else:
        new_top_1.insert(0, t1+" "+exclusion_1)
        exclusion_1=""
    if exclusion_2=="":
        new_top_2.insert(0, t2)
    else:
        new_top_2.insert(0, t2+" "+exclusion_2)
        exclusion_2=""
    if exclusion_3=="":
        new_top_3.insert(0, t3)
    else:
        new_top_3.insert(0, t3+" "+exclusion_3)
        exclusion_3=""
    if t1 and t1[0]=='(':
        exclusion_1=t1
    if t2 and t2[0]=='(':
        exclusion_2=t2
    if t3 and t3[0]=='(':
        exclusion_3=t3

df['top_1']=new_top_1
df['top_2']=new_top_2
df['top_3']=new_top_3



#### Remove Redundant Rows ####

df=df[df["shape"]!=""]

df=df.dropna(subset=['dimensions'])


df=df.dropna(subset=['size'])




#### squeeze tops into rows ####

dup = df['top_2'] != "nan"
df_try_1 = df[dup]

dup = df['top_3'] != "nan"
df_try_2 = df[dup]

df=df.append(df_try_1)
df=df.append(df_try_2)

df=df.sort_values(by=["model","shape"], key=lambda col: col.str.lower())


models=df['model'].tolist()
shapes=df['shape'].tolist()
sizes=df['size'].tolist()
prices=df['price'].tolist()
top_1=df['top_1'].tolist()
top_2=df['top_2'].tolist()
top_3=df['top_3'].tolist()

new_prices=[]
new_tops=[]

top_no=1
top_name=""
old_piece=""

for m, sh, s, p, t1, t2, t3 in zip(models, shapes, sizes, prices, top_1, top_2, top_3):
    if s.strip()=="Size":
        piece=m+sh
        if piece==old_piece:
            top_no+=1
        else:
            top_no=1
        if top_no==1:
            top_name=t1
        if top_no==2:
            top_name=t2
        if top_no==3:
            top_name=t3
        old_piece=piece
    new_tops.append(top_name)
    if top_no==1:
        new_prices.append(t1)
    if top_no==2:
        new_prices.append(t2)
    if top_no==3:
        new_prices.append(t3)

    

df['top']=new_tops
df['price']=new_prices
    



df=df[df["size"]!="Size "]



df=df[['model', 'shape', 'size', 'dimensions', 'height', 'top', 'notes', 'price']]


df.to_csv('after.csv', index=False)

