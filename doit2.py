import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
%matplotlib inline
pd.get_option("display.max_rows")

images_folder = "images/res2"
df = pd.read_excel("data.xlsx")

df_filename = df['File Name ']
df_tags = df['Tags ']

#First look there are 6,479 tags. After cleaning, this number is reduced dramatically
df_tags.nunique()


true_tags = "bays,beaches,canals,canyons,cliffs,coasts,deserts,fields,forests,gardens,hills,ice,islands,lakes,landscapes,mountains,parks,plains,rivers,seascapes,snow,streams,storms,valleys,volcanoes,waterfalls,wetlands,aqueducts,archaeological sites,architecture,architectural plans,bridges,buildings,castles,cottages,townscapes,cityscapes,villages,encampments,educational buildings,factories,farms,forts,government buildings,hospitals,huts,interiors,lighthouses,mills,monuments,palaces,ports,public spaces,pubs,religious buildings,residential buildings,roads,ruins,stately homes,stations,tombs,towers,town squares,arts,battles,ceremonies,death,disasters,domestic life,drink,exploration,fashion,festivals,food,historical events,historical figures,hunting,leisure,music,people,performances,politics,political leaders,portaits,religion,religious figures,royalty,slavery,society,social life,sport,theatre,war,agriculture,crafts,construction,fishing,industries,manufacturing,markets,medicine,military,mining,naval,professions,science,trade,technology,tools,weapons,air travel,bicycles,boats,horse-drawn,railways,ships,transport,travel"
true_tags = list(true_tags.split(","))
len(true_tags)

#Creating a list to see the true tags actually used in the overall tagging process
#There are thirteen tags not being use (len: true_tags = 118, ee = 105)
ee = []

for i in range(len(df['Tags '])):
    b = df['Tags '][i].split(',')
    for j in b:    
        if j.lower().strip().endswith('s') == True:
            j = j[:-1] 
        if j.lower().strip() in true_tags and j.lower().strip() not in ee:
            ee.append(j)
ee = set(ee)

#Creating a list of all of the non-true tags. Len = 449 - these are all unique (except for probably some typos, etc.
#Manually changing these
a = []

for i in range(len(df['Tags '])):
    b = df['Tags '][i].split(',')
    for j in b:    
        if j.lower().strip().endswith('s') == True:
            j = j[:-1] 
        if j.lower().strip().endswith('s') == True:
            j = j[:-1]         
        if j.lower().strip() not in a and j.lower().strip() not in true_tags:
            a.append(j.lower().strip())
            
len(set(a))

