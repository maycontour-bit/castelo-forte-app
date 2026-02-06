import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Castelo Forte",
    page_icon="🏰",
    layout="mobile",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .stMetric {background-color: #fff; padding: 10px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);}
    .plan-card {background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #e9ecef; margin-bottom: 10px;}
    .plan-title {font-size: 18px; font-weight: bold; color: #2c3e50;}
    .plan-price {font-size: 16px; color: #27ae60; font-weight: bold;}
    .locked {opacity: 0.6; filter: grayscale(100%);}
    </style>
""", unsafe_allow_html=True)

# --- STATE ---
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Data', 'Descrição', 'Categoria', 'Valor', 'Tipo'])
if 'plano_atual' not in st.session_state:
    st.session_state.plano_atual = "Castelo Digital (App)"

# --- NAVEGAÇÃO ---
st.sidebar.image("https://img.icons8.com/color/96/castle.png", width=50)
menu = st.sidebar.radio("Menu", ["🏰 Dashboard", "💰 Lançamentos", "🔮 Oráculo VFP", "💎 Planos & Serviços"])

# --- PÁGINA 1: DASHBOARD ---
if menu == "🏰 Dashboard":
    st.title("Meu Castelo")
    
    # Simulação Pluggy
    if st.button("🔗 Conectar Conta Bancária (Pluggy)"):
        st.toast("Iniciando conexão segura com Pluggy...", icon="🔒")
        st.info("Aqui abrirá o widget da Pluggy para o cliente digitar a senha do banco.")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    saldo = 12500.00 # Exemplo
    col1.metric("Saldo Global", f"R$ {saldo:,.2f}")
    col2.metric("Saídas Mês", "R$ 3.450,00", delta="-12%")
    
    st.subheader("Raio-X VIPE")
    # Dados fictícios para visualização
    chart_data = pd.DataFrame({
        'Categoria': ['Essencial', 'Estilo', 'Reino', 'Investimento'],
        'Valor': [2000, 800, 350, 300]
    }).set_index('Categoria')
    st.bar_chart(chart_data)

# --- PÁGINA 2: LANÇAMENTOS ---
elif menu == "💰 Lançamentos":
    st.title("Extrato Unificado")
    st.info("💡 Com o Pluggy conectado, seus gastos aparecerão aqui automaticamente.")
    
    with st.expander("Adicionar Manualmente"):
        with st.form("manual"):
            desc = st.text_input("Descrição")
            val = st.number_input("Valor")
            st.form_submit_button("Salvar")

# --- PÁGINA 3: ORÁCULO VFP ---
elif menu == "🔮 Oráculo VFP":
    st.title("Oráculo VFP 2.0")
    st.write("A ferramenta exclusiva para validar suas decisões.")
    # (Código da lógica VFP aqui - simplificado para visualização)
    renda = st.number_input("Renda Mensal", value=10000.0)
    parcela = st.number_input("Parcela do Projeto", value=3500.0)
    if st.button("Analisar"):
        comp = (parcela/renda)*100
        if comp > 30:
            st.error(f"❌ Risco Alto: {comp}% da renda comprometida.")
        else:
            st.success(f"✅ Aprovado: {comp}% da renda.")

# --- PÁGINA 4: VITRINE DE PLANOS (UPSELL) ---
elif menu == "💎 Planos & Serviços":
    st.title("Sua Jornada")
    st.write("Evolua seu plano para destravar mais poder e acompanhamento.")
    
    # Plano Atual
    st.markdown(f"""
    <div class='plan-card' style='border: 2px solid #27ae60;'>
        <div class='plan-title'>📱 Castelo Digital (SEU PLANO)</div>
        <div class='plan-price'>R$ 79,90/mês</div>
        <ul>
            <li>✅ App Gerenciador (Pluggy)</li>
            <li>✅ Oráculo VFP (Robô)</li>
            <li>✅ Teste VIP ID</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Plano Estandarte
    st.markdown("""
    <div class='plan-card'>
        <div class='plan-title'>⚔️ Plano Estandarte</div>
        <div class='plan-price'>R$ 497,00/mês</div>
        <ul>
            <li>✅ Tudo do Digital</li>
            <li>✨ <b>Reunião Mensal com Consultor</b></li>
            <li>✨ Análise de Carteira de Investimentos</li>
            <li>✨ Suporte WhatsApp Dedicado</li>
        </ul>
        <a href='#' style='text-decoration:none;'><button style='width:100%; background-color:#2c3e50; color:white; border:none; padding:10px; border-radius:5px;'>Falar com Consultor</button></a>
    </div>
    """, unsafe_allow_html=True)
    
    # Plano Legado
    st.markdown("""
    <div class='plan-card locked'>
        <div class='plan-title'>👑 Plano Legado</div>
        <div class='plan-price'>Sob Consulta</div>
        <ul>
            <li>✅ Planejamento Sucessório</li>
            <li>✅ Holding & Blindagem</li>
            <li>✅ Código da Família</li>
        </ul>
        <button disabled style='width:100%; padding:10px;'>Exclusivo para Membros</button>
    </div>
    """, unsafe_allow_html=True)
