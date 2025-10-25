import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Home - Stock Recommender",
    page_icon="💼",
    layout="wide"
)

# Main content
st.title("💼 Aadya's Stock Recommender")

st.markdown("""
Welcome to your personal **Stock Discovery and Portfolio Simulator**!

This app helps you explore stocks and simulate portfolio performance. Use the navigation 
in the sidebar to access different features:

- 🔍 **Discover Stocks**: Explore trending stocks and analyze their metrics
- 📈 **Portfolio Simulator**: Build and visualize your portfolio performance

---

### 🚀 Getting Started

1. **Discover**: Browse through available stocks and their key metrics
2. **Portfolio**: Add stocks to your portfolio and track simulated performance
3. **Analyze**: View charts, returns, and insights about your investments

*This is a simulation tool for educational purposes. Always do your own research before making real investment decisions.*
""")

# Add some visual elements
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📊 Available Stocks",
        value="500+",
        delta="Live Data"
    )

with col2:
    st.metric(
        label="📈 Portfolio Tools",
        value="Advanced",
        delta="Simulation Ready"
    )

with col3:
    st.metric(
        label="🔄 Real-time Updates",
        value="Enabled",
        delta="Auto Refresh"
    )

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; font-size: 0.8em;">💼 Built by Aadya — Powered by Streamlit</div>',
    unsafe_allow_html=True
)
