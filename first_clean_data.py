import os
import csv 

recipe_txt_path=os.path.join(os.getcwd(),'YinShanZhengYao_text/recipe_chapters')

fields=['Food_Name','Effect','Ingredients', 'Steps']


data={}
sequence=4


file_specific='JuanDiErShenXianFuShi.txt'
for file in os.listdir(recipe_txt_path):
    file_path=os.path.join(recipe_txt_path,file_specific)
    print('file_path:',file_path)
    # Using readlines()
    file_txt = open(file_path, 'r')
    Lines = file_txt.readlines()
    
    single_row=[]
    rows=[]

    flag=False
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        line=line.strip()
        single_row.append(line)

        # Special treatment for 'JuanDiErShenXianFuShi.txt'
        if file=='JuanDiErShenXianFuShi.txt':
            if line=='服天门冬': 
                print(line)
                count=1
                sequence=3
            if line=='服地黄':
                print(line)
                count=1
                sequence=2
            if line=='神枕法':
                print(line)
                count=1
                sequence=5
                flag=True
            if line=='服菖蒲':
                print(line)
                count=1
                sequence=3
            if line=='服胡麻':
                print(line)
                count=1
                sequence=2
            if line=='服莲子莲蕊':
                print(line)
                count=1
                sequence=3
            if line=='服何首乌':
                print(line)
                count=1
                sequence=2
        if count%sequence==0:
            rows.append(single_row)
            single_row=[]
            count=0
    
    data[file_specific.split('.')[0]]=rows
    break

for file, rows in data.items() :
    # name of csv file  
    csv_filename = os.path.join('first_clean_recipe','v1_'+file+".csv")
    print('csv_filename:',csv_filename)
        
    # writing to csv file  
    with open(csv_filename, 'w') as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
            
        # writing the fields  
        csvwriter.writerow(fields)  
            
        # writing the data rows  
        csvwriter.writerows(rows) 