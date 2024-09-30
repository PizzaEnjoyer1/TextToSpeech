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
st.write('¡Ay! -dijo el ratón-. El mundo se hace cada día más pequeño... Franz Kafka.')

# Mostrar área de texto para ingresar contenido
text = st.text_area("Ingrese el texto a escuchar.")

# Selección de idioma y bandera
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English", "Deutsch", "Français", "Português")
)

# Mapeo de idioma a código de lenguaje y archivo de bandera
flag_image = None
if option_lang == "Español":
    lg = 'es'
    flag_image = 'flags/es.png'  # Ruta de la bandera española
elif option_lang == "English":
    lg = 'en'
    flag_image = 'flags/en.png'  # Ruta de la bandera inglesa
elif option_lang == "Deutsch":
    lg = 'de'
    flag_image = 'flags/de.png'  # Ruta de la bandera alemana
elif option_lang == "Français":
    lg = 'fr'
    flag_image = 'flags/fr.png'  # Ruta de la bandera francesa
elif option_lang == "Português":
    lg = 'pt-BR'
    flag_image = 'flags/pt-BR.png'  # Ruta de la bandera de Brasil

# Mostrar la bandera seleccionada
if flag_image:
    flag = Image.open(flag_image)
    st.image(flag, width=100)  # Ajusta el tamaño de la bandera

# Función para convertir texto a voz
def text_to_speech(text, lg):
    tts = gTTS(text, lang=lg)
    try:
        my_file_name = text[:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text

# Botón para convertir texto a audio
if st.button("Convertir a Audio"):
    result, output_text = text_to_speech(text, lg)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown("## Tu audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    # Descargar archivo de audio
    with open(f"temp/{result}.mp3", "rb") as f:
        data = f.read()

    def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href

    st.markdown(get_binary_file_downloader_html(f"temp/{result}.mp3", "Audio File"), unsafe_allow_html=True)

# Eliminar archivos antiguos
def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_files(7)
