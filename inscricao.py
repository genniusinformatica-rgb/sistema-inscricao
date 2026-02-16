import streamlit as st

st.set_page_config(page_title="Inscrição 9º Acampamento Monte Tabor", page_icon="⛺")

# --- CONFIGURAÇÃO ---
email_destino = "genniusinformatica@gmail.com" 

st.title("⛺ 9º ACAMPAMENTO MONTE TABOR")
st.subheader("FICHA DE INSCRIÇÃO")

# Função para validar CPF simples
def validar_cpf(cpf):
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    return len(cpf_limpo) == 11

with st.form("ficha_acampamento", clear_on_submit=False):
    st.info("DADOS PESSOAIS (Obrigatórios)")
    nome = st.text_input("NOME (completo, sem abreviar) *")
    apelido = st.text_input("APELIDO")
    
    col1, col2 = st.columns(2)
    with col1:
        idade = st.number_input("IDADE *", min_value=0, max_value=120, step=1)
        nasc = st.text_input("DATA NASC. (DD/MM/AAAA) *")
    with col2:
        rg = st.text_input("RG *")
        cpf = st.text_input("CPF (Apenas números) *")
        
    tel_pessoal = st.text_input("TELEFONE PESSOAL (WhatsApp) *")
    endereco = st.text_input("ENDEREÇO (completo) *")
    
    col3, col4, col5 = st.columns(3)
    with col3:
        bairro = st.text_input("BAIRRO *")
    with col4:
        cidade = st.text_input("CIDADE/ESTADO *")
    with col5:
        cep = st.text_input("CEP *")
        
    ponto_ref = st.text_input("PONTO DE REFERÊNCIA *")
    
    st.divider()
    st.info("INFORMAÇÕES ADICIONAIS")
    batismo = st.text_input("DATA BATISMO (Se não souber, escreva 'Não sei') *")
    sus = st.text_input("CARTÃO DO SUS *")
    camiseta = st.selectbox("TAMANHO DA CAMISETA *", ["14", "16", "PP", "P", "M", "G", "GG"])
    mora_com = st.text_input("COM QUEM VOCÊ MORA? *")
    
    st.divider()
    st.info("CONTATOS DE EMERGÊNCIA")
    tels_familia = st.text_area("TELEFONES DE PESSOAS DE SUA FAMÍLIA *")
    tels_amigos = st.text_area("TELEFONES DE DIVERSOS AMIGOS PRÓXIMOS *")
    convite = st.text_input("QUEM TE CONVIDOU PARA O ACAMPAMENTO? *")
    
    st.divider()
    st.info("SAÚDE E REFLEXÃO")
    medicamento = st.radio("FAZ USO DE MEDICAMENTO CONTÍNUO? *", ["NÃO", "SIM"])
    quais_meds = st.text_input("SE SIM, QUAIS?")
    instrumento = st.text_input("TEM HABILIDADE COM ALGUM INSTRUMENTO MUSICAL? QUAL? *")
    parentes = st.text_area("PARENTE(S) OU AMIGO(S) PRÓXIMO(S) QUE IRÃO TRABALHAR OU PARTICIPAR *")
    vida_hoje = st.text_area("COMO ESTÁ SUA VIDA HOJE? *")
    espera_acamp = st.text_area("O QUE VOCÊ ESPERA DO ACAMPAMENTO? *")
    
    submit = st.form_submit_button("VALIDAR DADOS E GERAR PROTOCOLO")

if submit:
    # Lista de campos para conferência de preenchimento
    campos_obrigatorios = [nome, nasc, rg, cpf, tel_pessoal, endereco, bairro, cidade, 
                           cep, ponto_ref, batismo, sus, mora_com, tels_familia, 
                           tels_amigos, convite, instrumento, parentes, vida_hoje, espera_acamp]
    
    if any(campo == "" for campo in campos_obrigatorios):
        st.error("❌ ERRO: Todos os campos com * são obrigatórios!")
    elif not validar_cpf(cpf):
        st.error("❌ CPF INVÁLIDO: Digite um CPF com 11 números.")
    else:
        # VOLTA DOS BALÕES COLORIDOS 🎈
        st.balloons()
        
        st.success(f"✅ Dados validados com sucesso, {nome}! Agora, para finalizar, clique no botão vermelho abaixo.")
        
        corpo_dados = f"""
        NOVA INSCRIÇÃO - MONTE TABOR
        ----------------------------
        NOME: {nome} ({apelido})
        IDADE: {idade} | NASC: {nasc}
        RG: {rg} | CPF: {cpf}
        TEL: {tel_pessoal}
        ENDEREÇO: {endereco}, {bairro}, {cidade} - CEP: {cep}
        REF: {ponto_ref}
        BATISMO: {batismo}
        CARTÃO SUS: {sus}
        TAM. CAMISETA: {camiseta}
        MORA COM: {mora_com}
        CONTATO EMERGÊNCIA FAMÍLIA: {tels_familia}
        CONTATO EMERGÊNCIA AMIGOS: {tels_amigos}
        QUEM TE CONVIDOU: {convite}
        USA MEDICAMENTOS: {medicamento} ({quais_meds})
        INSTRUMENTOS MUSICAIS: {instrumento}
        PARENTES/AMIGOS QUE IRÃO TRABALHAR: {parentes}
        SUA VIDA HOJE: {vida_hoje}
        EXPECTATIVA DO ACAMP.: {espera_acamp}
        """

        html_form = f"""
            <form action="https://formsubmit.co/{email_destino}" method="POST">
                <input type="hidden" name="Ficha_Inscricao" value="{corpo_dados}">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_subject" value="INSCRIÇÃO: {nome} (CPF: {cpf})">
                <button type="submit" style="
                    background-color: #ff4b4b;
                    color: white;
                    padding: 18px;
                    border: none;
                    border-radius: 10px;
                    cursor: pointer;
                    font-size: 20px;
                    width: 100%;
                    font-weight: bold;
                ">
                    CONFIRMAR E ENVIAR AGORA ⛪
                </button>
            </form>
        """
        st.markdown(html_form, unsafe_allow_html=True)
