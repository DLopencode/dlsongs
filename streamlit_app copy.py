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

simil = 0
cancion_cerca = {}

if title:
    for a in album:
        simil_actual = fuzz.ratio(title, a["titulo"]) 

        if simil_actual > simil:
            simil = simil_actual
            cancion_cerca = a
        st.write(cancion_cerca)
       
################################################################################

        # if a['titulo'] == title:
        #     st.write(f'la tenemos!')
        #     st.write(f"coincicencias con nuestra biblioteca: %'{simil}'")
        #     st.write(a)
        # else:
        #     st.write(f"coincicencias con nuestra biblioteca: %'{simil}'")

##################################################################################



