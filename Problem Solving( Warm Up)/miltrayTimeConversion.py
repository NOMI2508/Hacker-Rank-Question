def convert24(str1):
    if(str1[:2] == '12' and str1[-2:]=='AM'):
        return  str1[:-4]
    

print(convert24("12:59:59 AM"))