import streamlit as st

st.set_page_config(page_title="Castelo Forte", page_icon="🏰", layout="centered")

# CSS Limpo
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #d4af37;
    }
    .stButton>button {
        width: 100%;
        background-color: #d4af37;
        color: black;
        border: none;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    h1, h2, h3 { color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏰 Castelo Forte")
st.caption("Planejamento Financeiro & Princípios Eternos")

st.info("✅ Sistema Online (Modo Leve)")

# Dados Simples (Sem Pandas)
saldo = 12450.00
meta = 100000.00

col1, col2 = st.columns(2)
col1.metric("Saldo", f"R$ {saldo:,.2f}")
col2.metric("Meta", f"R$ {meta:,.2f}")

st.divider()

menu = st.radio("Menu", ["Oráculo VFP", "Planos"])

if menu == "Oráculo VFP":
    st.header("🔮 Oráculo")
    st.markdown("O sistema que previne a ruína antes dela acontecer.")
    val = st.number_input("Valor da Compra (R$)", 0.0)
    if st.button("Consultar Guardião"):
        if val > 2000:
            st.error("🚫 BLOQUEADO: Risco ao Castelo detectado.")
        else:
            st.success("✅ APROVADO: Compra segura.")

elif menu == "Planos":
    st.header("💎 Planos")
    st.write("Plano App: R$ 79,90/mês")
    st.write("Plano Standard: R$ 497/mês")
