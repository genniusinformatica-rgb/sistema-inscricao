import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Inscrição de Evento", page_icon="📝")

st.title("📝 Formulário de Inscrição")
st.write("Preencha seus dados para confirmar sua participação.")

# Cria a conexão com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Cria o formulário visual
with st.form(key="formulario"):
    nome = st.text_input("Nome Completo")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    opcao = st.selectbox("Como soube do evento?", ["Redes Sociais", "Amigos", "E-mail", "Outros"])
    
    submit_button = st.form_submit_button(label="Enviar Inscrição")

if submit_button:
    if nome == "" or email == "":
        st.warning("Por favor, preencha o Nome e o E-mail.")
    else:
        # Prepara os dados
        dados = {"Nome": nome, "Email": email, "Telefone": telefone, "Origem": opcao}
        
        # Envia para a planilha
        conn.create(data=dados)
        
        st.success(f"Tudo pronto, {nome}! Sua inscrição foi salva na nossa planilha.")
        st.balloons()
