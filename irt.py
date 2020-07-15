# -*- coding: utf-8 -*-
"""
build implict rating
"""
import numpy as np

kgfile=input("Please enter the path+name of kg file: ")
ratingfile=input("Please enter the path+name of rating file: ")
new_kg_path=input("Please enter the output path+name of the kg: ")
new_rating_path=input("Please enter the output path+name of rating file: ")

kg=open(kgfile,encoding='utf-8')
rating=open(ratingfile)
nkg=open(new_kg_path,'w',encoding='utf-8')#final kg file
fr=open(new_rating_path,'w',encoding='utf-8')

line=kg.readlines()
itemindex=dict()
relationindex=dict()
i=0
ri=0
cnt=0
bi=0


for k in line:
    
    array=k.strip().split('\t')
    
    head=array[0]
    relation=array[1]
    tail=array[2]
 
    if head not in itemindex:
        itemindex[head]=i
        i+=1
        bi+=1
    if tail not in itemindex:
        itemindex[tail]=i
        i+=1
        
    if relation not in relationindex:
        relationindex[relation]=ri
        ri+=1
    headindex=itemindex[head]
    tailindex=itemindex[tail]
    rindex=relationindex[relation]
    #print(headindex,rindex,tailindex)
    nkg.write('%d\t%d\t%d\n'%(headindex,rindex,tailindex)) 
    cnt+=1
nkg.close()
print('total kg: %d'%cnt)
print('total item: %d'%i)   
print('total relation %d'%ri)
print('total business %d'%bi)



#convert rating

userindex=dict()

rcnt=0
positem=dict()
negitem=dict()
u=0
user_num=0
itemset=set()
for r in rating:
    array2=r.strip().split('\t')
    user_id=array2[0]
    business_id=array2[1]
    star=int(array2[2])
    if business_id in itemindex:
       
       
        if user_id not in userindex:
           userindex[user_id]=u
           u+=1
           business=itemindex[business_id]  
           itemset.add(business)
           user=userindex[user_id]
    
    
        if star>=4:
            if user not in positem:
                positem[user]=set()
                user_num+=1
                positem[user].add(business)
        
        elif star<4:
            if user not in negitem:
                negitem[user]=set()
                negitem[user].add(business)
    
    #r.write('%d\t%d\t%s\n'%(userindex[user_id],itemindex[business_id],star))
    #rcnt+=1
ui=0   
for user,pos_item in positem.items():
    
    for item in pos_item:
       
        fr.write('%d\t%d\t1\n' % (ui, item))
        rcnt+=1
    unwatched_set=itemset-positem[user]

    if user in negitem:
        unwatched_set-=negitem[user]
    for item in np.random.choice(list(unwatched_set),size=len(pos_item),replace=False):
        
        fr.write('%d\t%d\t0\n' % (ui, item))
        rcnt+=1
    ui+=1
fr.close()
print('total rating:',rcnt)
print('total user',ui)

