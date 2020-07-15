# -*- coding: utf-8 -*-
"""
KGP: Knowledge Graph Processor

"""
import pandas as pd


# Read the CSV file and generate the data frame of the csv
def readfile(path):
    print("Your file path is: ", path)

    YN=input(" \ncorrect?(Y/N)")
    print("YN is ", YN)
    print(YN=="y")

    while YN != 'Y'  and YN!='y':
        try:
            path= input("Please enter your the path of your file:")
            print("Your file path is: ", path)
            YN=input(" \ncorrect?(Y/N)")
            print(YN)
            print(YN=="n")
        except:
            print("Error, please re-enter")
            continue
    print("reading..........")
    input_file=pd.read_csv(path)
    return input_file
#select the columns you need
def takecolumns(input_file):
    columns=input_file.columns
    for i in range(len(columns)):
        print(i,".",columns[i])
    selected_column='0'

    columns_list=dict()
    while selected_column!= '-1':
        count=0
        selected_column=input("Enter the columns number you need and enter -1 to end:  ")
        column_n=int(selected_column)
        columns_list[selected_column]=columns[column_n]
        
    return columns_list

def build_kg_list(columns_list):
    kg_list=dict()
    triger='0'
    i=0
    while triger!='-1':
        try:
            relation_name=input("Enter the relation name ")
            item1_n=input('Enter the columns number for the on the left: ')
            item2_n=input('Enter the columns number for on the right ')
            item1=columns_list[item1_n]
            item2=columns_list[item2_n]
            kg_list[i]=[item1,relation_name,item2]
            i=i+1
            triger=input("end? -1")
        except:
            print("Error, please re-enter")
            continue
    for i in kg_list:
        print(i)
        print (kg_list[i])
    return kg_list

def build_rating_list(columns_list):
    rating_list=dict()
    triger='0'
    i=0
    while triger!='-1':
        try:  
            item1_n=input('Enter the columns number for the on the left: ')
            item2_n=input('Enter the columns number for on the right ')
            mid_n=input("Enter the columns number for in the middle  ")
            item1=columns_list[item1_n]
            item2=columns_list[item2_n]
            mid=columns_list[mid_n]
            rating_list[i]=[item1,mid,item2]
            i=i+1
            triger=input("end? -1")
        except:
            print("Error, please re-enter")
            continue
    for i in rating_list:
        print(i)
        print (rating_list[i])
    return rating_list
#
def pickout_kg(inputfile,kg_list):
    def resetbool(df,left,right):
        print(type(df.loc[1,left]))
        if type(df.loc[1,left])== bool:
            for i in range(len(df)):
                if df.loc[i,left]==True:
                    df.loc[i,left]=left+'.True' 
                elif  df.loc[i,left]==False:
                    df.loc[i,left]=left+'.False'

                
                
        if type(df.loc[1,right])== bool:
            for i in range(len(df)):
                if df.loc[i,right]==True:
                    df.loc[i,right]=right+'.True' 
                elif  df.loc[i,right]==False:
                    df.loc[i,right]=right+'.False'

   
        return df
    
    df_list=dict()
    for i in kg_list:
        print(i)
       
        left=kg_list[i][0]
        right=kg_list[i][2]
        relation=kg_list[i][1]
        print(left, right, relation)
        df_list[i]=inputfile[[left,right]]#constract a df for a serios triplets with same relation.
        print(type(df_list[i]))
      
                             
        df_list[i]['relation']=relation
        df_list[i]=df_list[i][[left,'relation',right]]
        df_list[i]=df_list[i].dropna(axis=0,how='any')
        df_list[i]=df_list[i].drop_duplicates(keep='first')
        df_list[i]=df_list[i].reset_index(drop=True)
        #
        for a in range(len(df_list[i])):
            df_list[i]=resetbool(df_list[i],left,right)
        df_list[i]= df_list[i].rename(columns={left:"item", right:"item.2"})
    d={'item':[0],'relation':[0],'item.2':[0]}
    dfc = pd.DataFrame(data=d)
    for i in df_list:
        
        dfc=pd.concat([dfc,df_list[i]])
    dfc=dfc.drop([0])
    dfc=dfc.dropna(axis=0,how='any')
    dfc=dfc.drop_duplicates(keep='first')
    dfc=dfc.reset_index(drop=True)
    return dfc

def pickout_rating(inputfile,rating_list):
    df_list=dict()   
    left=rating_list[0][0]
    right=rating_list[0][2]
    mid=rating_list[0][1]
    print(left, mid, right)
    dfc=inputfile[[left,mid,right]]    
    dfc=dfc.drop([0])
    dfc=dfc.dropna(axis=0,how='any')
    dfc=dfc.drop_duplicates(keep='first')
    dfc=dfc.reset_index(drop=True)
    return dfc

def assig_index(df,itemdict_file,relationdict_file):
    #itemdict_file=input("Please enter item index file path: ")
    itemtxt=open(itemdict_file,'w',encoding='utf-8')
    #relationdict_file=input("Please enter the relation index file path:")
    relationtxt=open(relationdict_file,'w',encoding='utf-8')
    itemdict=dict()
    relationdict=dict()
    ii=0
    ri=0
    print('replacing') 
    
    for i in range(len(df)):
        
        item=str(df.loc[i,'item']).strip()
        relation=str(df.loc[i,'relation']).strip()
        item2=str(df.loc[i,'item.2']).strip()
        
        if i==int(len(df)/5):
            print('20%')
        if i==int(len(df)/5)*2:
            print('40%')
        if i==int(len(df)/5)*3:
            print('60%')
        if i==int(len(df)/5)*4:
            print('80%')
            
        try:
            df.loc[i,'item']=itemdict[item]
        except:
            itemdict[item]=ii
            df.loc[i,'item']=ii
            itemtxt.write('%s\t%d\n'%(item,itemdict[item]))
            ii+=1
            
        
        
        try:
            df.loc[i,'item.2']=itemdict[item2]
        except:
            itemdict[item2]=ii
            df.loc[i,'item.2']=ii
            itemtxt.write('%s\t%d\n'%(item2,itemdict[item2]))
            ii+=1
            
        try:
            df.loc[i,'relation']=relationdict[relation]
        except:
            relationdict[relation]=ri
            df.loc[i,'relation']=ri
            relationtxt.write('%s\t%d\n'%(relation,relationdict[relation]))
            ri+=1
            
    itemtxt.close()
    relationtxt.close()
    output=[df,relationdict,itemdict,ri,ii] 
    return output

def assig_business_index(df,itemdict,ii,itemdict_file):
    itemtxt=open(itemdict_file,'a',encoding='utf-8')
    userdict_file=input("Please enter the path+name of the user index file")
    usertxt=open(userdict_file,'w',encoding='utf-8')
    
    userdict=dict()
    
    ui=0
    
    print('replacing') 
    left=df.columns[0]
    #right=df.columns[2]
    mid=df.columns[1]
    for i in range(len(df)):
        
        user=str(df.loc[i,left]).strip()
        business=str(df.loc[i,mid]).strip()
        #rating=str(df.loc[i,right]).strip()
        
        if i==int(len(df)/5):
            print('20%')
        if i==int(len(df)/5)*2:
            print('40%')
        if i==int(len(df)/5)*3:
            print('60%')
        if i==int(len(df)/5)*4:
            print('80%')
            
        try:
            df.loc[i,left]=itemdict[user]
        except:
            itemdict[user]=ui
            df.loc[i,left]=ui
            usertxt.write('%s\t%d\n'%(user,itemdict[user]))
            ui+=1
            
        
        
       
            
        try:
            df.loc[i,mid]=itemdict[business]
        except:
            itemdict[business]=ii
            df.loc[i,mid]=ii
            itemtxt.write('%s\t%d\n'%(business,itemdict[business]))
            ii+=1
            
    itemtxt.close()
    usertxt.close()
    rating_output=[df,userdict,itemdict,ui,ii] 
    return rating_output

path= input("Please enter your the path of the csv file:")
##Read file
input_file=readfile(path)
##select columns
columns_list=takecolumns(input_file)
#build kg list
kg_list=build_kg_list(columns_list)
df=pickout_kg(input_file,kg_list)
itemdict_file=input("Please enter item index file path: ")
relationdict_file=input("Please enter the relation index file path:")
output=assig_index(df,itemdict_file,relationdict_file)

relationdict=output[1]
itemdict=output[2]
ri=output[3]
ii=output[4]

a=1
while a == 1:
    try:
        filetype= input("Please enter the kg file type:(csv or txt) ")
        filename =input("Please enter the path+name for the kg file")
        if filetype == "csv":
            output[0].to_csv(filename)
            a=0
        elif filetype == "txt":
            output[0].to_csv(filename, sep = '\t',header = False, index = False)
            a=2
    except:
            print("Error, please re-enter")
            continue

d=input("Begin to construct rating file?(Y/N)")

if d == "y" or d == "Y":
    #df,itemdict,ii,itemdict_file
    rating_columns_list=takecolumns(input_file)
    rating_triplet=build_rating_list(rating_columns_list)
    rating_df=pickout_rating(input_file,rating_triplet)
    rating_output=assig_business_index(rating_df,itemdict,ii,itemdict_file)
    a=1
    while a == 1:
        try:
            filetype= input("Please enter the rating file type:(csv or txt) ")
            filename =input("Please enter the path+name for the rating file")
            if filetype == "csv":
                output[0].to_csv(filename)
                a=0
            elif filetype == "txt":
                output[0].to_csv(filename, sep = '\t',header = False, index = False)
                a=2
        except:
            print("Error, please re-enter")
            continue
            