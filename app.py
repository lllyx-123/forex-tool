import streamlit as st

st.set_page_config(page_title="跨币种外汇投资模拟器", layout="centered")
st.title("💱 跨币种外汇投资模拟工具")

st.markdown("模拟从本币换汇美元投资后结汇回本币的盈亏情况")

# ✅ 多币种设置
currency_options = {
    "人民币 (CNY)": 1,
    "美元 (USD)": None,
    "日元 (JPY)": 0.064,
    "欧元 (EUR)": 7.8
}
currency_names = list(currency_options.keys())
selected_currency = st.selectbox("💵 初始资金币种", currency_names)

# 默认初始金额（以本币计）
amount = st.number_input(f"💰 初始投资金额（{selected_currency.split()[0]}）", min_value=0.0, value=10000.0, step=100.0)

# 汇率输入
buy_rate = st.number_input("🔄 换汇汇率（本币兑USD）", min_value=0.01, value=7.2)
buy_fee = st.slider("💸 换汇手续费（%）", 0.0, 5.0, 0.0, step=0.1)

sell_rate = st.number_input("🔁 结汇汇率（USD兑本币）", min_value=0.01, value=7.1)
sell_fee = st.slider("💸 结汇手续费（%）", 0.0, 5.0, 0.0, step=0.1)

# 投资收益率
return_rate = st.slider("📈 美元投资收益率（%）", min_value=-100.0, max_value=100.0, value=4.0, step=0.1)

# 汇率换算 + 手续费处理
usd_invested = (amount / buy_rate) * (1 - buy_fee / 100)
usd_final = usd_invested * (1 + return_rate / 100)
final_amount = usd_final * sell_rate * (1 - sell_fee / 100)

# 盈亏
profit = final_amount - amount
roi = (profit / amount * 100) if amount != 0 else 0

# 输出结果
st.subheader("📊 模拟结果")

col1, col2, col3 = st.columns(3)
col1.metric("💵 美元投资金额", f"${usd_invested:,.2f}")
col2.metric(f"🔚 回本币金额", f"{final_amount:,.2f} {selected_currency.split()[0]}")
col3.metric("📈 盈亏", f"{profit:,.2f}", delta=f"{roi:.2f}%")

# 图表
st.bar_chart({
    "金额": {
        "初始金额": amount,
        "结汇后": final_amount
    }
})

st.caption("提示：手续费模拟为换汇/结汇中银行或平台抽取的点差，不含税收。")
