import streamlit as st

# 页面设置
st.set_page_config(page_title="外汇投资模拟器", layout="centered")
st.title("💱 外汇投资模拟器")

st.markdown("模拟本币换汇美元投资，并结汇回本币后的盈亏情况")

# 🪙 币种设置
currency_options = {
    "人民币 (CNY)": "¥",
    "美元 (USD)": "$",
    "日元 (JPY)": "¥",
    "欧元 (EUR)": "€"
}
currency_names = list(currency_options.keys())
selected_currency = st.selectbox("🌍 初始资金币种", currency_names)
symbol = currency_options[selected_currency]

# 💰 输入初始资金 & 汇率
amount = st.number_input(f"💰 初始资金（{selected_currency.split()[0]}）", min_value=0.0, value=10000.0, step=100.0)
buy_rate = st.number_input("🔄 换汇汇率（本币兑USD）", min_value=0.01, value=7.2)
sell_rate = st.number_input("🔁 结汇汇率（USD兑本币）", min_value=0.01, value=7.1)

# 📈 投资收益率滑动条（0.1 步进，附参考刻度）
st.markdown("📈 美元投资收益率（%）")
return_rate = st.slider(" ", min_value=-50.0, max_value=50.0, value=4.0, step=0.1, label_visibility="collapsed")

st.markdown(
    """
    <div style="font-size: 14px; color: gray; margin-top: -10px; margin-bottom: 15px;">
    🎯 常用参考点：<span style="margin: 0 10px;">-40%</span>
    <span style="margin: 0 10px;">-30%</span><span style="margin: 0 10px;">-20%</span>
    <span style="margin: 0 10px;">-10%</span><span style="margin: 0 10px;">0%</span>
    <span style="margin: 0 10px;">10%</span><span style="margin: 0 10px;">20%</span>
    <span style="margin: 0 10px;">30%</span><span style="margin: 0 10px;">40%</span>
    </div>
    """,
    unsafe_allow_html=True
)

# 🧮 计算逻辑
usd_invested = amount / buy_rate
usd_final = usd_invested * (1 + return_rate / 100)
final_amount = usd_final * sell_rate
profit = final_amount - amount
roi = (profit / amount * 100) if amount != 0 else 0

# 📊 显示结果
st.subheader("📊 模拟结果")

col1, col2, col3 = st.columns(3)
col1.metric("💵 美元投资金额", f"${usd_invested:,.2f}")
col2.metric("🔚 回本币金额", f"{symbol}{final_amount:,.2f}")
col3.metric("📈 盈亏", f"{symbol}{profit:,.2f}", delta=f"{roi:.2f}%")

# 📉 图表对比
st.bar_chart({
    "金额": {
        "初始资金": amount,
        "结汇后": final_amount
    }
})

st.caption("本工具仅作投资趋势模拟参考，未考虑税费与真实交易成本。")
