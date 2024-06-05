import streamlit as st
import os

# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

if 't_txt' not in st.session_state:
    st.session_state.t_txt = " "

if 'txt_tr' not in st.session_state:
    st.session_state.txt_tr = " "


st.title("Transcriptor de Audio")

ke = st.text_input('Ingresa tu Clave')
os.environ['OPENAI_API_KEY'] = ke
# Replace with your API key
aai.settings.api_key = ke
# Cargar archivo de audio
uploaded_file = st.file_uploader("Cargar archivo de audio", type=["mp3", "wav"])
if uploaded_file:
        st.audio(uploaded_file, format="audio/mp3")

if uploaded_file is not None:
    config = aai.TranscriptionConfig(auto_highlights=True)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
     uploaded_file,
     config=config
    )

for result in transcript.auto_highlights.results:
  print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")





