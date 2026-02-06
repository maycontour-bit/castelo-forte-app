import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import replicate
import os

# --- CONFIGURAÇÃO DA PÁGINA (DESIGN PREMIUM) ---
st.set_page_config(
    page_title="Castelo Forte",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CONFIGURAÇÃO DE SEGURANÇA (API KEY) ---
# Tenta pegar dos secrets ou pede na sidebar (para evitar hardcode no GitHub)
replicate_api = st.secrets.get("REPLICATE_API_TOKEN")
if not replicate_api:
    # Verifica variável de ambiente (caso local)
    replicate_api = os.environ.get("REPLICATE_API_TOKEN")

if not replicate_api:
    # Se não tiver, pede na sidebar
    with st.sidebar:
        st.markdown("---")
        replicate_api = st.text_input("🔑 API Replicate (Temp)", type="password", help="Cole sua chave aqui para ativar a IA.")
        if replicate_api:
            os.environ["REPLICATE_API_TOKEN"] = replicate_api
            st.success("IA Ativada!")


# --- CSS PERSONALIZADO (AZUL MARINHO & DOURADO) ---
st.markdown("""
    <style>
    /* Fundo Geral */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001529;
        border-right: 1px solid #1e293b;
    }
    
    /* Títulos e Destaques */
    h1, h2, h3 {
        color: #D4AF37 !important; /* Dourado */
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Métricas (Cards) */
    div[data-testid="stMetricValue"] {
        color: #D4AF37;
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        color: #a0a0a0;
    }
    
    /* Botões */
    .stButton>button {
        background-color: #D4AF37;
        color: #001529;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #bfa130;
        color: #000;
    }
    
    /* Tabelas */
    .stDataFrame {
        border: 1px solid #333;
        border-radius: 5px;
    }
    
    /* Inputs */
    .stTextInput>div>div>input {
        background-color: #1e293b;
        color: #fff;
        border: 1px solid #333;
    }
    .stNumberInput>div>div>input {
        background-color: #1e293b;
        color: #fff;
    }
    .stSelectbox>div>div>div {
        background-color: #1e293b;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (NAVEGAÇÃO) ---
with st.sidebar:
    # Logo do Castelo Forte
    st.image("logo.jpg", width=150)
    # st.markdown("<h2 style='text-align: center; color: #D4AF37;'>CASTELO FORTE</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "Navegação", 
        ["🏰 Visão Geral", "💳 Lançamentos", "🔮 Oráculo VFP", "💎 Planos & Assinatura"],
        index=0
    )
    
    st.markdown("---")
    st.caption("🔒 Conexão Segura (256-bit)")
    st.caption("© 2026 Castelo Forte")

# --- MÓDULO 1: VISÃO GERAL (DASHBOARD MOBILLS-STYLE) ---
if menu == "🏰 Visão Geral":
    st.title("Painel de Controle")
    st.markdown("Bem-vindo ao seu QG Financeiro, **Maycon**.")
    
    # 1. Cards Superiores (Resumo)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Saldo Atual", "R$ 12.450,00", "+5.2%")
    with col2:
        st.metric("Receitas (Mês)", "R$ 18.200,00", "+12%")
    with col3:
        st.metric("Despesas (Mês)", "R$ 5.750,00", "-2%")
    with col4:
        st.metric("Meta Castelo", "12%", "R$ 100k Alvo")

    st.markdown("---")

    # 2. Gráficos Principais (Layout Mobills)
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Fluxo de Caixa (6 Meses)")
        # Dados Fictícios
        df_fluxo = pd.DataFrame({
            "Mês": ["Ago", "Set", "Out", "Nov", "Dez", "Jan"],
            "Receitas": [15000, 16000, 15500, 18000, 22000, 18200],
            "Despesas": [12000, 11500, 13000, 14000, 10000, 5750]
        })
        
        fig_bar = go.Figure(data=[
            go.Bar(name='Receitas', x=df_fluxo['Mês'], y=df_fluxo['Receitas'], marker_color='#2ecc71'),
            go.Bar(name='Despesas', x=df_fluxo['Mês'], y=df_fluxo['Despesas'], marker_color='#e74c3c')
        ])
        fig_bar.update_layout(barmode='group', bg_color='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#fff')
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with c2:
        st.subheader("Gastos por Categoria")
        # Dados Fictícios
        df_pizza = pd.DataFrame({
            "Categoria": ["Moradia", "Alimentação", "Transporte", "Lazer", "Investimentos"],
            "Valor": [2500, 1200, 800, 600, 650]
        })
        
        fig_pie = px.pie(df_pizza, values='Valor', names='Categoria', color_discrete_sequence=px.colors.sequential.RdBu)
        fig_pie.update_layout(bg_color='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#fff')
        st.plotly_chart(fig_pie, use_container_width=True)

    # 3. Conexão Bancária (Pluggy)
    st.info("🔗 **Open Finance:** Conecte suas contas do Nubank e Itaú para sincronização automática.")
    if st.button("Conectar Nova Conta (+)", type="primary"):
        st.toast("Aguardando chave da Pluggy (Segunda-feira)...", icon="⏳")

# --- MÓDULO 2: LANÇAMENTOS (EXTRATO) ---
elif menu == "💳 Lançamentos":
    st.title("Extrato Inteligente")
    
    c_filter1, c_filter2 = st.columns(2)
    with c_filter1:
        st.date_input("Período", datetime.today())
    with c_filter2:
        st.selectbox("Conta", ["Todas", "Nubank", "Itaú", "Dinheiro"])
    
    # Tabela de Lançamentos
    data_lanc = {
        "Data": ["06/02", "05/02", "05/02", "04/02"],
        "Descrição": ["Supermercado", "Uber", "Salário", "Netflix"],
        "Categoria": ["Alimentação", "Transporte", "Receita", "Lazer"],
        "Valor": [-450.00, -24.90, 18200.00, -55.90],
        "Status": ["✅ Pago", "✅ Pago", "✅ Recebido", "✅ Pago"]
    }
    df_lanc = pd.DataFrame(data_lanc)
    
    # Estilizando a tabela
    def color_val(val):
        color = '#e74c3c' if val < 0 else '#2ecc71'
        return f'color: {color}; font-weight: bold;'
    
    st.dataframe(
        df_lanc.style.applymap(color_val, subset=['Valor']),
        use_container_width=True,
        height=300
    )
    
    with st.expander("➕ Novo Lançamento Manual"):
        with st.form("new_transaction"):
            c1, c2 = st.columns(2)
            c1.text_input("Descrição")
            c2.number_input("Valor", step=0.01)
            c1.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Outros"])
            c2.date_input("Data")
            st.form_submit_button("Salvar Transação")

# --- MÓDULO 3: ORÁCULO VFP (GUARDIÃO COM IA) ---
elif menu == "🔮 Oráculo VFP":
    st.title("Oráculo VFP 2.0 (IA)")
    st.markdown("O **Guardião do Castelo** usa Inteligência Artificial para analisar suas decisões.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Simulador de Compra")
        descricao = st.text_input("O que você quer comprar?", placeholder="Ex: iPhone 16 Pro Max")
        val_compra = st.number_input("Valor da Compra (R$)", 0.0, step=100.0)
        categoria = st.selectbox("Categoria", ["Essencial", "Estilo de Vida", "Supérfluo/Desejo"])
        parcelas = st.slider("Parcelas", 1, 12, 1)
        
        renda_mensal = 18200.00 # Puxar do banco de dados futuramente
        
        if st.button("Consultar Guardião", type="primary"):
            with st.spinner("O Guardião está consultando a sabedoria milenar..."):
                try:
                    # Lógica Híbrida: Cálculo + IA
                    impacto = (val_compra / renda_mensal) * 100
                    
                    # Prompt para o Modelo Llama 3
                    prompt = f"""
                    Você é o 'Guardião VFP' (Verdade, Fidelidade, Propósito), um consultor financeiro sábio, cristão e estrategista.
                    O usuário quer comprar: {descricao}
                    Valor: R$ {val_compra:.2f}
                    Renda Mensal do Usuário: R$ {renda_mensal:.2f}
                    Impacto na Renda: {impacto:.1f}%
                    Categoria: {categoria}
                    Parcelas: {parcelas}x
                    
                    Diretrizes:
                    1. Se o impacto for > 30%, seja firme e desencoraje.
                    2. Use a regra dos 72h para desejos supérfluos.
                    3. Cite um princípio bíblico curto se apropriado (Ex: Provérbios, Eclesiastes) sobre sabedoria/gastos.
                    4. Seja direto (máximo 3 frases). Dê um veredito: APROVADO, CUIDADO ou REPROVADO.
                    5. Fale como um mentor experiente.
                    """
                    
                    output = replicate.run(
                        "meta/llama-3-8b-instruct",
                        input={"prompt": prompt, "max_tokens": 150}
                    )
                    
                    resultado_ia = "".join(output)
                    
                    st.markdown("### 📜 Veredito do Guardião")
                    st.write(resultado_ia)
                    
                    st.markdown("---")
                    st.caption(f"Impacto Financeiro Real: {impacto:.1f}% da sua renda.")
                    
                    if impacto > 30:
                        st.progress(impacto/100, text="⚠️ Risco Crítico de Orçamento")
                    else:
                        st.progress(impacto/100, text="✅ Margem Segura")
                        
                except Exception as e:
                    st.error(f"O Guardião está em silêncio (Erro na conexão): {e}")
                    st.info("Verifique a chave da API Replicate.")

    with col2:
        st.subheader("Princípios do Manual")
        st.markdown("""
        > **VIPE:**
        > - **V**erdade: Encare seus números.
        > - **I**ntencionalidade: Todo gasto deve ter um propósito.
        > - **P**rincípios: Honre seus compromissos.
        > - **E**ternidade: Construa legado, não apenas patrimônio.
        """)
        
        st.warning("🛡️ **Lembrete:** Dívida não é pecado, mas é escravidão. Evite parcelamentos longos para bens de consumo.")

# --- MÓDULO 4: PLANOS & ASSINATURA ---
elif menu == "💎 Planos & Assinatura":
    st.title("Evolua seu Castelo")
    
    c1, c2, c3 = st.columns(3)
    
    # Plano 1 (Atual)
    with c1:
        st.markdown("""
        <div style='background-color: #1e293b; padding: 20px; border-radius: 10px; border: 2px solid #D4AF37;'>
            <h3 style='color: #D4AF37; text-align: center;'>👑 App MVP</h3>
            <h1 style='text-align: center; color: #fff;'>R$ 79,90</h1>
            <p style='text-align: center; color: #aaa;'>mensal</p>
            <hr>
            <ul style='list-style: none; padding: 0;'>
                <li>✅ Conexão Bancária (Pluggy)</li>
                <li>✅ Dashboard Premium</li>
                <li>✅ Oráculo VFP (Com IA)</li>
            </ul>
            <button style='width: 100%; background-color: #444; color: #fff; border: none; padding: 10px; border-radius: 5px; cursor: not-allowed;'>Plano Atual</button>
        </div>
        """, unsafe_allow_html=True)

    # Plano 2 (Standard)
    with c2:
        st.markdown("""
        <div style='background-color: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #333;'>
            <h3 style='color: #fff; text-align: center;'>⚔️ Standard</h3>
            <h1 style='text-align: center; color: #fff;'>R$ 497,00</h1>
            <p style='text-align: center; color: #aaa;'>mensal</p>
            <hr>
            <ul style='list-style: none; padding: 0;'>
                <li>✅ <b>Tudo do App</b></li>
                <li>✨ Reunião Mensal c/ Consultor</li>
                <li>✨ Análise de Investimentos</li>
            </ul>
            <button style='width: 100%; background-color: #D4AF37; color: #000; border: none; padding: 10px; border-radius: 5px; font-weight: bold;'>Fazer Upgrade</button>
        </div>
        """, unsafe_allow_html=True)
        
    # Plano 3 (Legado)
    with c3:
        st.markdown("""
        <div style='background-color: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #333; opacity: 0.7;'>
            <h3 style='color: #fff; text-align: center;'>🏰 Legado</h3>
            <h1 style='text-align: center; color: #fff;'>Consultar</h1>
            <p style='text-align: center; color: #aaa;'>anual</p>
            <hr>
            <ul style='list-style: none; padding: 0;'>
                <li>✅ Planejamento Sucessório</li>
                <li>✅ Blindagem Patrimonial</li>
                <li>✅ Gestão Familiar Completa</li>
            </ul>
            <button style='width: 100%; background-color: #333; color: #fff; border: none; padding: 10px; border-radius: 5px;'>Falar com Time</button>
        </div>
        """, unsafe_allow_html=True)
