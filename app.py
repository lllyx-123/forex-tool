import streamlit as st

st.set_page_config(page_title="外汇投资模拟器", layout="centered")
st.title("💱 外汇投资模拟器")

st.markdown("模拟本币换汇美元投资，并结汇回本币后的盈亏")

# 币种选择及符号
currency_options = {
    "人民币 (CNY)": "¥",
    "美元 (USD)": "$",
    "日元 (JPY)": "¥",
    "欧元 (EUR)": "€"
}
currency_names = list(currency_options.keys())
selected_currency = st.selectbox("🌍 初始资金币种", currency_names)
symbol = currency_options[selected_currency]

# 用户输入
amount = st.number_input(f"💰 初始资金（{selected_currency.split()[0]}）", min_value=0.0, value=10000.0, step=100.0)
buy_rate = st.number_input("🔄 换汇汇率（本币兑USD）", min_value=0.01, value=7.2)
sell_rate = st.number_input("🔁 结汇汇率（USD兑本币）", min_value=0.01, value=7.1)
return_rate = st.slider("📈 美元投资收益率（%）", -50.0, 50.0, 4.0, step=10.0)

# 模型计算
usd_invested = amount / buy_rate
usd_final = usd_invested * (1 + return_rate / 100)
final_amount = usd_final * sell_rate
profit = final_amount - amount
roi = (profit / amount * 100) if amount != 0 else 0

# 显示结果
st.subheader("📊 结果预览")

col1, col2, col3 = st.columns(3)
col1.metric("💵 美元投资金额", f"${usd_invested:,.2f}")
col2.metric("🔚 回本币金额", f"{symbol}{final_amount:,.2f}")
col3.metric("📈 盈亏", f"{symbol}{profit:,.2f}", delta=f"{roi:.2f}%")

# 可视化对比
st.bar_chart({
    "金额": {
        "初始资金": amount,
        "结汇后": final_amount
    }
})

st.caption("本工具简化手续费和税收计算，仅作趋势模拟。")
