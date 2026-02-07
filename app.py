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
replicate_api = st.secrets.get("REPLICATE_API_TOKEN")
if not replicate_api:
    replicate_api = os.environ.get("REPLICATE_API_TOKEN")

if not replicate_api:
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
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #1e293b;
        color: #fff;
        border: 1px solid #333;
    }
    .stSelectbox>div>div>div {
        background-color: #1e293b;
        color: #fff;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-color: #D4AF37;
    }
    </style>
""", unsafe_allow_html=True)

# --- MOCK DATA (ESTADO INICIAL) ---
if 'transactions' not in st.session_state:
    st.session_state.transactions = pd.DataFrame({
        "Data": [datetime(2026, 2, 6), datetime(2026, 2, 5), datetime(2026, 2, 5), datetime(2026, 2, 4)],
        "Descrição": ["Supermercado", "Uber", "Salário", "Netflix"],
        "Categoria": ["Alimentação", "Transporte", "Receita", "Lazer"],
        "Valor": [-450.00, -24.90, 18200.00, -55.90],
        "Conta": ["Nubank", "Nubank", "Itaú", "Nubank"],
        "Status": ["Pago", "Pago", "Recebido", "Pago"]
    })

if 'budgets' not in st.session_state:
    st.session_state.budgets = {
        "Alimentação": 1500.00,
        "Transporte": 500.00,
        "Lazer": 400.00,
        "Moradia": 3000.00
    }

# --- SIDEBAR (NAVEGAÇÃO) ---
with st.sidebar:
    st.image("logo.jpg", width=150)
    st.markdown("---")
    
    menu = st.radio(
        "Navegação", 
        ["🏰 Visão Geral", "💳 Lançamentos", "📊 Planejamento (Metas)", "🔮 Oráculo VFP", "💎 Planos"],
        index=0
    )
    
    st.markdown("---")
    st.caption("🔒 Conexão Segura (256-bit)")
    st.caption("© 2026 Castelo Forte")

# --- MÓDULO 1: VISÃO GERAL (DASHBOARD) ---
if menu == "🏰 Visão Geral":
    st.title("Painel de Controle")
    st.markdown("Bem-vindo ao seu QG Financeiro, **Maycon**.")
    
    # 1. Cards Superiores (Resumo)
    # Cálculo real baseado no Mock
    df = st.session_state.transactions
    receitas = df[df['Valor'] > 0]['Valor'].sum()
    despesas = abs(df[df['Valor'] < 0]['Valor'].sum())
    saldo = receitas - despesas
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Saldo Atual", f"R$ {saldo:,.2f}", "+5.2%")
    with col2:
        st.metric("Receitas (Mês)", f"R$ {receitas:,.2f}", "+12%")
    with col3:
        st.metric("Despesas (Mês)", f"R$ {despesas:,.2f}", "-2%")
    with col4:
        st.metric("Meta Castelo", "12%", "R$ 100k Alvo")

    st.markdown("---")

    # 2. Gráficos Principais
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Fluxo de Caixa (Evolução)")
        # Simulação de dados mensais
        df_fluxo = pd.DataFrame({
            "Mês": ["Ago", "Set", "Out", "Nov", "Dez", "Jan", "Fev"],
            "Receitas": [15000, 16000, 15500, 18000, 22000, 18200, receitas],
            "Despesas": [12000, 11500, 13000, 14000, 10000, 5750, despesas],
            "Saldo": [3000, 4500, 2500, 4000, 12000, 12450, saldo]
        })
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=df_fluxo['Mês'], y=df_fluxo['Receitas'], name='Receitas', line=dict(color='#2ecc71', width=3)))
        fig_line.add_trace(go.Scatter(x=df_fluxo['Mês'], y=df_fluxo['Despesas'], name='Despesas', line=dict(color='#e74c3c', width=3)))
        fig_line.add_trace(go.Bar(x=df_fluxo['Mês'], y=df_fluxo['Saldo'], name='Saldo Líquido', marker_color='#D4AF37', opacity=0.3))
        
        fig_line.update_layout(title="Receitas vs Despesas", bg_color='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#fff')
        st.plotly_chart(fig_line, use_container_width=True)
        
    with c2:
        st.subheader("Por Categoria")
        # Agrupamento real do Mock
        df_despesas = df[df['Valor'] < 0].copy()
        df_despesas['Valor'] = df_despesas['Valor'].abs()
        df_pizza = df_despesas.groupby("Categoria")['Valor'].sum().reset_index()
        
        fig_pie = px.pie(df_pizza, values='Valor', names='Categoria', color_discrete_sequence=px.colors.sequential.RdBu, hole=0.4)
        fig_pie.update_layout(bg_color='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#fff')
        st.plotly_chart(fig_pie, use_container_width=True)

# --- MÓDULO 2: LANÇAMENTOS (EXTRATO) ---
elif menu == "💳 Lançamentos":
    st.title("Extrato Inteligente")
    
    # Filtros
    c_filter1, c_filter2, c_filter3 = st.columns(3)
    with c_filter1:
        st.date_input("Período", datetime.today())
    with c_filter2:
        conta_sel = st.selectbox("Conta", ["Todas", "Nubank", "Itaú"])
    with c_filter3:
        cat_sel = st.selectbox("Categoria", ["Todas"] + list(st.session_state.budgets.keys()))
    
    # Tabela
    df_show = st.session_state.transactions
    
    # Estilizando
    def color_val(val):
        color = '#e74c3c' if val < 0 else '#2ecc71'
        return f'color: {color}; font-weight: bold;'
    
    st.dataframe(
        df_show.style.applymap(color_val, subset=['Valor']),
        use_container_width=True,
        height=400,
        column_config={
            "Data": st.column_config.DatetimeColumn(format="DD/MM/YYYY"),
            "Valor": st.column_config.NumberColumn(format="R$ %.2f")
        }
    )
    
    # Botão Flutuante (Simulado)
    with st.expander("➕ Novo Lançamento Manual", expanded=False):
        with st.form("new_transaction"):
            c1, c2 = st.columns(2)
            desc = c1.text_input("Descrição")
            val = c2.number_input("Valor", step=0.01)
            cat = c1.selectbox("Categoria", list(st.session_state.budgets.keys()) + ["Receita"])
            data = c2.date_input("Data")
            tipo = st.radio("Tipo", ["Despesa", "Receita"], horizontal=True)
            
            if st.form_submit_button("Salvar Transação"):
                valor_final = val if tipo == "Receita" else -val
                new_row = pd.DataFrame({
                    "Data": [pd.to_datetime(data)],
                    "Descrição": [desc],
                    "Categoria": [cat],
                    "Valor": [valor_final],
                    "Conta": ["Manual"],
                    "Status": ["Pago"]
                })
                st.session_state.transactions = pd.concat([new_row, st.session_state.transactions], ignore_index=True)
                st.toast("Transação salva com sucesso!", icon="✅")
                st.rerun()

# --- MÓDULO 3: PLANEJAMENTO (METAS) ---
elif menu == "📊 Planejamento (Metas)":
    st.title("Metas de Gastos")
    st.markdown("Defina limites para suas categorias e acompanhe o progresso.")
    
    df = st.session_state.transactions
    df_gastos = df[df['Valor'] < 0].copy()
    df_gastos['Valor'] = df_gastos['Valor'].abs()
    gastos_cat = df_gastos.groupby("Categoria")['Valor'].sum()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Progresso do Mês")
        for cat, limite in st.session_state.budgets.items():
            gasto_atual = gastos_cat.get(cat, 0.0)
            pct = min(gasto_atual / limite, 1.0)
            
            c_meta1, c_meta2 = st.columns([3, 1])
            with c_meta1:
                st.write(f"**{cat}** (R$ {gasto_atual:.2f} / R$ {limite:.2f})")
                color_bar = "red" if pct > 0.9 else "green"
                st.progress(pct, text=f"{pct*100:.0f}%")
            with c_meta2:
                diff = limite - gasto_atual
                if diff < 0:
                    st.error(f"Estourou R$ {abs(diff):.2f}")
                else:
                    st.success(f"Resta R$ {diff:.2f}")
            st.write("")
            
    with col2:
        st.subheader("Definir Metas")
        cat_edit = st.selectbox("Editar Categoria", list(st.session_state.budgets.keys()))
        new_limit = st.number_input(f"Novo limite para {cat_edit}", value=float(st.session_state.budgets[cat_edit]))
        if st.button("Atualizar Meta"):
            st.session_state.budgets[cat_edit] = new_limit
            st.toast("Meta atualizada!", icon="🎯")
            st.rerun()

# --- MÓDULO 4: ORÁCULO VFP ---
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
        
        renda_mensal = 18200.00 
        
        if st.button("Consultar Guardião", type="primary"):
            with st.spinner("O Guardião está consultando a sabedoria milenar..."):
                try:
                    impacto = (val_compra / renda_mensal) * 100
                    prompt = f"""
                    Você é o 'Guardião VFP' (Verdade, Fidelidade, Propósito).
                    Compra: {descricao} | Valor: R$ {val_compra:.2f}
                    Renda: R$ {renda_mensal:.2f} | Impacto: {impacto:.1f}% | Categoria: {categoria}
                    
                    Diretrizes:
                    1. Impacto > 30% = BLOQUEIO.
                    2. Supérfluo > 10% = Regra dos 72h.
                    3. Cite Bíblia se necessário.
                    4. Veredito: APROVADO, CUIDADO ou REPROVADO.
                    """
                    
                    output = replicate.run(
                        "meta/llama-3-8b-instruct",
                        input={"prompt": prompt, "max_tokens": 150}
                    )
                    st.markdown("### 📜 Veredito")
                    st.write("".join(output))
                    st.markdown("---")
                    
                    if impacto > 30:
                        st.progress(impacto/100, text="⚠️ Risco Crítico")
                    else:
                        st.progress(impacto/100, text="✅ Margem Segura")
                        
                except Exception as e:
                    st.error(f"Erro na IA: {e}")

    with col2:
        st.subheader("Princípios")
        st.info("💡 **Dica:** Antes de comprar, pergunte: Eu preciso? Eu posso pagar à vista? Isso me aproxima do meu propósito?")

# --- MÓDULO 5: PLANOS ---
elif menu == "💎 Planos":
    st.title("Assinatura Castelo Forte")
    c1, c2 = st.columns(2)
    with c1:
        st.success("✅ **Plano Atual: App MVP (R$ 79,90)**")
        st.write("- Acesso total ao Oráculo")
        st.write("- Gestão de Metas")
    with c2:
        st.info("🚀 **Upgrade: Standard (R$ 497,00)**")
        st.write("- Consultoria Humana")
        st.button("Fazer Upgrade")
