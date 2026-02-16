import streamlit as st

st.set_page_config(page_title="Inscrição 9º Acampamento Monte Tabor", page_icon="⛪")

# Substitua pelo seu e-mail real
email_destino = "genniusinformatica@gmail.com" 

st.title("⛪ ACAMPAMENTO MONTE TABOR")
st.subheader("FICHA DE INSCRIÇÃO")

with st.form("ficha_acampamento"):
    st.info("DADOS PESSOAIS")
    nome = st.text_input("NOME (completo, sem abreviar)")
    apelido = st.text_input("APELIDO")
    
    col1, col2 = st.columns(2)
    with col1:
        idade = st.number_input("IDADE", min_value=0, step=1)
        nasc = st.text_input("DATA NASC. (DD/MM/AAAA)")
    with col2:
        rg = st.text_input("RG")
        cpf = st.text_input("CPF")
        
    tel_pessoal = st.text_input("TELEFONE PESSOAL")
    endereco = st.text_input("ENDEREÇO (completo)")
    
    col3, col4, col5 = st.columns(3)
    with col3:
        bairro = st.text_input("BAIRRO")
    with col4:
        cidade = st.text_input("CIDADE/ESTADO")
    with col5:
        cep = st.text_input("CEP")
        
    ponto_ref = st.text_input("PONTO DE REFERÊNCIA")
    
    st.divider()
    st.info("INFORMAÇÕES ADICIONAIS")
    batismo = st.text_input("DATA BATISMO (Se houver)")
    sus = st.text_input("CARTÃO DO SUS")
    camiseta = st.selectbox("TAMANHO DA CAMISETA", ["14", "16", "PP", "P", "M", "G", "GG"])
    mora_com = st.text_input("COM QUEM VOCÊ MORA?")
    
    st.divider()
    st.info("CONTATOS DE EMERGÊNCIA")
    tels_familia = st.text_area("TELEFONES DE PESSOAS DE SUA FAMÍLIA")
    tels_amigos = st.text_area("TELEFONES DE DIVERSOS AMIGOS PRÓXIMOS")
    convite = st.text_input("QUEM TE CONVIDOU PARA O ACAMPAMENTO?")
    
    st.divider()
    st.info("SAÚDE E INTERESSES")
    medicamento = st.radio("FAZ USO DE MEDICAMENTO CONTÍNUO?", ["NÃO", "SIM"])
    quais_meds = st.text_input("SE SIM, QUAIS?")
    instrumento = st.text_input("TEM HABILIDADE COM ALGUM INSTRUMENTO MUSICAL? QUAL?")
    parentes = st.text_area("PARENTE(S) OU AMIGO(S) PRÓXIMO(S) QUE IRÃO TRABALHAR OU PARTICIPAR")
    
    st.divider()
    st.info("REFLEXÃO")
    vida_hoje = st.text_area("COMO ESTÁ SUA VIDA HOJE?")
    espera_acamp = st.text_area("O QUE VOCÊ ESPERA DO ACAMPAMENTO?")
    
    st.warning("É OBRIGATÓRIO O PREENCHIMENTO DE TODAS AS INFORMAÇÕES")
    submit = st.form_submit_button("GERAR PROTOCOLO DE ENVIO")

if submit:
    if nome and tel_pessoal:
        # ANIMAÇÃO RELIGIOSA (EFEITO DE NEVE/PAZ)
        st.snow()
        st.success(f"Obrigado, {nome}! Sua ficha está pronta. Clique no botão vermelho abaixo para nos enviar os dados.")
        
        # Montando o corpo do e-mail com todos os dados
        corpo_dados = f"""
        NOME: {nome}
        APELIDO: {apelido}
        IDADE: {idade} | NASC: {nasc}
        RG: {rg} | CPF: {cpf}
        TELEFONE: {tel_pessoal}
        ENDEREÇO: {endereco}, {bairro}, {cidade} - CEP: {cep}
        REF: {ponto_ref}
        BATISMO: {batismo} | SUS: {sus}
        CAMISETA: {camiseta}
        MORA COM: {mora_com}
        CONTATOS FAMÍLIA: {tels_familia}
        CONTATOS AMIGOS: {tels_amigos}
        QUEM CONVIDOU: {convite}
        MEDICAMENTO: {medicamento} ({quais_meds})
        INSTRUMENTO: {instrumento}
        PARENTE/AMIGO NO EVENTO: {parentes}
        VIDA HOJE: {vida_hoje}
        O QUE ESPERA: {espera_acamp}
        """

        html_form = f"""
            <form action="https://formsubmit.co/{email_destino}" method="POST">
                <input type="hidden" name="Ficha_Inscricao" value="{corpo_dados}">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_subject" value="NOVA INSCRIÇÃO: {nome} (Monte Tabor)">
                <button type="submit" style="
                    background-color: #ff4b4b;
                    color: white;
                    padding: 15px 30px;
                    border: none;
                    border-radius: 10px;
                    cursor: pointer;
                    font-size: 20px;
                    width: 100%;
                    font-weight: bold;
                ">
                    CLIQUE AQUI PARA CONFIRMAR E ENVIAR AGORA
                </button>
            </form>
        """
        st.markdown(html_form, unsafe_allow_html=True)
    else:
        st.error("Por favor, preencha ao menos o Nome e o Telefone Pessoal.")
