import random
import pprint
import time
def convert_txt_to_str(filename = "txtfile"):
    try:
        f = open(filename, "r")
        text = ""
        for x in f:
          text+=x
        return text
    except:
        return "Error"
def opracuvaty_rechennya_vyklychennya(text):
    iterate_list = text.split(".") #Розбиваємо текст на речення
    conc_list = text.split(".")
    finallist = []
    for i in range(len(iterate_list)):
        if iterate_list[i][-1].isupper():
                conc_list[i] = iterate_list[i]+"."+iterate_list[i+1]
                try:
                    conc_list[i+1] = ""
                except:
                    break
    for i in conc_list:
        if i != "":
            finallist.append(i)
    
    return finallist
def distaty_vypadkove_rechennya(text):
    for i in text:
        if input():
            rndom_number = random.randrange(0, len(text))
            result = text[rndom_number]   
            print(result.strip()+".")
            text.pop(rndom_number)      
    return 0
_str = convert_txt_to_str('text.txt')  
_text = opracuvaty_rechennya_vyklychennya(_str)
print(distaty_vypadkove_rechennya(_text))