import os
import csv 

recipe_txt_path=os.path.join(os.getcwd(),'YinShanZhengYao_text/recipe_chapters')

fields=['Food_Name','Effect','Ingredients', 'Steps']


data={}
sequence=4


file_specific='JuanDiErShenXianFuShi.txt'
for file in os.listdir(recipe_txt_path):
    file=file_specific
    file_path=os.path.join(recipe_txt_path,file)
    print('file_path:',file_path)
    # Using readlines()
    file_txt = open(file_path, 'r')
    Lines = file_txt.readlines()
    
    single_row=[]
    rows=[]

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        line=line.strip()

        # Special treatment for 'JuanDiErShenXianFuShi.txt'
        if file=='JuanDiErShenXianFuShi.txt':
            if line=='服天门冬': 
                count=1
                sequence=3
            if line=='服地黄':
                count=1
                sequence=2
            if line=='神枕法':
                count=1
                sequence=5
                flag=True
            if line=='服菖蒲':
                count=1
                sequence=3
            if line=='服胡麻':
                count=1
                sequence=2
            if line=='服莲子莲蕊':
                count=1
                sequence=3
            if line=='服何首乌':
                count=1
                sequence=2

        if file=='JuanDiErShiLiaoZhuBing.txt':
            if line=='羊肉羹':
                count=1
                sequence=5
            if line=='鹿蹄汤':
                count=1
                sequence=4
            if line=='牛肉脯':
                count=1
                sequence=5
            if line=='莲子粥':
                count=1
                sequence=4
            if line=='牛奶子煎荜拨法':
                count=1
                sequence=2
            if line=='肉羹':
                count=1
                sequence=4
            if line=='羊肚羹':
                count=1
                sequence=5
            if line=='葛粉羹':
                count=1
                sequence=4
            if line=='恶实菜':
                count=1
                sequence=3
            if line=='乌驴皮汤':
                count=1
                sequence=4
        if file=='JuanDiErZhuBanTangJian.txt':
            if line=='荔枝膏':
                count=1
                sequence=5
            if line=='五味子汤':
                count=1
                sequence=4
            if line=='橘皮醒酲汤':
                count=1
                sequence=5
            if line=='渴忒饼儿':
                count=1
                sequence=4
            if line=='牛髓膏子':
                count=1
                sequence=5
            if line=='木瓜煎':
                count=1
                sequence=3
            if line=='酥油':
                count=1
                sequence=2
            if line=='清茶':
                count=1
                sequence=2
                #Exception
                rows.append(single_row)
                single_row=[]
            if line=='香茶':
                count=1
                sequence=3

        if file=='JuanDiYiJuZhenYiZhuan_1.txt':
            if line=='围像':
                count=1
                sequence=5
            if line=='春盘面':
                count=1
                sequence=3
            if line=='皂羹面':
                count=1
                sequence=4
            if line=='水龙子':
                count=1
                sequence=5
            if line=='马乞':
                count=1
                sequence=4
            if line=='攒鸡儿':
                count=1
                sequence=3
            if line=='鱼弹儿':
                count=1
                sequence=4
            if line=='派饼儿':
                count=1
                sequence=2
            if line=='盐肠':
                count=1
                sequence=3
            if line=='脑瓦剌':
                count=1
                sequence=2

        single_row.append(line)
        if count%sequence==0:
            rows.append(single_row)
            single_row=[]
            count=0
    
    data[file.split('.')[0]]=rows
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