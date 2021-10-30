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

def fill_template(tmpl_string, dct):
        for key in dct:
            tmpl_string = tmpl_string.replace("<" + key + ">", dct[key])
        return tmpl_string

if __name__ == '__main__':
    for dct in m:
        print(fill_template(tmpl, dct))
