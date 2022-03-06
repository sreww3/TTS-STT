from datetime import datetime 
t1 = datetime.now()
while (datetime.now()-t1).seconds <= 3:
  #do something
  print(datetime.now())