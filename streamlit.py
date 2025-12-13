import streamlit as st
import requests

RASA = 'http://localhost:5005/webhooks/rest/webhook'

st.set_page_config(page_title="Meu Robô de Música 🎶", page_icon="🪕")
st.title("Robô de música 🎶")
st.write("Olá, sou seu robô de música, como posso te ajudar ?")
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
for msg in st.session_state.messages:
    if msg['regra'] == "usuario":
        st.chat_message("usuario").markdown(msg['conteudo'])
    else:
        st.chat_message("assistant").markdown(msg['conteudo'])

digitado = st.chat_input("Digite o que precisa...")

def enviar_msg_rasa(mensagem, remetente='user'):
    resposta = requests.post(RASA, json={'sender': remetente, 'message': mensagem})
    return resposta.json()

if digitado:
    st.session_state.messages.append({"regra": "usuario", "conteudo":digitado})
    with st.spinner("Pensando...🤖"):
        respostaDoBot = enviar_msg_rasa(digitado)
        st.chat_message("usuario").text(digitado)
        for message in respostaDoBot:
            if 'text' in message:
                st.session_state.messages.append({"regra": "assistant", "conteudo":message['text']})
                st.chat_message("assistant").text(message['text'])