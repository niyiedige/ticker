def clearstr(str):


   temp=str.strip()

   return temp

def seperatestr(str):
    temp=str.split('(')
    temp[1]= temp[1][:-1]
    return temp