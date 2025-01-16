from utils import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

s_m_09= pd.read_csv("Data/social_media(09-21).csv", sep=";")#Plación (millones) que usa RRSS en 2009 y 2021
eat_age=pd.read_csv("Data/eat_edad.csv", sep=";")# Porcentaje por edades de población que sufre trastornos alimenticios 2009 y 2021
eat_gen=pd.read_csv("Data/eat_gen.csv", sep=";")# Porcentaje por género de población que sufre trastornos alimenticios 2009 y 2021
dep_age=pd.read_csv("Data/dep_edad.csv", sep=";")# Porcentaje por edades de población que sufre depresión 2009 y 2021
dep_gen=pd.read_csv("Data/dep_gen.csv", sep=";")# Porcentaje por género de población que sufre trastornos depresión 2009 y 2021
test=pd.read_csv("Data/test.csv")

#eliminamos ls filas y columnas que no nos interesan en el estudio
eat_age=eat_age.rename(columns={"Unnamed: 0":"","Unnamed: 2":"","Unnamed: 3":"","Unnamed: 5":"","Unnamed: 6":"","Unnamed: 8":"","Unnamed: 9":"","Unnamed: 11":"","Unnamed: 12":"","Unnamed: 14":"","Unnamed: 15":"","Unnamed: 17":"","Unnamed: 18":"","Unnamed: 21":"","Unnamed: 20":"","Unnamed: 23":"","Unnamed: 24":"","Unnamed: 26":"","Unnamed: 27":""})
arrays1 = [["Country/area","Ages 5-14","Ages 5-14","Ages 5-14","Ages 15-19","Ages 15-19","Ages 15-19", "Ages 20-24", "Ages 20-24", "Ages 20-24", "Ages 25-29", "Ages 25-29", "Ages 25-29","Ages 30-34","Ages 30-34","Ages 30-34", "Ages 35-39", "Ages 35-39", "Ages 35-39","Ages 40-44","Ages 40-44","Ages 40-44","Ages 45-49","Ages 45-49","Ages 45-49", "All ages", "All ages", "All ages"],
    ["","2009", "2021","Relative Change","2009", "2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change"],
]

eat_age=multi_index(arrays1,eat_age)
cols3 = eat_age.columns #seleccionamos todas las columnas
# Limpiar '%' y convertir a float en las columnas seleccionadas
eat_age[cols3] = eat_age[cols3].replace({'%': ''}, regex=True).astype(float)

eat_age.duplicated().sum()
eat_age.info()

eat_gen=eat_gen.rename(columns={"Unnamed: 0":"","Unnamed: 2":"","Unnamed: 3":"","Unnamed: 5":"","Unnamed: 6":"","Unnamed: 8":"","Unnamed: 9":"","Unnamed: 10":""})

arrays2 = [["Country/area","MALE","MALE","MALE","FAMEL","FAMEL","FAMEL","POPULATION","POPULATION","POPULATION","POPULATION"],
    ["","2009", "2021","Relative Change","2009", "2021","Relative Change", "2009", "2021", "Absolute Change","Relative Change"],
]
eat_gen=multi_index(arrays2,eat_gen)
cols2 = eat_gen.columns #seleccionamos todas las columnas
# Limpiar '%' y convertir a float en las columnas seleccionadas
eat_gen[cols2] = eat_gen[cols2].replace({'%': '',',': ''}, regex=True).astype(float)
eat_gen=eat_gen.drop_duplicates()
eat_gen.duplicated().sum()
eat_gen.info()

#eliminamos ls filas y columnas que no nos interesan en el estudio
dep_age=dep_age.rename(columns={"Unnamed: 0":"","Unnamed: 2":"","Unnamed: 3":"","Unnamed: 5":"","Unnamed: 6":"","Unnamed: 8":"","Unnamed: 9":"","Unnamed: 11":"","Unnamed: 12":"","Unnamed: 14":"","Unnamed: 15":"","Unnamed: 17":"","Unnamed: 18":"","Unnamed: 21":"","Unnamed: 20":"","Unnamed: 23":"","Unnamed: 24":"","Unnamed: 26":"","Unnamed: 27":""})
dep_all=dep_age.loc[:,["All ages"]]
dep_age=dep_age.loc[:,:"Ages 50-54"].drop(columns=["Ages 50-54"])
arrays3 = [["Country/area","Ages 5-14","Ages 5-14","Ages 5-14","Ages 15-19","Ages 15-19","Ages 15-19", "Ages 20-24", "Ages 20-24", "Ages 20-24", "Ages 25-29", "Ages 25-29", "Ages 25-29","Ages 30-34","Ages 30-34","Ages 30-34", "Ages 35-39", "Ages 35-39", "Ages 35-39","Ages 40-44","Ages 40-44","Ages 40-44","Ages 45-49","Ages 45-49","Ages 45-49"],
    ["","2009", "2021","Relative Change","2009", "2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change","2009","2021","Relative Change", "2009", "2021","Relative Change"],
]
dep_age=multi_index(arrays3,dep_age)
cols = dep_age.columns #seleccionamos todas las columnas

# Limpiar '%' y convertir a float en las columnas seleccionadas
dep_age[cols] = dep_age[cols].replace('%', '', regex=True).astype(float)

dep_age.duplicated().sum()
dep_age.info()

#eliminamos ls filas y columnas que no nos interesan en el estudio
dep_gen=dep_gen.rename(columns={"Unnamed: 0":"","Unnamed: 2":"","Unnamed: 3":"","Unnamed: 5":"","Unnamed: 6":"","Unnamed: 8":"","Unnamed: 9":"","Unnamed: 10":""})

arrays4 = [["Country/area","MALE","MALE","MALE","FAMEL","FAMEL","FAMEL","POPULATION","POPULATION","POPULATION","POPULATION"],
    ["","2009", "2021","Relative Change","2009", "2021","Relative Change", "2009", "2021", "Absolute Change","Relative Change"],
]
dep_gen=multi_index(arrays4,dep_gen)
cols1 = dep_gen.columns #seleccionamos todas las columnas
# Limpiar '%' y convertir a float en las columnas seleccionadas
dep_gen[cols1] = dep_gen[cols1].replace({'%': '',',': ''}, regex=True).astype(float)
dep_gen=dep_gen.drop_duplicates()
dep_gen.duplicated().sum()
dep_gen.info()

s_m_09= s_m_09.set_index("Country/area")
cols4 = s_m_09.columns #seleccionamos todas las columnas
# Limpiar '%' y convertir a float en las columnas seleccionadas
s_m_09[cols4] =s_m_09[cols4].replace({'%': '',",":""}, regex=True).astype(float)
s_m_09.info()


test.drop(columns="User_ID",inplace=True)
test.info()

'''Agrupacion de paises por contientes'''
cont_paises={"Asia":["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", 
        "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", 
        "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", 
        "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", 
        "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", 
        "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", 
        "Sri Lanka", "Syria","Tajikistan", "Thailand", "Turkey", 
        "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Yemen"],

"Europe":["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", 
        "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", 
        "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", 
        "Israel", "Italy", "Kazakhstan", "Latvia", "Lithuania", 
        "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", 
        "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", 
        "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", 
        "Ukraine", "United Kingdom"],

"Africa":["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cape Verde", 
        "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo", 
        "Democratic Republic of Congo", "Djibouti", "Egypt", "Equatorial Guinea", 
        "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", 
        "Guinea-Bissau", "Cote d'Ivoire", "Kenya", "Lesotho", "Liberia", "Libya", 
        "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", 
        "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", 
        "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", 
        "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],

"North America":["Antigua and Barbuda","Bahamas", "Barbados","Canada", "Cuba", "Costa Rica",
                  "Dominica", "Grenada", "Trinidad and Tobago", "Jamaica", "Panama","Dominican Republic", "United States", "Mexico"],

"South America":["Argentina", "Belize", "Bolivia", 
        "Brazil", "Chile", "Colombia",
         "Ecuador", "El Salvador","Guatemala", "Guyana", 
        "Haiti", "Honduras", "Nicaragua", "Paraguay", "Peru", 
        "Puerto Rico", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
        "Suriname", "Uruguay", "Venezuela"],

"Oceania":["American Samoa", "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia (country)", 
        "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", 
        "Tonga", "Tuvalu", "Vanuatu"
]}
#hago una lista con los continentes que son las claves del diccionario
cont=["Africa", "Asia", "North America", "Oceania", "South America", "Europe"]
'''POBLACIONES DE 2009 Y 2021 POR CONTINENTES'''
#n la columna de POPULATION de los dataset de genero tenemos la población total de cada región
pob_09=dep_gen.loc[["Africa", "Asia", "North America", "Oceania", "South America", "Europe"],("POPULATION","2009")]
pob_21=dep_gen.loc[["Africa", "Asia", "North America", "Oceania", "South America", "Europe"],("POPULATION","2021")]

eat_all=eat_age.loc[:,"All ages"]
eat_age=eat_age.drop(columns="All ages")

#Obtenemos las areas donde se han dado los max valores de depresion en cada edad 
max_21_area=pd.DataFrame((dep_age.loc[dep_age[:]["2021"].idxmax()]).idxmax()).T
max_21_area=max_21_area[:]["2021"]

max_09_area=pd.DataFrame((dep_age.loc[dep_age[:]["2009"].idxmax()]).idxmax()).T
max_09_area=max_09_area[:]["2021"]
#obtenemos el maximo de los datos de 2021 y 2009
max_21=pd.DataFrame(dep_age[:]["2021"].max()).T
max_09=pd.DataFrame(dep_age[:]["2009"].max()).T

#Obtenemos las areas donde se han dado los max valores de desordenes alimenticios en cada edad 
max_21_area_eat=pd.DataFrame((eat_age.loc[eat_age[:]["2021"].idxmax()]).idxmax()).T
max_21_area_eat=max_21_area_eat[:]["2021"]

max_09_area_eat=pd.DataFrame((eat_age.loc[eat_age[:]["2009"].idxmax()]).idxmax()).T
max_09_area_eat=max_09_area_eat[:]["2021"]
#obtenemos el maximo de los datos de 2021 y 2009
max_21_eat=pd.DataFrame(eat_age[:]["2021"].max()).T
max_09_eat=pd.DataFrame(eat_age[:]["2009"].max()).T

display("max_21_eat","max_09_eat","max_21","max_09","max_21_area_eat","max_09_area_eat","max_21_area","max_09_area")

#Obtenemos las areas donde se han dado los  min valores de depresion en cada edad 
min_21_area=pd.DataFrame((dep_age.loc[dep_age[:]["2021"].idxmin()]).idxmin()).T
min_21_area=min_21_area[:]["2021"]

min_09_area=pd.DataFrame((dep_age.loc[dep_age[:]["2009"].idxmin()]).idxmin()).T
min_09_area=min_09_area[:]["2021"]
#obtenemos el minimo de los datos de 2021 y 2009
min_21=pd.DataFrame(dep_age[:]["2021"].min()).T
min_09=pd.DataFrame(dep_age[:]["2009"].min()).T


#Obtenemos las areas donde se han dado los min valores de desordenes alimenticios en cada edad 
min_21_area_eat=pd.DataFrame((eat_age.loc[eat_age[:]["2021"].idxmin()]).idxmin()).T
min_21_area_eat=min_21_area_eat[:]["2021"]

min_09_area_eat=pd.DataFrame((eat_age.loc[eat_age[:]["2009"].idxmin()]).idxmin()).T
min_09_area_eat=min_09_area_eat[:]["2021"]
#obtenemos el minimo de los datos de 2021 y 2009
min_21_eat=pd.DataFrame(eat_age[:]["2021"].min()).T
min_09_eat=pd.DataFrame(eat_age[:]["2009"].min()).T

display("min_21_eat","min_09_eat","min_21","min_09","min_21_area_eat","min_09_area_eat","min_21_area","min_09_area")


dep_age_09=(dep_age.T).xs("2009",level="Measure")
#Traspongo la tabla y creo un nuevo DataFrame con todas las edades, paises y los datos de 2009
dep_age_21=(dep_age.T).xs("2021",level="Measure")

'''Hacemos la media por edades y añadimos la columna a los dataframe'''
#Ponemos que sea hasta "Zimbabwe" para que haga la media de los paises
dep_age_21["media"] = dep_age_21.loc[:, :"Zimbabwe"].mean(axis=1)
dep_age_09["media"]=dep_age_09.loc[:, :"Zimbabwe"].mean(axis='columns')
#Hacemos lo mismo con los max y minimos
dep_age_21["min"]=dep_age_21.loc[:, :"Zimbabwe"].min(axis='columns')
dep_age_09["min"]=dep_age_09.loc[:, :"Zimbabwe"].min(axis='columns')

dep_age_21["max"]=dep_age_21.loc[:, :"Zimbabwe"].max(axis='columns')
dep_age_09["max"]=dep_age_09.loc[:, :"Zimbabwe"].max(axis='columns')

'''Hacemos lo mismo para los desordenes alimenticios'''
eat_age_09=(eat_age.T).xs("2009",level="Measure")
#Traspongo la tabla y creo un nuevo DataFrame con todas las edades, paises y los datos de 2009
eat_age_21=(eat_age.T).xs("2021",level="Measure")
#Hacemos la media por edades y añadimos la columna a los dataframe
eat_age_21["media"] = eat_age_21.loc[:, :"Zimbabwe"].mean(axis=1)
eat_age_09["media"]=eat_age_09.loc[:, :"Zimbabwe"].mean(axis='columns')
#Hacemos lo mismo con los max y minimos
eat_age_21["min"]=eat_age_21.loc[:, :"Zimbabwe"].min(axis='columns')
eat_age_09["min"]=eat_age_09.loc[:, :"Zimbabwe"].min(axis='columns')

eat_age_21["max"]=eat_age_21.loc[:, :"Zimbabwe"].max(axis='columns')
eat_age_09["max"]=eat_age_09.loc[:, :"Zimbabwe"].max(axis='columns')

'''Veamos los mismo estadísticos por género'''
dep_gen_09=(dep_gen[["MALE","FAMEL"]].T).xs("2009",level="Measure")
#Traspongo la tabla y creo un nuevo DataFrame con todas los generos, paises y los datos de 2009
dep_gen_21=(dep_gen[["MALE","FAMEL"]].T).xs("2021",level="Measure")
#Hacemos la media por géneros y añadimos la columna a los dataframe
dep_gen_21_p=(dep_gen_21.loc[:, :"Zimbabwe"]).dropna(axis=1, how='all')#eliminamos los paises sin datos para que no afecte a la media
dep_gen_09_p=(dep_gen_21_p.loc[:, :"Zimbabwe"]).dropna(axis=1, how='all')
dep_gen_21_p["media"]=dep_gen_21_p.mean(axis='columns')
dep_gen_09_p["media"]=dep_gen_09_p.mean(axis='columns')
'''--------Desviación estamdar por continentes---------'''#esto nos va a permitir tener una vision mas acertada del cambio entre un año y otro por contientes
dev_dep_gen_21_p_africa=dep_gen_21_p.loc[:,cont_paises["Africa"]].std()
dev_dep_gen_21_p_asia=dep_gen_21_p.loc[:,cont_paises["Asia"]].std()
dev_dep_gen_21_p_oceania=dep_gen_21_p.loc[:,cont_paises["Oceania"]].std()
dev_dep_gen_21_p_sa=dep_gen_21_p.loc[:,cont_paises["South America"]].std()
dev_dep_gen_21_p_na=dep_gen_21_p.loc[:,cont_paises["North America"]].std()
dev_dep_gen_21_p_eu=dep_gen_21_p.loc[:,cont_paises["Europe"]].std()

dev_dep_gen_09_p_africa=dep_gen_09_p.loc[:,cont_paises["Africa"]].std()
dev_dep_gen_09_p_asia=dep_gen_09_p.loc[:,cont_paises["Asia"]].std()
dev_dep_gen_09_p_oceania=dep_gen_09_p.loc[:,cont_paises["Oceania"]].std()
dev_dep_gen_09_p_sa=dep_gen_09_p.loc[:,cont_paises["South America"]].std()
dev_dep_gen_09_p_na=dep_gen_09_p.loc[:,cont_paises["North America"]].std()
dev_dep_gen_09_p_eu=dep_gen_09_p.loc[:,cont_paises["Europe"]].std()

dev_dep_age_21_p_africa=dep_age_21.loc[:,cont_paises["Africa"]].std()
dev_dep_age_21_p_asia=dep_age_21.loc[:,cont_paises["Asia"]].std()
dev_dep_age_21_p_oceania=dep_age_21.loc[:,cont_paises["Oceania"]].std()
dev_dep_age_21_p_sa=dep_age_21.loc[:,cont_paises["South America"]].std()
dev_dep_age_21_p_na=dep_age_21.loc[:,cont_paises["North America"]].std()
dev_dep_age_21_p_eu=dep_age_21.loc[:,cont_paises["Europe"]].std()

dev_dep_age_09_p_africa=dep_age_09.loc[:,cont_paises["Africa"]].std()
dev_dep_age_09_p_asia=dep_age_09.loc[:,cont_paises["Asia"]].std()
dev_dep_age_09_p_oceania=dep_age_09.loc[:,cont_paises["Oceania"]].std()
dev_dep_age_09_p_sa=dep_age_09.loc[:,cont_paises["South America"]].std()
dev_dep_age_09_p_na=dep_age_09.loc[:,cont_paises["North America"]].std()
dev_dep_age_09_p_eu=dep_age_09.loc[:,cont_paises["Europe"]].std()
'''-----------------'''
#Hacemos lo mismo con los max y minimos
dep_gen_21_p["min"]=dep_gen_21_p.min(axis='columns')
dep_gen_09_p["min"]=dep_gen_09_p.min(axis='columns')

dep_gen_21_p["max"]=dep_gen_21_p.max(axis='columns')
dep_gen_09_p["max"]=dep_gen_09_p.max(axis='columns')

'''Hacemos el mismo procedimiento con eat_gen'''
eat_gen_09=(eat_gen[["MALE","FAMEL"]].T).xs("2009",level="Measure")
#Traspongo la tabla y creo un nuevo DataFrame con todas los generos, paises y los datos de 2009
eat_gen_21=(eat_gen[["MALE","FAMEL"]].T).xs("2021",level="Measure")

eat_gen_21_p=(eat_gen_21.loc[:, :"Zimbabwe"]).dropna(axis=1, how='all')#eliminamos los paises sin datos para que no afecte a la media
eat_gen_09_p=(eat_gen_09.loc[:, :"Zimbabwe"]).dropna(axis=1, how='all')
#Hacemos la media por géneros y añadimos la columna a los dataframe
eat_gen_21_p["media"]=eat_gen_21_p.mean(axis='columns')
eat_gen_09_p["media"]=eat_gen_09_p.mean(axis='columns')
#Hacemos lo mismo con los max y minimos
eat_gen_21_p["min"]=eat_gen_21_p.min(axis='columns')
eat_gen_09_p["min"]=eat_gen_09_p.min(axis='columns')

eat_gen_21_p["max"]=eat_gen_21_p.max(axis='columns')
eat_gen_09_p["max"]=eat_gen_09_p.max(axis='columns')

'''--------Desviación estamdar por continentes---------'''
dev_eat_gen_21_p_africa=eat_gen_21_p.loc[:,cont_paises["Africa"]].std()
dev_eat_gen_21_p_asia=eat_gen_21_p.loc[:,cont_paises["Asia"]].std()
dev_eat_gen_21_p_oceania=eat_gen_21_p.loc[:,cont_paises["Oceania"]].std()
dev_eat_gen_21_p_sa=eat_gen_21_p.loc[:,cont_paises["South America"]].std()
dev_eat_gen_21_p_na=eat_gen_21_p.loc[:,cont_paises["North America"]].std()
dev_eat_gen_21_p_eu=eat_gen_21_p.loc[:,cont_paises["Europe"]].std()

dev_eat_gen_09_p_africa=eat_gen_09_p.loc[:,cont_paises["Africa"]].std()
dev_eat_gen_09_p_asia=eat_gen_09_p.loc[:,cont_paises["Asia"]].std()
dev_eat_gen_09_p_oceania=eat_gen_09_p.loc[:,cont_paises["Oceania"]].std()
dev_eat_gen_09_p_sa=eat_gen_09_p.loc[:,cont_paises["South America"]].std()
dev_eat_gen_09_p_na=eat_gen_09_p.loc[:,cont_paises["North America"]].std()
dev_eat_gen_09_p_eu=eat_gen_09_p.loc[:,cont_paises["Europe"]].std()
'''-----------------------------'''
dev_eat_age_21_p_africa=eat_age_21.loc[:,cont_paises["Africa"]].std()
dev_eat_age_21_p_asia=eat_age_21.loc[:,cont_paises["Asia"]].std()
dev_eat_age_21_p_oceania=eat_age_21.loc[:,cont_paises["Oceania"]].std()
dev_eat_age_21_p_sa=eat_age_21.loc[:,cont_paises["South America"]].std()
dev_eat_age_21_p_na=eat_age_21.loc[:,cont_paises["North America"]].std()
dev_eat_age_21_p_eu=eat_age_21.loc[:,cont_paises["Europe"]].std()

dev_eat_age_09_p_africa=eat_age_09.loc[:,cont_paises["Africa"]].std()
dev_eat_age_09_p_asia=eat_age_09.loc[:,cont_paises["Asia"]].std()
dev_eat_age_09_p_oceania=eat_age_09.loc[:,cont_paises["Oceania"]].std()
dev_eat_age_09_p_sa=eat_age_09.loc[:,cont_paises["South America"]].std()
dev_eat_age_09_p_na=eat_age_09.loc[:,cont_paises["North America"]].std()
dev_eat_age_09_p_eu=eat_age_09.loc[:,cont_paises["Europe"]].std()

a=pd.concat([eat_age_09["World"].T, eat_age_21["World"].T],axis=1)
a.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar a nivel mundial por años")
plt.legend(labels=["2009","2021"]);

x=pd.concat([eat_age_09["Africa"].T, eat_age_21["Africa"].T],axis=1)
x.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en Africa por año")
plt.legend(labels=["2009","2021"]);

asi=pd.concat([eat_age_09["Asia"].T, eat_age_21["Asia"].T],axis=1)
asi.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en Asia por año")
plt.legend(labels=["2009","2021"]);

x=pd.concat([eat_age_09["Oceania"].T, eat_age_21["Oceania"].T],axis=1)
x.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en Oceania por año")
plt.legend(labels=["2009","2021"]);

x=pd.concat([eat_age_09["Europe"].T, eat_age_21["Europe"].T],axis=1)
x.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en Europa por año")
plt.legend(labels=["2009","2021"]);

x=pd.concat([eat_age_09["North America"].T, eat_age_21["North America"].T],axis=1)
x.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en N.America por año")
plt.legend(labels=["2009","2021"]);

x=pd.concat([eat_age_09["South America"].T, eat_age_21["South America"].T],axis=1)
x.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en S.America por año")
plt.legend(labels=["2009","2021"]);

x=pd.concat([dev_eat_age_09_p_eu.T, dev_eat_age_21_p_eu.T],axis=1)
x.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Paises")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar en paises de Europa por año")
plt.legend(labels=["2009","2021"]);

a=pd.concat([dep_age_09["World"].T, dep_age_21["World"].T],axis=1)
a.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Edades")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar a nivel mundial por años")
plt.legend(labels=["2009","2021"]);

a=pd.concat([eat_gen_09["World"].T, eat_gen_21["World"].T],axis=1)
a.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Géneros")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar a nivel mundial por géneros - T.Alimenticios")
plt.legend(labels=["2009","2021"]);

a=pd.concat([dep_gen_09["World"].T, dep_gen_21["World"].T],axis=1)
a.plot(kind='bar', width=0.8, figsize=(10, 6), color=["blue", "orange"])
# Configurar etiquetas y título
plt.xlabel("Géneros")
plt.ylabel("Desviación estándar (%)")
plt.title("Desviación estándar a nivel mundial por años - Depresión")
plt.legend(labels=["2009","2021"]);

color=["#B0E0E6","#DDA0DD"]
color2=["#00BFFF","#FF1493"]
colors=["#00CED1","#FFB6C1"]
colors2=["#000080","#FF00FF"]
col_F="#FFB6C1"
col_M="#00CED1"


f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

'''Depresión por género 2009-21'''
axes[0].barh(y=dep_gen_21_p.index, width=dep_gen_21_p["media"],color=colors,label=["M 2021","F 2021"]);
axes[0].barh(y=dep_gen_09_p.index, width=dep_gen_09_p["media"],color=colors2,label =["M 2009","F 2009"]);
axes[0].set_title("MEDIA Depresión por año y género");
axes[0].legend();
'''Depresión por edad 2009-21'''
axes[1].barh(y=dep_age_21.index, width=dep_age_21["media"],color=["green"],label="media 2021");
axes[1].barh(y=dep_age_09.index, width=dep_age_09["media"],color=["purple"],label ="media 2009");
axes[1].set_title("MEDIA Depresión por año y edades");
axes[1].legend();

f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

'''Desordenes alimenticios por género 2009-21'''
axes[1].barh(y=eat_gen_21_p.index, width=eat_gen_21_p["media"],color=color,label=["M 2021","F 2021"]);
axes[1].barh(y=eat_gen_09_p.index, width=eat_gen_09_p["media"],color=color2,label =["M 2009","F 2009"]);
axes[1].set_title("MEDIA T. Alimenticios por año y género");
axes[1].legend();

'''Desordenes alimenticios por edad 2009-21'''
axes[0].barh(y=eat_age_21.index, width=eat_age_21["media"],color="#FF8C00",label="media 2021");
axes[0].barh(y=eat_age_09.index, width=eat_age_09["media"],color="#008080",label ="media 2009");
axes[0].set_title("MEDIA T. Alimenticios por año y edades")
axes[0].legend();


'''MAXIMOS'''
f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)


'''Desordenes alimenticios por edad 2009-21'''

axes[0].barh(y=eat_age_09.index, width=eat_age_09["min"],color="#008080",label ="min 2009");
axes[0].barh(y=eat_age_21.index, width=eat_age_21["min"],color="#FF8C00",label="min 2021");
axes[0].set_title("MIN Des. Alimenticios por año y edades")
axes[0].legend();


'''Desordenes alimenticios por edad 2009-21'''
axes[1].barh(y=eat_age_21.index, width=eat_age_21["max"],color="#FF8C00",label="max 2021");
axes[1].barh(y=eat_age_09.index, width=eat_age_09["max"],color="#008080",label ="max 2009");
axes[1].set_title("MAX Des. Alimenticios por año y edades")
axes[1].legend();
f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)


'''Depresión por edad 2009-21'''
axes[0].barh(y=dep_age_21.index, width=dep_age_21["min"],color=["green"],label="min 2021");
axes[0].barh(y=dep_age_09.index, width=dep_age_09["min"],color=["purple"],label ="min 2009");
axes[0].set_title("MIN Depresión por año y edades");
axes[0].legend();
'''Depresión por edad 2009-21'''
axes[1].barh(y=dep_age_21.index, width=dep_age_21["max"],color=["green"],label="max 2021");
axes[1].barh(y=dep_age_09.index, width=dep_age_09["max"],color=["purple"],label ="max 2009");
axes[1].set_title("MAX Depresión por año y edades");
axes[1].legend();

'''MINIMOS'''
f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

'''Desordenes alimenticios por género 2009-21'''

axes[1].barh(y=eat_gen_09_p.index, width=eat_gen_09_p["min"],color=color2,label =["M 2009","F 2009"]);
axes[1].barh(y=eat_gen_21_p.index, width=eat_gen_21_p["min"],color=color,label=["M 2021","F 2021"]);
axes[1].set_title("MIN Des. Alimenticios por año y género");
axes[1].legend();
'''Desordenes alimenticios por género 2009-21'''
axes[0].barh(y=eat_gen_21_p.index, width=eat_gen_21_p["max"],color=color,label=["M 2021","F 2021"]);
axes[0].barh(y=eat_gen_09_p.index, width=eat_gen_09_p["max"],color=color2,label =["M 2009","F 2009"]);
axes[0].set_title("MAX Des. Alimenticios por año y género");
axes[0].legend();

f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

'''Depresión por género 2009-21'''
axes[0].barh(y=dep_gen_21_p.index, width=dep_gen_21_p["min"],color=colors,label=["M 2021","F 2021"]);
axes[0].barh(y=dep_gen_09_p.index, width=dep_gen_09_p["min"],color=colors2,label =["M 2009","F 2009"]);
axes[0].set_title("MIN Depresión por año y género");
axes[0].legend();
'''Depresión por género 2009-21'''
axes[1].barh(y=dep_gen_09_p.index, width=dep_gen_09_p["max"],color=colors2,label =["M 2009","F 2009"]);
axes[1].barh(y=dep_gen_21_p.index, width=dep_gen_21_p["max"],color=colors,label=["M 2021","F 2021"]);
axes[1].set_title("MAX Depresión por año y género");
axes[1].legend();



dep_gen["male_09"] = (dep_gen[("MALE", "2009")] * dep_gen[("POPULATION", "2009")]) / 100
dep_gen["famel_09"] = (dep_gen[("FAMEL", "2009")] * dep_gen[("POPULATION", "2009")]) / 100
dep_gen["male_21"] = (dep_gen[("MALE", "2021")] * dep_gen[("POPULATION", "2021")]) / 100
dep_gen["famel_21"] = (dep_gen[("FAMEL", "2021")] * dep_gen[("POPULATION", "2021")]) / 100

eat_gen["male_09"] = (eat_gen[("MALE", "2009")] * eat_gen[("POPULATION", "2009")]) / 100
eat_gen["famel_09"] = (eat_gen[("FAMEL", "2009")] * eat_gen[("POPULATION", "2009")]) / 100
eat_gen["male_21"] = (eat_gen[("MALE", "2021")] * eat_gen[("POPULATION", "2021")]) / 100
eat_gen["famel_21"] = (eat_gen[("FAMEL", "2021")] * eat_gen[("POPULATION", "2021")]) / 100

'''2009'''
medias_f_09_num=calcular_medias_num(dep_gen,"famel_09",cont,cont_paises)
dep_F_09_num = pd.DataFrame({"Country/area": cont, "Famel_09": medias_f_09_num}).set_index("Country/area")

medias_M_09_num=calcular_medias_num(dep_gen,"male_09",cont,cont_paises)
dep_M_09_num = pd.DataFrame({"Country/area": cont, "Male_09": medias_M_09_num}).set_index("Country/area")

'''2021'''
medias_F_21_num=calcular_medias_num(dep_gen,"famel_21",cont,cont_paises)
dep_F_21_num = pd.DataFrame({"Country/area": cont, "Famel_21": medias_F_21_num}).set_index("Country/area")

medias_M_21_num=calcular_medias_num(dep_gen,"male_21",cont,cont_paises)
dep_M_21_num = pd.DataFrame({"Country/area": cont, "Male_21": medias_M_21_num}).set_index("Country/area")
'''2009'''
med_f_09_num=calcular_medias_num(eat_gen,"famel_09",cont,cont_paises)
eat_F_09_num = pd.DataFrame({"Country/area": cont, "Famel_09": med_f_09_num}).set_index("Country/area")

med_M_09_num=calcular_medias_num(eat_gen,"male_09",cont,cont_paises)
eat_M_09_num = pd.DataFrame({"Country/area": cont, "Male_09": med_M_09_num}).set_index("Country/area")

'''2021'''
med_F_21_num=calcular_medias_num(eat_gen,"famel_21",cont,cont_paises)
eat_F_21_num = pd.DataFrame({"Country/area": cont, "Famel_21": med_F_21_num}).set_index("Country/area")

med_M_21_num=calcular_medias_num(eat_gen,"male_21",cont,cont_paises)
eat_M_21_num = pd.DataFrame({"Country/area": cont, "Male_21": med_M_21_num}).set_index("Country/area")

'''De cada año seleccionamos solo los continentes'''
continentes=["Africa","Asia","North America","Oceania","South America","Europe"]

s_m_cont_años=s_m_09.loc[["Africa","Asia","North America","Oceania","South America","Europe"],["2009","2021"]]
s_m_cont_años=s_m_cont_años.rename(columns={"2009":"2009_RS","2021":"2021_RS"})

'''Analizamos los datos clasificando los paises por su nivel economico'''
dep_gen_icm= dep_gen.loc[["High-income countries","Upper-middle-income countries","Lower-middle-income countries","Low-income countries"]]
dep_age_icm= dep_age.loc[["High-income countries","Upper-middle-income countries","Lower-middle-income countries","Low-income countries"]]

'''Lo mismo para eat_gen'''
eat_gen_icm= eat_gen.loc[["High-income countries","Upper-middle-income countries","Lower-middle-income countries","Low-income countries"]]
eat_age_icm= eat_age.loc[["High-income countries","Upper-middle-income countries","Lower-middle-income countries","Low-income countries"]]

'''Evolución de las Redes de 2009 a 2021'''
s_m_icm= s_m_09.loc[["High-income countries","Upper-middle-income countries","Lower-middle-income countries","Low-income countries"],["2009","2021"]]
#Separamos en distintos DataFram por años

'''Volvemos a separar los dato en dos dataFrame distintos por años'''
dep_gen_icm_09=(dep_gen_icm.T).xs("2009",level="Measure")
dep_gen_icm_21=(dep_gen_icm.T).xs("2021",level="Measure")
dep_age_icm_09=(dep_age_icm.T).xs("2009",level="Measure")
dep_age_icm_21=(dep_age_icm.T).xs("2021",level="Measure")
'''eat_gen'''
eat_gen_icm_09=(eat_gen_icm.T).xs("2009",level="Measure")
eat_gen_icm_21=(eat_gen_icm.T).xs("2021",level="Measure")
eat_age_icm_09=(eat_age_icm.T).xs("2009",level="Measure")
eat_age_icm_21=(eat_age_icm.T).xs("2021",level="Measure")
'''Redes sociales'''
s_m_icm_09=(s_m_icm.loc[:,["2009"]]).T
s_m_icm_21=(s_m_icm.loc[:,["2021"]]).T

fig, axes = plt.subplots(2, 2, figsize=(10, 5))
data_f=(eat_gen_icm_21.T)["FAMEL"]

# Crear el gráfico de pastel
axes[0,0].pie(data_f,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle_f=plt.Circle( (0,0), 0.5, color='white')
axes[0,0].add_artist(circle_f)
axes[0,0].set_title("Desórdenes alimenticios F/€");

data_m=(eat_gen_icm_21.T)["MALE"]


# Crear el gráfico de pastel
axes[0,1].pie(data_m,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle_m=plt.Circle( (0,0), 0.5, color='white')
axes[0,1].add_artist(circle_m)
axes[0,1].set_title("Desórdenes alimenticios M/€");

data=(dep_gen_icm_21.T)["FAMEL"]

axes[1,0].pie(data_f,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle_f=plt.Circle( (0,0), 0.5, color='white')
axes[1,0].add_artist(circle_f)
axes[1,0].set_title("Depresión F/€");


data_m=(dep_gen_icm_21.T)["MALE"]


# Crear el gráfico de pastel
axes[1,1].pie(data_m,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle_m=plt.Circle( (0,0), 0.5, color='white')
axes[1,1].add_artist(circle_m)
axes[1,1].set_title("Depresión M/€");

labels = data.index
fig.legend(labels=labels,title="2021",loc='center')

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 5))
data_f=(eat_gen_icm_09.T)["FAMEL"]

# Crear el gráfico de pastel
axes[0,0].pie(data_f,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle_f=plt.Circle( (0,0), 0.5, color='white')
axes[0,0].add_artist(circle_f)
axes[0,0].set_title("Desórdenes alimenticios F/€");

data_m=(eat_gen_icm_09.T)["MALE"]


# Crear el gráfico de pastel
axes[0,1].pie(data_m,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle_m=plt.Circle( (0,0), 0.5, color='white')
axes[0,1].add_artist(circle_m)
axes[0,1].set_title("Desórdenes alimenticios M/€");

data1=(dep_gen_icm_09.T)["FAMEL"]

axes[1,0].pie(data1,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle1=plt.Circle( (0,0), 0.5, color='white')
axes[1,0].add_artist(circle1)
axes[1,0].set_title("Depresión F/€");


data2=(dep_gen_icm_09.T)["MALE"]


# Crear el gráfico de pastel
axes[1,1].pie(data2,autopct = '%1.2f%%')
# add a circle at the center to transform it in a donut chart
circle2=plt.Circle( (0,0), 0.5, color='white')
axes[1,1].add_artist(circle2)
axes[1,1].set_title("Depresión M/€");

labels = data.index
fig.legend(labels=labels,title="2009",loc='center')

plt.tight_layout()
plt.show()

f, axes = plt.subplots(2, 1, figsize=(12,12), sharex=True)

'''Desordenes alimenticios por género 2009-21'''
axes[0].barh(y=eat_gen_icm_21.columns, width=eat_gen_icm_21.T["FAMEL"],color="#FF00FF",label="F 2021");
axes[0].barh(y=eat_gen_icm_21.columns, width=eat_gen_icm_21.T["MALE"],color="#000080",label ="M 2021");
axes[0].set_title("Trastornos alimenticios por género y € en 2021");
axes[0].legend();
axes[1].barh(y=eat_gen_icm_09.columns, width=eat_gen_icm_09.T["FAMEL"],color="#FF00FF",label="F 2009");
axes[1].barh(y=eat_gen_icm_09.columns, width=eat_gen_icm_09.T["MALE"],color="#000080",label ="M 2009");
axes[1].set_title("Trastornos alimenticios por género y € en 2009");
axes[1].legend();


f, axes = plt.subplots(2, 1, figsize=(12,12), sharex=True)


axes[1].barh(y=dep_gen_icm_21.columns, width=dep_gen_icm_21.T["FAMEL"],color=col_F,label="F 2021");
axes[1].barh(y=dep_gen_icm_21.columns, width=dep_gen_icm_21.T["MALE"],color=col_M,label ="M 2021");
axes[1].set_title("Depresión por género y € en 2021");
axes[1].legend();
axes[0].barh(y=dep_gen_icm_09.columns, width=dep_gen_icm_09.T["FAMEL"],color=col_F,label="F 2009");
axes[0].barh(y=dep_gen_icm_09.columns, width=dep_gen_icm_09.T["MALE"],color=col_M,label ="M 2009");
axes[0].set_title("Depresión por género y € en 2009")
axes[0].legend();

axes[1].set_xlabel("Porcentaje de la población");

x = np.arange(len(dep_age_icm_21))  # Posiciones para los rangos de edad
width = 0.2 
fig, ax = plt.subplots(figsize=(10, 6))

for i, col in enumerate(dep_age_icm_21.columns):
    ax.bar(x + i * width, dep_age_icm_21[col], width, label=col)
ax.set_xlabel('Rangos de Edad')
ax.set_ylabel('Porcentaje de Depresión (%)')
ax.set_title('Porcentaje de Depresión por Edad y Clasificación Económica 2021')
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(eat_age_icm_21.index, rotation=45)
ax.legend(title='Clasificación Económica')

fig, ax = plt.subplots(figsize=(10, 6))

for i, col in enumerate(dep_age_icm_09.columns):
    ax.bar(x + i * width, dep_age_icm_09[col], width, label=col)
ax.set_xlabel('Rangos de Edad')
ax.set_ylabel('Porcentaje de Depresión (%)')
ax.set_title('Porcentaje de Depresión por Edad y Clasificación Económica 2009')
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(eat_age_icm_09.index, rotation=45)
ax.legend(title='Clasificación Económica')

x = np.arange(len(eat_age_icm_09))
width = 0.2  # Ancho de las barras
colores_3= ["#00CED1", "#FFB6C1", "#008080", "#FF8C00"]  

fig, ax = plt.subplots(figsize=(12, 8))

# Agregar barras para cada clasificación económica en 2021
for i, col in enumerate(eat_age_icm_21.columns):
    ax.bar(x + i * width + width, eat_age_icm_21[col], width, label=f"{col} 2021", color=colores_3[i])

ax.set_xlabel('Rangos de Edad')
ax.set_ylabel('Porcentaje de Trastornos alimenticios (%)')
ax.set_title('Porcentaje de D.Alimenticios por edad y Clasificación Económica 2021')
ax.set_xticks(x)
ax.set_xticklabels(eat_age_icm_21.index, rotation=45)
ax.legend(title='Clasificación Económica')


fig, ax = plt.subplots(figsize=(12, 8))
# Agregar barras para cada clasificación económica en 2020
for i, col in enumerate(eat_age_icm_09.columns):
    ax.bar(x + i * width - width, eat_age_icm_09[col], width, label=f"{col} 2009", color=colores_3[i])



ax.set_xlabel('Rangos de Edad')
ax.set_ylabel('Porcentaje de Trastornos alimenticios (%)')
ax.set_title('Porcentaje de D.Alimenticios por edad y Clasificación Económica 2009')
ax.set_xticks(x)
ax.set_xticklabels(eat_age_icm_09.index, rotation=45)
ax.legend(title='Clasificación Económica')

'''DEP'''
plt.figure(figsize=(10,10))
plt.barh(y=dep_gen_icm_21.columns, width=dep_gen_icm_21.T["FAMEL"],color=col_F,label="F 2021");
plt.barh(y=dep_gen_icm_09.columns, width=dep_gen_icm_09.T["FAMEL"],color="#FF00FF",label="F 2009");
plt.barh(y=dep_gen_icm_21.columns, width=dep_gen_icm_21.T["MALE"],color=col_M,label ="M 2021");
plt.barh(y=dep_gen_icm_09.columns, width=dep_gen_icm_09.T["MALE"],color="#000080",label ="M 2009");
plt.legend(title="Depresión 09/21 entre F/M", loc="upper right",bbox_to_anchor=(1,0.5));
plt.xlabel("Porcentaje de población")

'''EAT'''
plt.barh(y=eat_gen_icm_09.columns, width=eat_gen_icm_09.T["FAMEL"],color="#FF00FF",label="F 2009");
plt.barh(y=eat_gen_icm_21.columns, width=eat_gen_icm_21.T["FAMEL"],color=col_F,label="F 2021");

plt.barh(y=eat_gen_icm_09.columns, width=eat_gen_icm_09.T["MALE"],color="#000080",label ="M 2009");
plt.barh(y=eat_gen_icm_21.columns, width=eat_gen_icm_21.T["MALE"],color=col_M,label ="M 2021");

plt.legend(title="Trastornos alimenticios 09/21 entre F/M");
plt.xlabel("Porcentaje de población")

s_m=s_m_09.T.loc[["2009","2021"],:"Zimbabwe"]
s_m["media"]=s_m.T.mean()
s_m["min"]=s_m.T.min()
s_m["max"]=s_m.T.max()
plt.figure(figsize=(5,3))
plt.barh(y=s_m.index, width=s_m["media"],color=["#9ACD32","#9467bd"],label =["2009","2021"]);
plt.legend(title="Media del uso de la resdes sociales");

s_m_continent=s_m_09.T.loc[["2009","2021"],["Africa","Asia","North America","Oceania","South America","Europe"]]
s_m_continent_09=s_m_09.T.loc[["2009"],["Africa","Asia","North America","Oceania","South America","Europe"]]
s_m_continent_21=s_m_09.T.loc[["2021"],["Africa","Asia","North America","Oceania","South America","Europe"]]

c=pd.concat([dep_M_09_num.T,dep_M_21_num.T]).T
z=pd.concat([dep_F_09_num.T,dep_F_21_num.T]).T
z["suma09"]=z["Famel_09"]+c["Male_09"]
c["suma21"]=z["Famel_21"]+c["Male_21"]
c=c.drop(columns=["Male_09","Male_21"])
z=z.drop(columns=["Famel_09","Famel_21"])
dep_sum=pd.concat([z,c],axis=1).T


q=pd.concat([eat_M_09_num.T,eat_M_21_num.T]).T
l=pd.concat([eat_F_09_num.T,eat_F_21_num.T]).T
l["suma09"]=l["Famel_09"]+q["Male_09"]
q["suma21"]=l["Famel_21"]+q["Male_21"]
q=q.drop(columns=["Male_09","Male_21"])
l=l.drop(columns=["Famel_09","Famel_21"])
eat_sum=pd.concat([l,q],axis=1).T

plt.figure(figsize=(6,4))
'''Vamos a ver la evolución de las redes sociales en los ultimos años por continentes. Así podremos compararlo con la gráfica de aumneto de depresión por continentes'''

for column in s_m_continent.columns:
    plt.plot(s_m_continent.index, s_m_continent[column], marker='o', label=column)

# Personalizar el gráfico
plt.title("Evolución del uso de redes sociales por continentes (2009-2021)", fontsize=16)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Usuarios (mil millones)", fontsize=12)
plt.legend(title="Continentes")

plt.figure(figsize=(6,4))
'''Desordenes alimenticios por género(population) 2009-21'''
for column in eat_sum.columns:
    plt.plot(eat_sum.index,eat_sum[column], marker='o', label=column)

# Personalizar el gráfico
plt.title("Evolución del transtorno alimenticio por continentes (2009-2021)", fontsize=16)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Usuarios", fontsize=12)
plt.legend(title="Continentes")


plt.figure(figsize=(6,4))
'''Depresión por género(population) 2009-21'''
for column in dep_sum.columns:
    plt.plot(dep_sum.index, dep_sum[column], marker='o', label=column)

# Personalizar el gráfico
plt.title("Evolución del transtorno depresivo por continentes  (2009-2021)", fontsize=16)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Usuarios (millones)", fontsize=12)
plt.legend(title="Continentes")

corr_RS_dep_gen=pd.concat([dep_sum.T,s_m_cont_años],axis=1)

plt.figure(figsize=(5,5))
sns.heatmap(corr_RS_dep_gen.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(14, 145, s=80, l=25, n=8),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión y Uso de Redes Sociales (2009 vs 2021)");

corr_RS_eat_gen=pd.concat([eat_sum.T,s_m_cont_años],axis=1)

plt.figure(figsize=(5,5))
sns.heatmap(corr_RS_eat_gen.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(14, 145, s=80, l=25, n=8),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T. Alimenticio y Uso de Redes Sociales (2009 vs 2021)");

p_eat_09=test_corr(0.64,6)
p_eat_21=test_corr(0.66,6)

p_dep_09=test_corr(0.92,6)
p_dep_21=test_corr(0.86,6)

print(f"p_value depresión 2009: {round(p_dep_09,2)}")
print(f"p_value depresión 2021: {round(p_dep_21,2)}")
print(f"p_value t. alimenticios 2009: {round(p_eat_09,2)}")
print(f"p_value t. alimenticios 2021: {round(p_eat_21,2)}")

c=pd.concat([dep_M_09_num.T,dep_M_21_num.T]).T
z=pd.concat([dep_F_09_num.T,dep_F_21_num.T]).T
c1=pd.concat([eat_M_09_num.T,eat_M_21_num.T]).T
z1=pd.concat([eat_F_09_num.T,eat_F_21_num.T]).T
RS_dep_09=pd.concat([c["Male_09"],z["Famel_09"],s_m_cont_años[["2009_RS"]]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(RS_dep_09.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión y Uso de Redes Sociales 2009 ");
RS_dep_21=pd.concat([c["Male_21"],z["Famel_21"],s_m_cont_años[["2021_RS"]]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(RS_dep_21.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión y Uso de Redes Sociales 2021");
RS_eat_09=pd.concat([c1["Male_09"],z1["Famel_09"],s_m_cont_años[["2009_RS"]]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(RS_eat_09.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T. alimenticios y Uso de Redes Sociales 2009 ");
RS_eat_21=pd.concat([c1["Male_21"],z1["Famel_21"],s_m_cont_años[["2021_RS"]]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(RS_eat_21.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T. alimenticios y Uso de Redes Sociales 2021");

p_eat_09_M=test_corr(0.74,6)
p_eat_21_M=test_corr(0.72,6)
p_eat_09_F=test_corr(0.57,6)
p_eat_21_F=test_corr(0.63,6)

p_dep_09_M=test_corr(0.86,6)
p_dep_21_M=test_corr(0.94,6)
p_dep_09_F=test_corr(0.85,6)
p_dep_21_F=test_corr(0.90,6)

print(f"p_value depresión 2009 M: {round(p_dep_09_M,2)}")
print(f"p_value depresión 2021 M: {round(p_dep_21_M,2)}")
print(f"p_value t. alimenticios 2009 M: {round(p_eat_09_M,2)}")
print(f"p_value t. alimenticios 2021 M: {round(p_eat_21_M,2)}")
print(f"p_value depresión 2009 F: {round(p_dep_09_F,2)}")
print(f"p_value depresión 2021 F: {round(p_dep_21_F,2)}")
print(f"p_value t. alimenticios 2009 F: {round(p_eat_09_F,2)}")
print(f"p_value t. alimenticios 2021 F: {round(p_eat_21_F,2)}")

'''Hacemos una separación de los datos de depresión por géneros según los paises de cada continente '''
dep_f_21_africa=(dep_gen.T).loc["famel_21",cont_paises["Africa"]].rename(index={"":"famel_21"})
dep_f_21_asia=(dep_gen.T).loc["famel_21",cont_paises["Asia"]].rename(index={"":"famel_21"})
dep_f_21_oceania=(dep_gen.T).loc["famel_21",cont_paises["Oceania"]].rename(index={"":"famel_21"})
dep_f_21_sa=(dep_gen.T).loc["famel_21",cont_paises["South America"]].rename(index={"":"famel_21"})
dep_f_21_na=(dep_gen.T).loc["famel_21",cont_paises["North America"]].rename(index={"":"famel_21"})
dep_f_21_eu=(dep_gen.T).loc["famel_21",cont_paises["Europe"]].rename(index={"":"famel_21"})

dep_m_21_africa=(dep_gen.T).loc["male_21",cont_paises["Africa"]].rename(index={"":"male_21"})
dep_m_21_asia=(dep_gen.T).loc["male_21",cont_paises["Asia"]].rename(index={"":"male_21"})
dep_m_21_oceania=(dep_gen.T).loc["male_21",cont_paises["Oceania"]].rename(index={"":"male_21"})
dep_m_21_sa=(dep_gen.T).loc["male_21",cont_paises["South America"]].rename(index={"":"male_21"})
dep_m_21_na=(dep_gen.T).loc["male_21",cont_paises["North America"]].rename(index={"":"male_21"})
dep_m_21_eu=(dep_gen.T).loc["male_21",cont_paises["Europe"]].rename(index={"":"male_21"})

dep_f_09_africa=(dep_gen.T).loc["famel_09",cont_paises["Africa"]].rename(index={"":"famel_09"})
dep_f_09_asia=(dep_gen.T).loc["famel_09",cont_paises["Asia"]].rename(index={"":"famel_09"})
dep_f_09_oceania=(dep_gen.T).loc["famel_09",cont_paises["Oceania"]].rename(index={"":"famel_09"})
dep_f_09_sa=(dep_gen.T).loc["famel_09",cont_paises["South America"]].rename(index={"":"famel_09"})
dep_f_09_na=(dep_gen.T).loc["famel_09",cont_paises["North America"]].rename(index={"":"famel_09"})
dep_f_09_eu=(dep_gen.T).loc["famel_09",cont_paises["Europe"]].rename(index={"":"famel_09"})

dep_m_09_africa=(dep_gen.T).loc["male_09",cont_paises["Africa"]].rename(index={"":"male_09"})
dep_m_09_asia=(dep_gen.T).loc["male_09",cont_paises["Asia"]].rename(index={"":"male_09"})
dep_m_09_oceania=(dep_gen.T).loc["male_09",cont_paises["Oceania"]].rename(index={"":"male_09"})
dep_m_09_sa=(dep_gen.T).loc["male_09",cont_paises["South America"]].rename(index={"":"male_09"})
dep_m_09_na=(dep_gen.T).loc["male_09",cont_paises["North America"]].rename(index={"":"male_09"})
dep_m_09_eu=(dep_gen.T).loc["male_09",cont_paises["Europe"]].rename(index={"":"male_09"})

'''Hacemos los mismo para trastornos alimneticios por generos'''
eat_f_21_africa=(eat_gen.T).loc["famel_21",cont_paises["Africa"]].rename(index={"":"famel_21"})
eat_f_21_asia=(eat_gen.T).loc["famel_21",cont_paises["Asia"]].rename(index={"":"famel_21"})
eat_f_21_oceania=(eat_gen.T).loc["famel_21",cont_paises["Oceania"]].rename(index={"":"famel_21"})
eat_f_21_sa=(eat_gen.T).loc["famel_21",cont_paises["South America"]].rename(index={"":"famel_21"})
eat_f_21_na=(eat_gen.T).loc["famel_21",cont_paises["North America"]].rename(index={"":"famel_21"})
eat_f_21_eu=(eat_gen.T).loc["famel_21",cont_paises["Europe"]].rename(index={"":"famel_21"})

eat_m_21_africa=(eat_gen.T).loc["male_21",cont_paises["Africa"]].rename(index={"":"male_21"})
eat_m_21_asia=(eat_gen.T).loc["male_21",cont_paises["Asia"]].rename(index={"":"male_21"})
eat_m_21_oceania=(eat_gen.T).loc["male_21",cont_paises["Oceania"]].rename(index={"":"male_21"})
eat_m_21_sa=(eat_gen.T).loc["male_21",cont_paises["South America"]].rename(index={"":"male_21"})
eat_m_21_na=(eat_gen.T).loc["male_21",cont_paises["North America"]].rename(index={"":"male_21"})
eat_m_21_eu=(eat_gen.T).loc["male_21",cont_paises["Europe"]].rename(index={"":"male_21"})

eat_f_09_africa=(eat_gen.T).loc["famel_09",cont_paises["Africa"]].rename(index={"":"famel_09"})
eat_f_09_asia=(eat_gen.T).loc["famel_09",cont_paises["Asia"]].rename(index={"":"famel_09"})
eat_f_09_oceania=(eat_gen.T).loc["famel_09",cont_paises["Oceania"]].rename(index={"":"famel_09"})
eat_f_09_sa=(eat_gen.T).loc["famel_09",cont_paises["South America"]].rename(index={"":"famel_09"})
eat_f_09_na=(eat_gen.T).loc["famel_09",cont_paises["North America"]].rename(index={"":"famel_09"})
eat_f_09_eu=(eat_gen.T).loc["famel_09",cont_paises["Europe"]].rename(index={"":"famel_09"})

eat_m_09_africa=(eat_gen.T).loc["male_09",cont_paises["Africa"]].rename(index={"":"male_09"})
eat_m_09_asia=(eat_gen.T).loc["male_09",cont_paises["Asia"]].rename(index={"":"male_09"})
eat_m_09_oceania=(eat_gen.T).loc["male_09",cont_paises["Oceania"]].rename(index={"":"male_09"})
eat_m_09_sa=(eat_gen.T).loc["male_09",cont_paises["South America"]].rename(index={"":"male_09"})
eat_m_09_na=(eat_gen.T).loc["male_09",cont_paises["North America"]].rename(index={"":"male_09"})
eat_m_09_eu=(eat_gen.T).loc["male_09",cont_paises["Europe"]].rename(index={"":"male_09"})

'''Redes sociales dividas por los paises a los que pertenece cada continete'''
s_m_africa=s_m.loc[:,cont_paises["Africa"]]
s_m_asia=s_m.loc[:,cont_paises["Asia"]]
s_m_oceania=s_m.loc[:,cont_paises["Oceania"]]
s_m_sa=s_m.loc[:,cont_paises["South America"]]
s_m_na=s_m.loc[:,cont_paises["North America"]]
s_m_eu=s_m.loc[:,cont_paises["Europe"]]

dep_af=pd.concat([dep_f_21_africa.T,dep_m_21_africa.T,(s_m_africa.T)["2021"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(dep_af.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2021 AFRICA");
correl=pd.concat([dep_f_09_africa.T,dep_m_09_africa.T,(s_m_africa.T)["2009"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2009 AFRICA");
p_v_dep_09_af=test_corr(0.61,54)
p_v_dep_21_af=test_corr(0.77,54)
print(f"El p_valor de Africa en 2009 es: {p_v_dep_09_af}")
print(f"El p_valor de Africa en 2021 es: {p_v_dep_21_af}")

dep_af=pd.concat([dep_f_21_asia.T,dep_m_21_asia.T,(s_m_asia.T)["2021"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(dep_af.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2021 AFRICA");
correl=pd.concat([dep_f_09_asia.T,dep_m_09_asia.T,(s_m_asia.T)["2009"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2009 ASIA");

p_v_dep_09_as=test_corr(67,46)
p_v_dep_21_as=test_corr(0.87,46)
print(f"El p_valor de Asia en 2009 es: {p_v_dep_09_as}")
print(f"El p_valor de Asia en 2021 es: {p_v_dep_21_as}")

dep_eu=pd.concat([dep_f_21_eu.T,dep_m_21_eu.T,(s_m_eu.T)["2021"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(dep_eu.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2021 EUROPA");
correl=pd.concat([dep_f_09_eu.T,dep_m_09_eu.T,(s_m_eu.T)["2009"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2009 EUROPA");

p_v_dep_09_eu=test_corr(0.93,46)
p_v_dep_21_eu=test_corr(0.98,46)
print(f"El p_valor de Europa en 2009 es: {p_v_dep_09_eu}")
print(f"El p_valor de Europa en 2021 es: {p_v_dep_21_eu}")
dep_oc=pd.concat([dep_f_21_oceania.T,dep_m_21_oceania.T,(s_m_oceania.T)["2021"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(dep_eu.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2021 OCEANIA");
correl=pd.concat([dep_f_09_oceania.T,dep_m_09_oceania.T,(s_m_oceania.T)["2009"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2009 OCEANIA");

p_v_dep_09_oc=test_corr(0.97,15)
p_v_dep_21_oc=test_corr(0.98,15)
print(f"El p_valor de Europa en 2009 es: {p_v_dep_09_oc}")
print(f"El p_valor de Europa en 2021 es: {p_v_dep_21_oc}")

dep_sa=pd.concat([dep_f_21_sa.T,dep_m_21_sa.T,(s_m_sa.T)["2021"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(dep_eu.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2021 S.America");
correl=pd.concat([dep_f_09_sa.T,dep_m_09_sa.T,(s_m_sa.T)["2009"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2009 S.America");

p_v_dep_09_sa=test_corr(0.99,22)
p_v_dep_21_sa=test_corr(0.98,22)
print(f"El p_valor de Europa en 2009 es: {p_v_dep_09_sa}")
print(f"El p_valor de Europa en 2021 es: {p_v_dep_21_sa}")

dep_na=pd.concat([dep_f_21_na.T,dep_m_21_na.T,(s_m_na.T)["2021"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(dep_eu.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 N.America");
correl=pd.concat([dep_f_09_na.T,dep_m_09_na.T,(s_m_na.T)["2009"]],axis=1)
plt.figure(figsize=(4,4))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por generos y Uso de Redes Sociales 2009 N.America");

p_v_dep_09_na=test_corr(0.99,14)
p_v_dep_21_na=test_corr(0.99,14)
print(f"El p_valor de NA en 2009 es: {p_v_dep_09_na}")
print(f"El p_valor de NA en 2021 es: {p_v_dep_21_na}")


q1=pd.concat([eat_gen_icm.loc[:,["famel_09"]].T,eat_gen_icm.loc[:,["male_09"]].T]).T
l1=pd.concat([eat_gen_icm.loc[:,["famel_21"]].T,eat_gen_icm.loc[:,["male_21"]].T]).T
q1["suma09"]=q1["famel_09"]+q1["male_09"]
l1["suma21"]=l1["famel_21"]+l1["male_21"]
q1=q1.drop(columns=["famel_09","male_09"])
l1=l1.drop(columns=["male_21","famel_21"])
eat_sum_icm=pd.concat([l1,q1],axis=1).T

q2=pd.concat([dep_gen_icm.loc[:,["famel_09"]].T,dep_gen_icm.loc[:,["male_09"]].T]).T
l2=pd.concat([dep_gen_icm.loc[:,["famel_21"]].T,dep_gen_icm.loc[:,["male_21"]].T]).T
q2["suma09"]=q2["famel_09"]+q2["male_09"]
l2["suma21"]=l2["famel_21"]+l2["male_21"]
q2=q2.drop(columns=["famel_09","male_09"])
l2=l2.drop(columns=["male_21","famel_21"])
dep_sum_icm=pd.concat([l2,q2],axis=1).T
f, axes = plt.subplots(1,2, figsize=(30,20), sharex=True)
h=(dep_sum_icm.T).loc[:,'suma09'].reset_index()
h1=(dep_sum_icm.T).loc[:,'suma21'].reset_index()
l=(s_m_icm_09.T).reset_index()
z=(s_m_icm_21.T).reset_index()

sns.barplot(l,x='2009',y ="Country/area", color="olive", ax=axes[0])
axes[0].set_title('Redes Sociales 2009-€')

sns.barplot(z, x='2021', y ="Country/area", color="purple", ax=axes[1])
axes[1].set_title('Redes Sociales 2021-€')
axes[1].set_ylabel('') 
axes[1].set_xlabel('') 
axes[0].set_xlabel('') 
axes[1].set_yticklabels([]);
 
# Ajustar el diseño
f, axes = plt.subplots(1,2, figsize=(20,10), sharex=True)
sns.barplot(h,x='suma09',y ="Country/area", color="gold", ax=axes[0])
axes[0].set_title('Depresión 2009-€')

sns.barplot(h1, x='suma21',y ="Country/area", color="blue", ax=axes[1])
axes[1].set_title('Depresión 2021-€')
axes[1].set_ylabel('') 
axes[1].set_xlabel('') 
axes[0].set_xlabel('') 
axes[1].set_yticklabels([]);

plt.tight_layout()
plt.show()
f, axes = plt.subplots(1,2, figsize=(20,10), sharex=True)

k=(eat_sum_icm.T).loc[:,'suma09'].reset_index()
k1=(eat_sum_icm.T).loc[:,'suma21'].reset_index()
sns.barplot(k,x='suma09',y ="Country/area", color="skyblue", ax=axes[0])
axes[0].set_title('Desordenes alimenticios 2009-€')
sns.barplot(k1, x='suma21',y ="Country/area", color="teal", ax=axes[1])
axes[1].set_title('Desordenes alimenticios 2021-€')
axes[1].set_ylabel('') 
axes[1].set_xlabel('') 
axes[0].set_xlabel('') 
axes[1].set_yticklabels([]);

correl=pd.concat([dep_sum_icm.T["suma09"],s_m_icm_09.T],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresion y Uso de Redes Sociales € 2009" );

correl=pd.concat([dep_sum_icm.T["suma21"],s_m_icm_21.T],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresion y Uso de Redes Sociales 2021€");

correl=pd.concat([eat_sum_icm.T["suma09"],s_m_icm_09.T],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.alimenticios y Uso de Redes Sociales € 2009" );

correl=pd.concat([eat_sum_icm.T["suma21"],s_m_icm_21.T],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=0,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.alimenticios y Uso de Redes Sociales 2021€");

p_eat_09_icm=test_corr(0.13,4)#en este caso es 4 que son la clasificación según la economía
p_eat_21_icm=test_corr(0.66,4)
p_dep_09_icm=test_corr(0.57,4)
p_dep_21_icm=test_corr(0.76,4)

print(f"p_value depresión 2009 M: {round(p_dep_09_icm,2)}")
print(f"p_value depresión 2021 M: {round(p_dep_21_icm,2)}")
print(f"p_value t. alimenticios 2009 M: {round(p_eat_09_icm,2)}")
print(f"p_value t. alimenticios 2021 M: {round(p_eat_21_icm,2)}")
#Datos sin Nan para que no influyan en la media
'''Por paises'''
dep_age_21_pais=dep_age_21.loc[:, :"Zimbabwe"]
dep_age_09_pais=dep_age_09.loc[:, :"Zimbabwe"]
eat_age_21_pais=eat_age_21.loc[:, :"Zimbabwe"]
eat_age_09_pais=eat_age_09.loc[:, :"Zimbabwe"]

'''Limpiamos datos'''
x2=((dep_age_09_pais.T).dropna()).T
y2=((dep_age_21_pais.T).dropna()).T

x3=((eat_age_09_pais.T).dropna()).T
y3=((eat_age_21_pais.T).dropna()).T

'''2009'''
medias_5_14=calcular_medias(x2,"Ages 5-14",cont,pob_09,cont_paises)
dep_5_14_09_media_09 = pd.DataFrame({"Country/area": cont, "Ages 5-14": medias_5_14}).set_index("Country/area")

medias_15_19=calcular_medias(x2,"Ages 15-19",cont,pob_09,cont_paises)
dep_15_19_media_09 = pd.DataFrame({"Country/area": cont, "Ages 15-19": medias_15_19}).set_index("Country/area")

medias_20_24=calcular_medias(x2,"Ages 20-24",cont,pob_09,cont_paises)
dep_20_24_media_09 = pd.DataFrame({"Country/area": cont, "Ages 20-24": medias_20_24}).set_index("Country/area")

medias_25_29=calcular_medias(x2,"Ages 25-29",cont,pob_09,cont_paises)
dep_25_25_media_09 = pd.DataFrame({"Country/area": cont, "Ages 25-29": medias_25_29}).set_index("Country/area")

medias_30_34=calcular_medias(x2,"Ages 30-34",cont,pob_09,cont_paises)
dep_30_34_media_09 = pd.DataFrame({"Country/area": cont, "Ages 30-34": medias_30_34}).set_index("Country/area")

medias_35_39=calcular_medias(x2,"Ages 35-39",cont,pob_09,cont_paises)
dep_35_39_media_09 = pd.DataFrame({"Country/area": cont, "Ages 35-39": medias_35_39}).set_index("Country/area")

medias_40_44=calcular_medias(x2,"Ages 40-44",cont,pob_09,cont_paises)
dep_40_44_media_09 = pd.DataFrame({"Country/area": cont, "Ages 40-44": medias_40_44}).set_index("Country/area")

medias_45_49=calcular_medias(x2,"Ages 45-49",cont,pob_09,cont_paises)
dep_45_49_media_09 = pd.DataFrame({"Country/area": cont, "Ages 45-49": medias_45_49}).set_index("Country/area")

'''2021'''
medias_5_14_1=calcular_medias(y2,"Ages 5-14",cont,pob_21,cont_paises)
dep_5_14_09_media_21 = pd.DataFrame({"Country/area": cont, "Ages 5-14": medias_5_14_1}).set_index("Country/area")

medias_15_19_1=calcular_medias(y2,"Ages 15-19",cont,pob_21,cont_paises)
dep_15_19_media_21 = pd.DataFrame({"Country/area": cont, "Ages 15-19": medias_15_19_1}).set_index("Country/area")

medias_20_24_1=calcular_medias(y2,"Ages 20-24",cont,pob_21,cont_paises)
dep_20_24_media_21 = pd.DataFrame({"Country/area": cont, "Ages 20-24": medias_20_24_1}).set_index("Country/area")

medias_25_29_1=calcular_medias(y2,"Ages 25-29",cont,pob_21,cont_paises)
dep_25_25_media_21 = pd.DataFrame({"Country/area": cont, "Ages 25-29": medias_25_29_1}).set_index("Country/area")

medias_30_34_1=calcular_medias(y2,"Ages 30-34",cont,pob_21,cont_paises)
dep_30_34_media_21 = pd.DataFrame({"Country/area": cont, "Ages 30-34": medias_30_34_1}).set_index("Country/area")

medias_35_39_1=calcular_medias(y2,"Ages 35-39",cont,pob_21,cont_paises)
dep_35_39_media_21 = pd.DataFrame({"Country/area": cont, "Ages 35-39": medias_35_39_1}).set_index("Country/area")

medias_40_44_1=calcular_medias(y2,"Ages 40-44",cont,pob_21,cont_paises)
dep_40_44_media_21 = pd.DataFrame({"Country/area": cont, "Ages 40-44": medias_40_44_1}).set_index("Country/area")

medias_45_49_1=calcular_medias(y2,"Ages 45-49",cont,pob_21,cont_paises)
dep_45_49_media_21 = pd.DataFrame({"Country/area": cont, "Ages 45-49": medias_45_49_1}).set_index("Country/area")

'''Eat'''

'''2009'''
medias_5_14_2=calcular_medias(x3,"Ages 5-14",cont,pob_09,cont_paises)
eat_5_14_09_media_09 = pd.DataFrame({"Country/area": cont, "Ages 5-14": medias_5_14_2}).set_index("Country/area")

medias_15_19_2=calcular_medias(x3,"Ages 15-19",cont,pob_09,cont_paises)
eat_15_19_media_09 = pd.DataFrame({"Country/area": cont, "Ages 15-19": medias_15_19_2}).set_index("Country/area")

medias_20_24_2=calcular_medias(x3,"Ages 20-24",cont,pob_09,cont_paises)
eat_20_24_media_09 = pd.DataFrame({"Country/area": cont, "Ages 20-24": medias_20_24_2}).set_index("Country/area")

medias_25_29_2=calcular_medias(x3,"Ages 25-29",cont,pob_09,cont_paises)
eat_25_25_media_09 = pd.DataFrame({"Country/area": cont, "Ages 25-29": medias_25_29_2}).set_index("Country/area")

medias_30_34_2=calcular_medias(x3,"Ages 30-34",cont,pob_09,cont_paises)
eat_30_34_media_09 = pd.DataFrame({"Country/area": cont, "Ages 30-34": medias_30_34_2}).set_index("Country/area")

medias_35_39_2=calcular_medias(x3,"Ages 35-39",cont,pob_09,cont_paises)
eat_35_39_media_09 = pd.DataFrame({"Country/area": cont, "Ages 35-39": medias_35_39_2}).set_index("Country/area")

medias_40_44_2=calcular_medias(x3,"Ages 40-44",cont,pob_09,cont_paises)
eat_40_44_media_09 = pd.DataFrame({"Country/area": cont, "Ages 40-44": medias_40_44_2}).set_index("Country/area")

medias_45_49_2=calcular_medias(x3,"Ages 45-49",cont,pob_09,cont_paises)
eat_45_49_media_09 = pd.DataFrame({"Country/area": cont, "Ages 30-34": medias_45_49_2}).set_index("Country/area")


'''2021'''
medias_5_14_3=calcular_medias(y3,"Ages 5-14",cont,pob_21,cont_paises)
eat_5_14_09_media_21 = pd.DataFrame({"Country/area": cont, "Ages 5-14": medias_5_14_3}).set_index("Country/area")

medias_15_19_3=calcular_medias(y3,"Ages 15-19",cont,pob_21,cont_paises)
eat_15_19_media_21 = pd.DataFrame({"Country/area": cont, "Ages 15-19": medias_15_19_3}).set_index("Country/area")

medias_20_24_3=calcular_medias(y3,"Ages 20-24",cont,pob_21,cont_paises)
eat_20_24_media_21 = pd.DataFrame({"Country/area": cont, "Ages 20-24": medias_20_24_3}).set_index("Country/area")

medias_25_29_3=calcular_medias(y3,"Ages 25-29",cont,pob_21,cont_paises)
eat_25_25_media_21 = pd.DataFrame({"Country/area": cont, "Ages 25-29": medias_25_29_3}).set_index("Country/area")

medias_30_34_3=calcular_medias(y3,"Ages 30-34",cont,pob_21,cont_paises)
eat_30_34_media_21 = pd.DataFrame({"Country/area": cont, "Ages 30-34": medias_30_34_3}).set_index("Country/area")

medias_35_39_3=calcular_medias(y3,"Ages 35-39",cont,pob_21,cont_paises)
eat_35_39_media_21 = pd.DataFrame({"Country/area": cont, "Ages 35-39": medias_35_39_3}).set_index("Country/area")

medias_40_44_3=calcular_medias(y3,"Ages 40-44",cont,pob_21,cont_paises)
eat_40_44_media_21 = pd.DataFrame({"Country/area": cont, "Ages 40-44": medias_40_44_3}).set_index("Country/area")

medias_45_49_3=calcular_medias(y3,"Ages 45-49",cont,pob_21,cont_paises)
eat_45_49_media_21 = pd.DataFrame({"Country/area": cont, "Ages 30-34": medias_45_49_3}).set_index("Country/area")

'''concatenamos las medias segun los años y el desorden alimenticio para crear los nuevos DataFrame'''
n=pd.concat([eat_5_14_09_media_21,eat_15_19_media_21,eat_20_24_media_21,eat_25_25_media_21,eat_30_34_media_21,eat_35_39_media_21,eat_40_44_media_21,eat_45_49_media_21],axis=1)

m=pd.concat([eat_5_14_09_media_09,eat_15_19_media_09,eat_20_24_media_09,eat_25_25_media_09,eat_30_34_media_09,eat_35_39_media_09,eat_40_44_media_09,eat_45_49_media_09],axis=1)
p=pd.concat([dep_5_14_09_media_21,dep_15_19_media_21,dep_20_24_media_21,dep_25_25_media_21,dep_30_34_media_21,dep_35_39_media_21,dep_40_44_media_21,dep_45_49_media_21],axis=1)

q=pd.concat([dep_5_14_09_media_09,dep_15_19_media_09,dep_20_24_media_09,dep_25_25_media_09,dep_30_34_media_09,dep_35_39_media_09,dep_40_44_media_09,dep_45_49_media_09],axis=1)

m_melted = melt_datos(m)
n_melted = melt_datos(n)
p_melted = melt_datos(p)
q_melted = melt_datos(q)

f, axes = plt.subplots(2,2, figsize=(30,20), sharex=True)
sns.lineplot(m_melted, x='Rango de Edad', y='Num de Personas', hue='Country/area', color="skyblue", ax=axes[0, 0])
axes[0, 0].set_title('Desordenes alimenticios 2009')
sns.lineplot(n_melted, x='Rango de Edad', y='Num de Personas', hue='Country/area', color="olive", ax=axes[0, 1])
axes[0, 1].set_title('Desordenes alimenticios 2021')

sns.lineplot(q_melted, x='Rango de Edad', y='Num de Personas', hue='Country/area', color="teal", ax=axes[1, 0])
axes[1, 0].set_title('Depresión 2009')
sns.lineplot(p_melted, x='Rango de Edad', y='Num de Personas', hue='Country/area', color="gold", ax=axes[1, 1])
axes[1, 1].set_title('Depresión 2021')
# Ajustar el diseño
plt.tight_layout()
plt.show()

'''Hacemos una separación de los datos por los paises de cada continente'''
dep_age_21_africa=dep_age_21.loc[:,cont_paises["Africa"]]
dep_age_21_asia=dep_age_21.loc[:,cont_paises["Asia"]]
dep_age_21_oceania=dep_age_21.loc[:,cont_paises["Oceania"]]
dep_age_21_sa=dep_age_21.loc[:,cont_paises["South America"]]
dep_age_21_na=dep_age_21.loc[:,cont_paises["North America"]]
dep_age_21_eu=dep_age_21.loc[:,cont_paises["Europe"]]

dep_age_09_africa=dep_age_09.loc[:,cont_paises["Africa"]]
dep_age_09_asia=dep_age_09.loc[:,cont_paises["Asia"]]
dep_age_09_oceania=dep_age_09.loc[:,cont_paises["Oceania"]]
dep_age_09_sa=dep_age_09.loc[:,cont_paises["South America"]]
dep_age_09_na=dep_age_09.loc[:,cont_paises["North America"]]
dep_age_09_eu=dep_age_09.loc[:,cont_paises["Europe"]]

eat_age_09_africa=eat_age_09.loc[:,cont_paises["Africa"]]
eat_age_09_asia=eat_age_09.loc[:,cont_paises["Asia"]]
eat_age_09_oceania=eat_age_09.loc[:,cont_paises["Oceania"]]
eat_age_09_sa=eat_age_09.loc[:,cont_paises["South America"]]
eat_age_09_na=eat_age_09.loc[:,cont_paises["North America"]]
eat_age_09_eu=eat_age_09.loc[:,cont_paises["Europe"]]

eat_age_21_africa=eat_age_21.loc[:,cont_paises["Africa"]]
eat_age_21_asia=eat_age_21.loc[:,cont_paises["Asia"]]
eat_age_21_oceania=eat_age_21.loc[:,cont_paises["Oceania"]]
eat_age_21_sa=eat_age_21.loc[:,cont_paises["South America"]]
eat_age_21_na=eat_age_21.loc[:,cont_paises["North America"]]
eat_age_21_eu=eat_age_21.loc[:,cont_paises["Europe"]]

dep_af=pd.concat([dep_age_21_africa.T,(s_m_africa.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(dep_af.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 AFRICA");
correl=pd.concat([dep_age_09_africa.T,(s_m_africa.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 AFRICA");
ex=eat_all.loc["Africa",["2009"]]
ex=eat_all.loc[cont_paises["Africa"],["2009"]]
ex1=(ex*pob_09["Africa"])/100
dep_all_af=pd.concat([ex1,(s_m_africa.T)["2009"].T],axis=1)

plt.figure(figsize=(5,5))
sns.heatmap(dep_all_af.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión para todas All ages y Uso de Redes Sociales 2009 Africa");

e=eat_all.loc["Africa",["2021"]]
e=eat_all.loc[cont_paises["Africa"],["2021"]]
e1=(e*pob_09["Africa"])/100
dep_all_eu=pd.concat([e1,(s_m_africa.T)["2021"].T],axis=1)

plt.figure(figsize=(5,5))
sns.heatmap(dep_all_eu.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión para todas All ages y Uso de Redes Sociales 2021 Africa");

'''Valores de All age'''
p_v_dep_09_af=test_corr(0.25,54)
p_v_dep_21_af=test_corr(0.28,54)
print(f"El p_valor de Africa en 2009 es: {p_v_dep_09_af}")
print(f"El p_valor de Africa en 2021 es: {p_v_dep_21_af}")
'''Valores de todas las edades'''
p_v_dep_09_af=test_corr(-0.16,54)
p_v_dep_21_af=test_corr(0.059,54)
print(f"El p_valor de Africa en 2009 es: {p_v_dep_09_af}")
print(f"El p_valor de Africa en 2021 es: {p_v_dep_21_af}")


correl=pd.concat([dep_age_21_asia.T,(s_m_asia.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 ASIA");

correl1=pd.concat([dep_age_09_asia.T,(s_m_asia.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 ASIA");
ex=eat_all.loc["Asia",["2009"]]
ex=eat_all.loc[cont_paises["Asia"],["2009"]]
ex1=(ex*pob_09["Asia"])/100
dep_all_as=pd.concat([ex1,(s_m_asia.T)["2009"].T],axis=1)

plt.figure(figsize=(5,5))
sns.heatmap(dep_all_as.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión para todas las edades y Uso de Redes Sociales 2009 Asia");

e=eat_all.loc["Asia",["2021"]]
e=eat_all.loc[cont_paises["Asia"],["2021"]]
e1=(e*pob_09["Asia"])/100
dep_all_as=pd.concat([e1,(s_m_asia.T)["2021"].T],axis=1)

plt.figure(figsize=(5,5))
sns.heatmap(dep_all_as.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión para todas las edades y Uso de Redes Sociales 2021 Asia");

correl=pd.concat([dep_age_21_eu.T,(s_m_eu.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 EUROPA");

correl1=pd.concat([dep_age_09_eu.T,(s_m_eu.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 EUROPA");

p_v_dep_09_eu=test_corr(0.17,46)
p_v_dep_21_eu=test_corr(0.0045,46)
print(f"El p_valor de Europa en 2009 es: {p_v_dep_09_eu}")
print(f"El p_valor de Europa en 2021 es: {p_v_dep_21_eu}")

correl=pd.concat([dep_age_21_oceania.T,(s_m_oceania.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 OCEANIA");

correl1=pd.concat([dep_age_09_oceania.T,(s_m_oceania.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 OCEANIA");

p_v_dep_09_oc=test_corr(0.82,15)
p_v_dep_21_oc=test_corr(0.95,15)
print(f"El p_valor de Europa en 2009 es: {p_v_dep_09_oc}")
print(f"El p_valor de Europa en 2021 es: {p_v_dep_21_oc}")

correl=pd.concat([dep_age_21_sa.T,(s_m_sa.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 South America");

correl1=pd.concat([dep_age_09_sa.T,(s_m_sa.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 South America");

p_v_dep_09_sa=test_corr(0.1,22)
p_v_dep_21_sa=test_corr(-0.1,22)
print(f"El p_valor de SA en 2009 es: {p_v_dep_09_sa}")
print(f"El p_valor de SA en 2021 es: {p_v_dep_21_sa}")

correl=pd.concat([dep_age_21_na.T,(s_m_na.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2021 North America");

correl1=pd.concat([dep_age_09_na.T,(s_m_na.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 North America");
p_v_dep_09_na=test_corr(0.53,14)
p_v_dep_21_na=test_corr(0.59,14)
print(f"El p_valor de NA en 2009 es: {p_v_dep_09_na}")
print(f"El p_valor de NA en 2021 es: {p_v_dep_21_na}")
all_pop_eu_09=(eat_all.loc["Europe","2009"]*100)/pob_09["Europe"]
all_pop_af_09=(eat_all.loc["Africa","2009"]*100)/pob_09["Africa"]
correl=pd.concat([dep_age_09_africa.T,(s_m.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre Depresión por edades y Uso de Redes Sociales 2009 AFRICA");
dep_af=pd.concat([eat_age_21_africa.T,(s_m_africa.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(dep_af.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2021 AFRICA");
correl=pd.concat([dep_age_09_africa.T,(s_m_africa.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2009 AFRICA");

p_v_eat_09_af=test_corr(0.36,54)
p_v_eat_21_af=test_corr(0.25,54)
print(f"El p_valor de Africa en 2009 es: {p_v_eat_09_af}")
print(f"El p_valor de Africa en 2021 es: {p_v_eat_21_af}")
correl=pd.concat([eat_age_21_asia.T,(s_m_asia.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2021 ASIA");

correl1=pd.concat([dep_age_09_asia.T,(s_m_asia.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2009 ASIA");
correl=pd.concat([eat_age_21_eu.T,(s_m_eu.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2021 EUROPA");

correl1=pd.concat([dep_age_09_eu.T,(s_m_eu.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2009 EUROPA");

p_v_eat_09_eu=test_corr(0.17,46)
p_v_eat_21_eu=test_corr(0.07,46)
print(f"El p_valor de Eu en 2009 es: {p_v_eat_09_eu}")
print(f"El p_valor de Eu en 2021 es: {p_v_eat_21_eu}")

correl=pd.concat([eat_age_21_oceania.T,(s_m_oceania.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2021 OCEANIA");

correl1=pd.concat([dep_age_09_oceania.T,(s_m_oceania.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2009 OCEANIA");

p_v_eat_09_oc=test_corr(0.82,15)
p_v_eat_21_oc=test_corr(0.91,15)
print(f"El p_valor de Oceania en 2009 es: {p_v_eat_09_oc}")
print(f"El p_valor de Oceania en 2021 es: {p_v_eat_21_oc}")
correl=pd.concat([eat_age_21_sa.T,(s_m_sa.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2021 South America");

correl1=pd.concat([eat_age_09_sa.T,(s_m_sa.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2009 South America");

p_v_eat_09_sa=test_corr(0.14,22)
p_v_eat_21_sa=test_corr(0.12,22)
print(f"El p_valor de S.A en 2009 es: {p_v_eat_09_sa}")
print(f"El p_valor de S.A en 2021 es: {p_v_eat_21_sa}")
correl=pd.concat([eat_age_21_na.T,(s_m_na.T)["2021"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(250,270, s=80, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2021 North America");

correl1=pd.concat([dep_age_09_na.T,(s_m_na.T)["2009"]],axis=1)
plt.figure(figsize=(5,5))
sns.heatmap(correl1.corr(),
            vmin=-1,
            vmax=1,
            cmap=sns.diverging_palette(90, 120, s=100, l=40, n=9),
            square=True,
            linewidths=.9,
            cbar_kws={'shrink': 0.7, 'aspect': 10},
            annot=True);
plt.title("Correlación entre T.Alimenticios por edades y Uso de Redes Sociales 2009 North America");
p_v_eat_09_na=test_corr(0.53,14)#tenemos 14 paises
p_v_eat_21_na=test_corr(0.7,14)
print(f"El p_valor de N.A en 2009 es: {p_v_eat_09_na}")
print(f"El p_valor de N.A en 2021 es: {p_v_eat_21_na}")

'''Calculamos los porcentajes en españa de los datos de redes sociales de cada año'''
x=(s_m.loc["2009","Spain"]/46360000)*100
y=(s_m.loc["2021","Spain"]/47420000)*100
plt.figure(figsize=(6,3))
plt.barh(y=s_m.index, width=[x,y],color=["#9467bd","#9ACD32"]);
plt.legend(title="Uso de Redes sociales en España %");
f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

'''Desordenes alimenticios por género 2009-21'''
axes[1].barh(y=eat_gen_09.index, width=eat_gen_09["Spain"],color=color2,label =["2009 M","2009 F"]);
axes[1].barh(y=eat_gen_21.index, width=eat_gen_21["Spain"],color=color,label =["2021 M","2021 F"]);
axes[1].set_title("Des. Alimenticios por año y género en España");
axes[1].legend();

'''Desordenes alimenticios por edad 2009-21'''
axes[0].barh(y=eat_age_21.index, width=eat_age_21["Spain"],color="#FF8C00",label ="2021");
axes[0].barh(y=eat_age_09.index, width=eat_age_09["Spain"],color="#008080",label ="2009");
axes[0].set_title("Des. Alimenticios por año y edades en España")
axes[0].legend();
f, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

'''Depresión por género 2009-21'''
axes[0].barh(y=dep_gen_21.index, width=dep_gen_21["Spain"],color=['#0000CD','#FF00FF'],label=["2021 M","2021 F"]);
axes[0].barh(y=dep_gen_09.index, width=dep_gen_09["Spain"],color=['#87CEEB', "#FFC0CB"],label =["2009 M","2009 F"]);
axes[0].set_title("Depresión por año y género en España");
axes[0].legend();
'''Depresión por edad 2009-21'''
axes[1].barh(y=dep_age_21.index, width=dep_age_21["Spain"],color="#9ACD32",label ="2021");
axes[1].barh(y=dep_age_09.index, width=dep_age_09["Spain"],color="#9467bd",label ="2009");
axes[1].set_title("Depresión por año y edades en España");
axes[1].legend();
'''Para ver la diferencia entre un año  y otro de forma más clara vamos a representarlo en nuevos DataFrame'''
dif_gen_Sp=pd.concat([dep_gen_09["Spain"],dep_gen_21["Spain"]],axis=1)
dif_gen_Sp["diferencia"]= dif_gen_Sp.iloc[:,0]-dif_gen_Sp.iloc[:,1]

dif_age_Sp=pd.concat([dep_age_09["Spain"],dep_age_21["Spain"]],axis=1)
dif_age_Sp["diferencia"]= dif_age_Sp.iloc[:,0]-dif_age_Sp.iloc[:,1]
display("dif_gen_Sp","dif_age_Sp")
dif_gen_Sp_eat=pd.concat([eat_gen_09["Spain"],eat_gen_21["Spain"]],axis=1)
dif_gen_Sp_eat["diferencia"]= dif_gen_Sp_eat.iloc[:,0]-dif_gen_Sp_eat.iloc[:,1]

dif_age_Sp_eat=pd.concat([eat_age_09["Spain"],eat_age_21["Spain"]],axis=1)
dif_age_Sp_eat["diferencia"]= dif_age_Sp_eat.iloc[:,0]-dif_age_Sp_eat.iloc[:,1]


display("dif_gen_Sp_eat","dif_age_Sp_eat")


#tenemos un dato mal escrito que hay que corregir
test["Gender"]=test["Gender"].replace({"Marie":"Male"})
f, ax = plt.subplots(figsize=(13, 10))
sns.heatmap(test[['Daily_Usage_Time (minutes)', 'Posts_Per_Day',
       'Likes_Received_Per_Day', 'Comments_Received_Per_Day',
       'Messages_Sent_Per_Day']].corr(),
            annot=True,
            linewidths=.5,
            ax=ax,
            vmin=0.8,
            vmax=1);

sns.pairplot(test,
             kind="scatter",
             hue="Dominant_Emotion",
             plot_kws=dict(s=80, edgecolor="white",
                           linewidth=2.5));
sns.scatterplot(test,
             x="Daily_Usage_Time (minutes)",
             y="Age",
             hue="Dominant_Emotion");
sns.scatterplot(test,
             x='Likes_Received_Per_Day',
             y="Age",
             hue="Dominant_Emotion");