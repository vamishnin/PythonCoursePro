'''
Интерполировать некие шаблоны в строке: есть строка с определенного вида форматированием, необходимо заменить в этой строке все вхождения шаблонов на их значение из словаря.
'''

m = [{
    "name" : "Ivan",
    "surname" : "Ivanov",
    "bdate" : "1992/02/15",
    "nationality" : "Russian"
},{
    "name" : "Jhon",
    "surname" : "Doe",
    "bdate" : "1990/12/30",
    "nationality" : "USA"
}]

tmpl = "<name> <surname> was born in <bdate>, <nationality>"

def InsTemplate(tmpl_string, lst):
    for dct in lst:
        buf = tmpl_string
        
        for key in dct:
            buf = buf.replace("<" + key + ">", dct[key])
        
        print(buf)

InsTemplate(tmpl, m)
