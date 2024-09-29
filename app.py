import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('gato_raton.png')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Escribe y/o selecciona texto para ser escuchado.")

try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")
st.write('¡Ay! -dijo el ratón-. El mundo se hace cada día más pequeño. Al principio era tan grande que le tenía miedo. '  
         ' Corría y corría y por cierto que me alegraba ver esos muros, a diestra y siniestra, en la distancia. ' 
         ' Pero esas paredes se estrechan tan rápido que me encuentro en el último cuarto y ahí en el rincón está '  
         ' la trampa sobre la cual debo pasar. Todo lo que debes hacer es cambiar de rumbo dijo el gato...y se lo comió. ' 
         '  '
         ' Franz Kafka.'
        
        )

st.markdown(f"¿Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese el texto a escuchar.")

# Selección de idioma y mostrar la bandera correspondiente
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English", "Deutsch", "Français", "Português")
)

if option_lang == "Español":
    lg = 'es'
    flag = Image.open('banderas/espanol.png')
elif option_lang == "English":
    lg = 'en'
    flag = Image.open('banderas/ingles.png')
elif option_lang == "Deutsch":
    lg = "de"
    flag = Image.open('banderas/aleman.png')
elif option_lang == "Français":
    lg = "fr"
    flag = Image.open('banderas/frances.png')
elif option_lang == "Português":
    lg = "pt-BR"
    flag = Image.open('banderas/brasil.png')

# Mostrar la bandera seleccionada
st.image(flag, width=100)

def text_to_speech(text, lg):
    tts = gTTS(text, lang=lg)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text
