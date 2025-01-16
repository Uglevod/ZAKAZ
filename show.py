# лоад данные ожидания 
# лоад данные заказов 

# что нужно.. что забирать уже сейчас - до какого желательно забрать 
# + коммент - возврат ели нуно 
# ближайший доставка 

# просто вывести все что есть по дате прихождения и общую сумму заказов которые не получены и в этом месяце 
# можно еще категорию ))) закзаов ) 

import json
from datetime import datetime,timedelta



f = open("zakaz.json")
zj = json.loads( f.read() )
f.close()

now = datetime.now()

f = open("hold.json")
hj = json.loads( f.read() )
f.close()

for z in zj:
    #print(z)
    
    dtd = datetime.strptime( z["dtd"] , "%Y-%m-%d")
    #print(now,dtd)
    if now < dtd and not z["get"]:
        
        ost = round( (dtd-now).total_seconds()//(60*60*24) )
        
        print("В Пути", z["dtd"], f"{ost:<2}", f"{z['place']:<9}" , z["prod"]  )






print( )

sum=0
for z in zj:
    #print(z)
    
    dtd = datetime.strptime( z["dtd"] , "%Y-%m-%d")
    #print(now,dtd)
    if now > dtd and not z["get"]:
        
    
        #print("В ПВЗ с ", z["dtd"], z["place"] , z["prod"]  , end=" " )
        
        dth=""
        for h in hj:
            if h["place"] == z["place"]:
                dl  = timedelta( days=h["d"] )
                dth = (dtd+dl ).strftime("%Y-%m-%d")
                #print(" Хранение до", dth  )

        print("В ПВЗ с", z["dtd"], f"{z['place']:<11}" , f"{z['prod']:<33}", 'Хранение до'   , dth ,"т.е. еще ", "dl" ,   (dtd+dl) -now  )

        #print( )
        
    
    sum += z["price"]
        
print( ) 
print("Сумма ожидаемых"                 ,sum)
print("Сумма заказанного в этом месяце" ,sum)
print("Сумма заказаного  в этом году"   ,sum)