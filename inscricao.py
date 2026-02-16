import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("📝 Inscrição para o Evento")
st.write("Preencha os dados abaixo para garantir sua vaga.")

# Estabelece a conexão com a planilha (configuraremos o link depois)
conn = st.connection("gsheets", type=GSheetsConnection)

# Cria o formulário
with st.form(key="form_inscricao"):
    nome = st.text_input("Nome Completo:")
    email = st.text_input("E-mail:")
    setor = st.selectbox("Setor/Empresa:", ["TI", "RH", "Vendas", "Outros"])
    
    botao_enviar = st.form_submit_button(label="Finalizar Inscrição")

if botao_enviar:
    if nome == "" or email == "":
        st.error("Por favor, preencha o nome e o e-mail!")
    else:
        # Aqui o Python prepara os dados para salvar
        nova_linha = {"Nome": nome, "Email": email, "Setor": setor}
        
        # Comando que envia para o Google Sheets
        conn.create(data=nova_linha)
        
        st.success(f"Parabéns {nome}! Sua inscrição foi realizada.")
        st.balloons()