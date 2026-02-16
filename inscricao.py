import streamlit as st

st.set_page_config(page_title="Inscrição Acampamento", page_icon="⛺")

st.title("⛺ Inscrição para o Acampamento")
st.write("Preencha os dados abaixo para confirmar sua participação.")

# --- CONFIGURAÇÃO ---
# Coloque o seu e-mail real aqui embaixo
email_destino = "SEU_EMAIL_AQUI@gmail.com" 

with st.form("meu_formulario"):
    nome = st.text_input("Nome Completo")
    whatsapp = st.text_input("WhatsApp com DDD")
    email_usuario = st.text_input("Seu E-mail")
    origem = st.selectbox("Como soube do evento?", ["Amigo", "Instagram", "Igreja", "Outro"])
    
    submit = st.form_submit_button("Enviar Inscrição")

if submit:
    if nome and whatsapp and email_usuario:
        # Mensagem de sucesso visual
        st.balloons()
        st.success(f"Quase lá, {nome}! Clique no botão abaixo para finalizar o envio dos dados.")
        
        # Este bloco cria um formulário invisível que manda os dados para o seu e-mail via FormSubmit
        html_form = f"""
            <form action="https://formsubmit.co/{email_destino}" method="POST">
                <input type="hidden" name="Nome" value="{nome}">
                <input type="hidden" name="WhatsApp" value="{whatsapp}">
                <input type="hidden" name="Email_Contato" value="{email_usuario}">
                <input type="hidden" name="Origem" value="{origem}">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_subject" value="Nova Inscrição: {nome}">
                <button type="submit" style="
                    background-color: #ff4b4b;
                    color: white;
                    padding: 12px 24px;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 18px;
                    width: 100%;
                    font-weight: bold;
                ">
                    CLIQUE AQUI PARA CONFIRMAR INSCRIÇÃO
                </button>
            </form>
        """
        st.markdown(html_form, unsafe_allow_html=True)
    else:
        st.warning("Por favor, preencha todos os campos.")
