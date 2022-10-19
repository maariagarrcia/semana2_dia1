import numpy as np
citizens = [{ 'First Name': 'Preston' , 'Last Name': 'Cunningham', 'Age': 49 , 'Education': 'Doctoral', 'Occupation':' Teacher' ,'Experience (Years)': 6, 'Salary': 62499}, 
 { 'First Name': 'Madaline', 'Last Name': 'Farrell', 'Age': 41, 'Education': 'Bachelor', 'Occupation': 'Insurer','Experience (Years)': 16, 'Salary': 50190},
 { 'First Name': 'Eleanor', 'Last Name': 'Carter', 'Age': 49, 'Education': 'Lower secondary', 'Occupation': 'Programmer','Experience (Years)': 18, 'Salary': 189716},
 { 'First Name': 'Adison', 'Last Name': 'Hall', 'Age': 42 , 'Education': 'Bachelor', 'Occupation': 'Florist','Experience (Years)': 21, 'Salary': 34517},
 { 'First Name': 'Grace', 'Last Name': 'Cooper', 'Age': 49, 'Education': 'Master', 'Occupation': 'Singer','Experience (Years)': 9, 'Salary': 51994},
 { 'First Name': 'Alford', 'Last Name': 'Kelley', 'Age': 49, 'Education': 'Bachelor', 'Occupation': 'Aeroplane Pilot','Experience (Years)': 9, 'Salary': 170466},
 { 'First Name': 'Vincent', 'Last Name': 'Anderson', 'Age': 47, 'Education': 'Master', 'Occupation': 'Botanist','Experience (Years)': 6, 'Salary': 71617},
 { 'First Name': 'Myra', 'Last Name': 'Wright', 'Age': 45, 'Education': 'Master', 'Occupation': 'Geologist' ,'Experience (Years)': 18, 'Salary': 48786},
 { 'First Name': 'Chester', 'Last Name':'Bennett', 'Age': 42, 'Education': 'Doctoral', 'Occupation': 'Astronomer','Experience (Years)': 13, 'Salary': 44826},
 { 'First Name': 'Blake', 'Last Name': 'Tucker', 'Age': 42, 'Education': 'Doctoral', 'Occupation': 'Firefighter','Experience (Years)': 21, 'Salary': 36761},
 { 'First Name': 'Paige', 'Last Name': 'Ryan', 'Age': 43, 'Education': 'Primary', 'Occupation': 'Fine Artist','Experience (Years)': 19, 'Salary': 28181},
 { 'First Name': 'Natalie', 'Last Name': 'Ellis', 'Age': 45, 'Education': 'Bachelor', 'Occupation': 'Baker','Experience (Years)': 0, 'Salary': 31194},
 { 'First Name': 'Martin', 'Last Name': 'Thompson', 'Age': 47, 'Education': 'Bachelor', 'Occupation': 'Journalist','Experience (Years)': 21, 'Salary': 90183},
 { 'First Name': 'Alan', 'Last Name': 'Sullivan', 'Age': 46, 'Education': 'Doctoral', 'Occupation': 'Singer','Experience (Years)': 2, 'Salary': 18440},
 { 'First Name': 'Inga', 'Last Name': 'Bergman', 'Age': 41, 'Education': 'Bachelor', 'Occupation': 'Producer','Experience (Years)': 22, 'Salary': 80029},
 { 'First Name': 'Freddy', 'Last Name': 'Brown', 'Age': 48, 'Education': 'Bachelor', 'Occupation': 'Economist','Experience (Years)': 18, 'Salary': 146217},
 { 'First Name': 'Adelaide', 'Last Name': 'Farrell', 'Age': 42, 'Education': 'Bachelor', 'Occupation': 'Mechanic','Experience (Years)': 9, 'Salary':19414},
 { 'First Name': 'Luke', 'Last Name': 'Cooper', 'Age': 40, 'Education': 'Upper secondary', 'Occupation': 'Producer','Experience (Years)': 17, 'Salary': 160541},
 { 'First Name': 'Sofia', 'Last Name': 'Hall', 'Age': 41, 'Education': 'Doctoral', 'Occupation': 'Baker','Experience (Years)': 1, 'Salary': 25904},
 { 'First Name': 'Ashton', 'Last Name': 'Kelly', 'Age': 49, 'Education': 'Master', 'Occupation': 'Chef','Experience (Years)': 6, 'Salary': 95533}
]

# edad media de los ciudadanos
    
def  almacenar_edades(lista):
    edades = []
    for i in lista:
        edades.append(i['Age'])
    return edades

def media_numeros(lista):
    print("La edad  media de los ciudadanos es de :",np.mean(lista), "años")

def  edad_media(lista):
    edades = almacenar_edades(lista)
    return media_numeros(edades)


def education(lista):
    educacion = []
    for i in lista:
        educacion.append(i['Education'])
    print(educacion)

#que tipos de educacion hay
def tipos_educacion(lista):
    educacion = []
    for i in lista:
        educacion.append(i['Education'])
    print(set(educacion))

#que tipos de ocupacion hay Y CUANTAS
def tipos_ocupacion(lista):
    ocupacion = []
    for i in lista:
        ocupacion.append(i['Occupation'])
    print(set(ocupacion))
    print("Hay un total de",len(set(ocupacion)),"ocupaciones diferentes")

#  crear una lista de diccionarios   con las claves de  first name last name y age  
def lista_diccionarios(lista):
    lista_diccionarios = []
    for i in lista:
        lista_diccionarios.append([{'First Name':i['First Name'],'Last Name':i['Last Name'],'Started working':i['Age']-i['Experience (Years)']}])
    print(lista_diccionarios)

#crear  un diccionario con su ocupacion  y el valor de su salario medio
def salario_medio_ocupacion(lista):
    salario_medio = {}
    for i in lista:
        if i['Occupation'] not in salario_medio:
            salario_medio[i['Occupation']] = [i['Salary']]
        else:
            salario_medio[i['Occupation']].append(i['Salary'])
    for i in salario_medio:
        salario_medio[i] = np.mean(salario_medio[i])
    print(salario_medio)

def salario_medio_educacion(lista):
    salario_medio = {}
    for i in lista:
        if i['Education'] not in salario_medio:
            salario_medio[i['Education']] = [i['Salary']]
        else:
            salario_medio[i['Education']].append(i['Salary'])
    for i in salario_medio:
        salario_medio[i] = np.mean(salario_medio[i])
    print(salario_medio)

# crear una lista de diccionarios donde se guarde la cupacion: doctoral
def lista_diccionarios_ocupacion(lista):
    lista_diccionarios = []
    for i in lista:
        if i['Education'] == 'Doctoral':
            lista_diccionarios.append(i)
    print(lista_diccionarios)

# crear una lista de diccionarios donde se guarde la cupacion: doctoral usando  lambda
def lista_diccionarios_ocupacion_lambda(lista):
    lista_diccionarios = list(filter(lambda x: x['Education'] == 'Doctoral',lista))
    print(lista_diccionarios)    

# crear funcion con lambda con map para  obtener una  lista de cadenas
def lista_cadenas(lista):
    lista_cadenas = list(map(lambda x: x['First Name'] + " "+ x["Last Name"] + ' tiene' + " " + str(x['Age'])+ "  " +"años ",lista))
    print(lista_cadenas)   


## INICIO PROGRAMA
