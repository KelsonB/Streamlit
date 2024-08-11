import streamlit as st
from datetime import date

# Definindo o URL da imagem de fundo
background_image_url = "https://img.freepik.com/vetores-gratis/fundo-gradiente-azul-escuro_78370-2078.jpg"

# Definição das cores baseadas na paleta do site mencionado
PRIMARY_COLOR = "#2b4e72"  # Substitua pela cor primária
SECONDARY_COLOR = "#fa7a32"  # Cor secundária (branco)
ACCENT_COLOR = "#fa7a32"  # Cor de destaque (laranja)

# Estilos customizados
st.markdown("""
            <style>
            header {visibility: hidden;}
            .css-18e3th9 {padding-top: 0;}
            .css-1d391kg {padding: 0;}
            </style>
            """, unsafe_allow_html=True)
st.markdown(
    f"""
    <style>
    /* Estilizando a caixa de seleção */
    .stSelectbox div[data-baseweb="select"] {{
        background-color: {PRIMARY_COLOR};
        color: {ACCENT_COLOR};
        border-radius: 5px;
        border: 2px solid {ACCENT_COLOR};
        padding: 10px;
        font-size: 16px;
    }}
     /* Estilizando o título das caixas de seleção */
    .stSelectbox label {{
        color: {ACCENT_COLOR};
        font-weight: bold;
        font-size: 18px;
        
    }}
    
    /* Cor do texto dentro das opções */
    .stSelectbox div[data-baseweb="select"] > div {{
        color: {PRIMARY_COLOR};
    }}
    
    /* Estilizando o dropdown da caixa de seleção */
    .stSelectbox div[data-baseweb="select"] ul {{
        background-color: {PRIMARY_COLOR};
        color: {PRIMARY_COLOR};
    }}
    .stApp {{
        background-color: {PRIMARY_COLOR};
        background-size: cover;
        background-position: center;
        color: {SECONDARY_COLOR};
        font-family: 'Helvetica', sans-serif;
    }}

    /* Estilo dos títulos */
    h1 {{
        color: {ACCENT_COLOR};
        font-weight: bold;
        font-size:60px;
    }}
    h2 {{
        color: {ACCENT_COLOR};
        font-weight: bold;
        font-size:40px;
    }}

    /* Estilo das caixas de seleção e entrada de texto */
    .stSelectbox, .stTextInput, .stMultiSelect {{
        background-color: rgba(255, 255, 255, 0.8);
        color: {ACCENT_COLOR};
        border-radius: 10px;
        border: none;
        padding: 10px;
        margin-bottom: 20px;
    }}

    /* Estilo dos botões */
    .stButton>button {{
        background-color: {ACCENT_COLOR};
        color: {PRIMARY_COLOR};
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        transition: background-color 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: #e03a00;
    }}

    /* Estilo do resumo */
    .stMarkdown p {{
        color: {PRIMARY_COLOR};
        background-color: rgba(255, 255, 255, 0.7);
        font-weight: bold;
        font-size: 18px;
        border-left: 4px solid {ACCENT_COLOR};
        padding-left: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }}

    /* Responsividade */
    @media (max-width: 768px) {{
        .stApp {{
            padding: 10px;
        }}
        .stButton>button {{
            width: 100%;
            font-size: 16px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Título do site
st.title("Serviços de Contabilidade Lorena Queiroz")

# Lista de serviços
services = {
    "Regularização de CPF": {
        "Declaração IRPF": 200.00,
        "Negociação de débitos": 200.00
    },
    "Regularização de CNPJ": {
        "Fiscal": "A depender do porte",
        "Contábil": "A depender do porte",
        "Fiscal e Contábil": "A depender do porte"
    },
    "Defesa de Malha": {
        "Intimação": 250.00,
        "Notificação": 350.00
    },
    "Abertura de Empresa": {
        "Faturamento Anual até 81.000": "A depender da atividade",
        "Faturamento Anual até 360.000": "A depender da atividade",
        "Faturamento Anual até 4,6 Milhões": "A depender da atividade"
    },
    "Escrituração Contábil": {
        "ME Faturamento Anual até 360.000": "A depender da atividade",
        "EPP Faturamento Anual até 4,6 Milhões": "A depender da atividade"
    },
    "Emissão de Darf": {
        "Quota Imposto de renda PF": 50.00,
        "Guia Simples Nacional": {
            "MEI": 50.00,
            "ME": 100.00,
            "EPP": 150.00
        },
        "Darf de parcelamento": 50.00
    }
}

# Seleção do serviço
selected_service = st.selectbox("Selecione o serviço:", list(services.keys()), placeholder="Selecione")
# Ultimos 5 anos
ano = []
for i in range(0, 5):
    ano.append(date.today().year - i)
# Subserviços
if selected_service:
    subservices = services[selected_service]
    if isinstance(subservices, dict):
        selected_subservice = st.selectbox("Selecione o subserviço:", list(subservices.keys()))
        print(selected_subservice)
        if selected_subservice == "Declaração IRPF":
            ano = st.multiselect("Selecione o ano:", ano, placeholder="Selecione o ano")
    else:
        selected_subservice = selected_service

    # Formulário de informações do cliente
    st.header("Informações do Cliente")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone para contato")
    email = st.text_input("E-mail")

    # Botão para realizar o pagamento
    if st.button("Realizar análise"):
        if selected_subservice == "Declaração IRPF":
            cliente_info = {
                "Nome": nome,
                "Telefone": telefone,
                "Email": email,
                "Serviço": selected_service,
                "Subserviço": selected_subservice,
                "Valor": f'R${int(subservices[selected_subservice]) * len(ano)}',
                "OBS":"Atenção! Esse é o valor base do serviço, sujeito a alteração após análise"
            }
        else:
            # Armazenar valores em uma variável
            cliente_info = {
                "Nome": nome,
                "Telefone": telefone,
                "Email": email,
                "Serviço": selected_service,
                "Subserviço": selected_subservice,
                "Valor": subservices[selected_subservice]
            }

        # Mostrar resumo das informações digitadas
        st.header("Resumo das Informações")
        for key, value in cliente_info.items():
            st.write(f"**{key}:** {value}")

        # Redirecionar para o site de pagamento
        st.write("Redirecionando para pagamento...")
        st.markdown("[Clique aqui para realizar o pagamento](https://www.youtube.com)")