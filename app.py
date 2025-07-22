import streamlit as st

st.set_page_config(page_title="跨币种投资模拟器", layout="centered")
st.title("🌍 跨币种投资收益模拟工具")

st.markdown("模拟不同币种资金换汇 → 美元投资 → 再结汇回原币种的全过程。")

# 多币种支持
currency_options = {
    "人民币 CNY": 1,
    "美元 USD": 1,
    "日元 JPY": 0.0065,
    "欧元 EUR": 1.1
}

currency = st.selectbox("💱 选择初始投资币种", options=list(currency_options.keys()))
currency_code = currency.split()[1]

# 汇率输入
st.markdown("### 📥 汇率 & 投资参数")
col1, col2 = st.columns(2)
with col1:
    initial_amount = st.number_input(f"💰 初始投资金额（{currency_code}）", min_value=0.0, value=10000.0, step=100.0)
with col2:
    buy_rate = st.number_input(f"🔄 换汇汇率（{currency_code}兑USD）", min_value=0.0001, value=currency_options[currency], step=0.0001)

col3, col4 = st.columns(2)
with col3:
    sell_rate = st.number_input(f"🔁 结汇汇率（USD兑{currency_code}）", min_value=0.0001, value=1/currency_options[currency], step=0.0001)
with col4:
    return_rate = st.slider("📈 美元投资收益率（%）", min_value=-100.0, max_value=100.0, value=4.0, step=0.1)

# 成本模拟
st.markdown("### 🧾 成本参数")
col5, col6 = st.columns(2)
with col5:
    fee_rate = st.slider("💸 换汇手续费（%）", 0.0, 5.0, 0.5, step=0.1)
with col6:
    tax_rate = st.slider("🧾 税费/资本利得税（%）", 0.0, 30.0, 10.0, step=1.0)

# 模拟过程
usd_invested = (initial_amount * (1 - fee_rate / 100)) / buy_rate
usd_final = usd_invested * (1 + return_rate / 100) * (1 - tax_rate / 100)
final_amount = usd_final * sell_rate
profit = final_amount - initial_amount
roi = (profit / initial_amount * 100) if initial_amount != 0 else 0

# 显示结果
st.markdown("### 📊 模拟结果")
col7, col8, col9 = st.columns(3)
col7.metric("💵 美元投资金额", f"${usd_invested:,.2f}")
col8.metric(f"💰 回本金额（{currency_code}）", f"{final_amount:,.2f}")
col9.metric(f"📈 盈亏（{currency_code}）", f"{profit:,.2f}", delta=f"{roi:.2f}%")

# 图表
st.bar_chart({
    f"{currency_code} 金额": {
        "初始资金": initial_amount,
        "结汇后": final_amount
    }
})

st.caption("汇率、手续费、税费等参数仅供模拟使用，不构成投资建议。")
