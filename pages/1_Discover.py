import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Discover - Stock Recommender",
    page_icon="🔍",
    layout="wide"
)

# Main content
st.title("🔍 Discover Stocks")

st.markdown("""
Explore and analyze stocks with comprehensive metrics and insights. This page will contain:

- **Stock Cards**: Visual cards showing key metrics for each stock
- **Search & Filter**: Find stocks by ticker, sector, or performance criteria
- **Real-time Data**: Live price updates and market information
- **Analytics**: Technical indicators, trends, and recommendations

*Backend integration coming soon - this is a placeholder for future stock discovery features.*
""")

# Placeholder content
st.info("🚧 **Coming Soon**: Stock discovery features are under development. This will include real-time stock data, filtering options, and detailed analytics.")

# Sample placeholder cards
st.subheader("📊 Sample Stock Cards")
st.markdown("*These are placeholder cards - real data integration coming soon*")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown("""
        **Apple Inc. (AAPL)**
        - Price: $150.00
        - Change: +2.5%
        - Volume: 45M
        """)
        st.button("Add to Portfolio", key="aapl", disabled=True)

with col2:
    with st.container():
        st.markdown("""
        **Microsoft Corp. (MSFT)**
        - Price: $300.00
        - Change: +1.8%
        - Volume: 32M
        """)
        st.button("Add to Portfolio", key="msft", disabled=True)

with col3:
    with st.container():
        st.markdown("""
        **Tesla Inc. (TSLA)**
        - Price: $200.00
        - Change: -0.5%
        - Volume: 28M
        """)
        st.button("Add to Portfolio", key="tsla", disabled=True)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; font-size: 0.8em;">💼 Built by Aadya — Powered by Streamlit</div>',
    unsafe_allow_html=True
)
