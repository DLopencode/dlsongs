import streamlit as st
from fuzzywuzzy import fuzz

st.title("Buscador de 'CANCIONES'")


title = st.text_input("Titulo de canción")
st.write("Estas buscando...", title)


album = [
    {
    "track_id":1,
    "titulo":"titulo1",
    "duracion":3.5
    },
       {
    "track_id":2,
    "titulo":"hola1",
    "duracion":4.5
    },
       {
    "track_id":3,
    "titulo":"adios1",
    "duracion":5.5
    }
 
]


##################################################################################
# codigo de 'CHE'
# simil = 0
# cancion_cerca = {}

# if title:
#     for a in album:
#         simil_actual = fuzz.ratio(title, a["titulo"]) 

#         if simil_actual > simil:
#             simil = simil_actual
#             cancion_cerca = a
#         st.write(cancion_cerca)
       
################################################################################
if title:
    for a in album:
        simil_actual = fuzz.ratio(title, a["titulo"]) 
        if a['titulo'] == title:
            st.write(f'la tenemos!')
            st.write(f"coincicencias con nuestra biblioteca: %'{simil_actual}'")
            st.write(a)
        else:
            st.write(f"coincicencias con nuestra biblioteca: %'{simil_actual}'")

##################################################################################


option = st.selectbox("SeleccionA opcion",["opciones","cancion mas larga", "cancion mas corta"])


if option == 'cancion mas larga':
    st.write(max([c['duracion']for c in album]))
if option == 'cancion mas corta':
    st.write(min([c['duracion']for c in album]))



##################################################################################

##################################################################################

##################################################################################

##################################################################################

#################################################
# 161224 teoria:
# GRaFICOS!!
numeros = [c['duracion']for c in album]

st.bar_chart(numeros)

######################################

semana = {'lunes': 2, 'martes': 4, 'miercoles': 10, 'jueves': -15, }
st.bar_chart(semana) # algo de label

##########################################

import pandas as pd

def load_datos():
    df = pd.read_csv("titanic.csv") # se suele usar 'df = dataframe'
    return df

df = load_datos()

st.write(df)
st.table(df)











