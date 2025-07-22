import streamlit as st

# 页面设置
st.set_page_config(page_title="外汇投资模拟器", layout="centered")
st.title("💱 外汇投资模拟器")

st.markdown("模拟将本币兑换成美元投资后再结汇回来的盈亏情况")

# 币种与符号设置
currency_options = {
    "人民币 (CNY)": "¥",
    "美元 (USD)": "$",
    "日元 (JPY)": "¥",
    "欧元 (EUR)": "€"
}
currency_names = list(currency_options.keys())
selected_currency = st.selectbox("🌍 初始资金币种", currency_names)
symbol = currency_options[selected_currency]

# 输入参数
amount = st.number_input(f"💰 初始资金（{selected_currency.split()[0]}）", min_value=0.0, value=10000.0, step=100.0)
buy_rate = st.number_input("🔄 换汇汇率（本币兑USD）", min_value=0.01, value=7.2)
sell_rate = st.number_input("🔁 结汇汇率（USD兑本币）", min_value=0.01, value=7.1)

# 投资收益率
return_rate = st.slider(
    "📈 美元投资收益率（%）",
    min_value=-50.0,
    max_value=50.0,
    value=4.0,
    step=0.1
)

# 计算逻辑
usd_invested = amount / buy_rate
usd_final = usd_invested * (1 + return_rate / 100)
final_amount = usd_final * sell_rate
profit = final_amount - amount
roi = (profit / amount * 100) if amount != 0 else 0

# 结果展示
st.subheader("📊 模拟结果")

col1, col2, col3 = st.columns(3)
col1.metric("💵 美元投资金额", f"${usd_invested:,.2f}")
col2.metric("🔚 回本币金额", f"{symbol}{final_amount:,.2f}")
col3.metric("📈 盈亏", f"{symbol}{profit:,.2f}", delta=f"{roi:.2f}%")

# 图表展示
st.bar_chart({
    "金额": {
        "初始资金": amount,
        "结汇后": final_amount
    }
})

st.caption("本工具仅作投资趋势模拟参考，未考虑税费与真实交易成本。")
