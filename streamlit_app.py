import streamlit as st
import pandas as pd
from datetime import datetime

# Define os caminhos das imagens para cada nível de feedback
emoticons = {
    "Ótimo": "otimo.png",
    "Bom": "bom.png",
    "Regular": "regular.png",
    "Ruim": "ruim.png",
    "Pessimo": "pessimo.png"
}

# Função para salvar o feedback em um arquivo CSV
def save_feedback(feedback):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    feedback_data = {"timestamp": timestamp, "feedback": feedback}
    df = pd.DataFrame([feedback_data])
    
    try:
        # Se o arquivo já existe, adiciona o novo feedback
        df_existing = pd.read_csv("feedback.csv")
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        # Se o arquivo não existe, cria um novo
        pass
    
    df.to_csv("feedback.csv", index=False)

# Título do app
st.title("Feedback Interativo")

# Texto de instrução
st.write("Por favor, nos dê seu feedback!")

# Layout de colunas para os emoticons e botões
cols = st.columns(len(emoticons))

for i, (feedback, image_path) in enumerate(emoticons.items()):
    with cols[i]:
        st.image(image_path, use_column_width=True)
        if st.button(feedback, key=feedback):
            save_feedback(feedback)
            st.success(f"Obrigado pelo seu feedback: {feedback}")

# Exibe os feedbacks recebidos
if st.checkbox("Ver feedbacks recebidos"):
    try:
        df_feedback = pd.read_csv("feedback.csv")
        st.write(df_feedback)
    except FileNotFoundError:
        st.write("Nenhum feedback recebido ainda.")
