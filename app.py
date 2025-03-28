import streamlit as st

# Function to calculate additional shares needed
def calculate_additional_shares(P1, Q1, P2, Pt):
    if P2 >= Pt:
        return "New purchase price must be lower than target price to average down."
    
    Q2 = (Pt * Q1 - P1 * Q1) / (P2 - Pt)
    return max(0, int(Q2))

# Streamlit UI
st.set_page_config(page_title="Stock Average Calculator", page_icon="📉")

st.title("📉 Stock Average Price Calculator")
st.write("Calculate how many shares you need to buy to reach a target average price.")

# User inputs
P1 = st.number_input("🔹 Enter initial purchase price per share:", min_value=0.01, value=50.0)
Q1 = st.number_input("🔹 Enter initial number of shares purchased:", min_value=1, value=100)
P2 = st.number_input("🔹 Enter new purchase price per share:", min_value=0.01, value=30.0)
Pt = st.number_input("🔹 Enter target average price per share:", min_value=0.01, value=40.0)

# Calculate button
if st.button("📊 Calculate"):
    result = calculate_additional_shares(P1, Q1, P2, Pt)
    st.success(f"✅ You need to buy **{result}** more shares at Rs.{P2} to reach an average price of Rs. {Pt}.")

st.markdown("---")
st.write("Developed by Aravindhaa Vijayakumar | 💡 [GitHub](https://github.com/yourprofile)")
