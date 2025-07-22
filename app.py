import streamlit as st

st.set_page_config(page_title="外汇投资工具", layout="centered")

st.title("💱 外汇投资模拟工具")

usd = st.number_input("💵 投资金额（美元）", value=1000.0)
entry = st.number_input("🔒 买入汇率", value=7.2)
exit = st.number_input("📈 卖出汇率", value=7.0)
fee = st.slider("🧾 手续费（%）", 0.0, 5.0, 0.0)

initial = usd * entry
final = usd * exit * (1 - fee / 100)
profit = final - initial
rate = (profit / initial * 100) if initial != 0 else 0

st.metric("盈亏金额（¥）", f"{profit:,.2f}", delta=f"{rate:.2f}%")
