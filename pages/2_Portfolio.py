import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Portfolio - Stock Recommender",
    page_icon="📈",
    layout="wide"
)

# Main content
st.title("📈 Portfolio Simulator")

st.markdown("""
Build and analyze your investment portfolio with advanced simulation tools. This page will include:

- **Portfolio Builder**: Add/remove stocks and set allocation percentages
- **Performance Charts**: Interactive charts showing portfolio growth over time
- **Risk Analysis**: Portfolio risk metrics and diversification insights
- **Backtesting**: Historical performance simulation
- **Real-time Updates**: Live portfolio value tracking

*Backend integration coming soon - this is a placeholder for future portfolio simulation features.*
""")

# Placeholder content
st.info("🚧 **Coming Soon**: Portfolio simulation features are under development. This will include real-time portfolio tracking, advanced analytics, and interactive charts.")

# Sample portfolio visualization
st.subheader("📊 Sample Portfolio Overview")
st.markdown("*This is a placeholder visualization - real portfolio tracking coming soon*")

# Portfolio summary metrics
st.subheader("📈 Portfolio Summary")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Value", "$100,000", "5.2%")

with col2:
    st.metric("Total Return", "8.7%", "2.1%")

with col3:
    st.metric("Best Performer", "GOOGL", "15.7%")

with col4:
    st.metric("Worst Performer", "TSLA", "-2.1%")
    
# Sample data
sample_data = {
    'Stock': ['AAPL', 'MSFT', 'TSLA', 'GOOGL', 'AMZN'],
    'Allocation': [25, 20, 15, 20, 20],
    'Value': [25000, 20000, 15000, 20000, 20000],
    'Return': [8.5, 12.3, -2.1, 15.7, 6.8]
}

df = pd.DataFrame(sample_data)

# Portfolio allocation pie chart
col1, col2 = st.columns(2)

with col1:
    st.subheader("Portfolio Allocation")
    fig_pie = px.pie(df, values='Allocation', names='Stock', 
                     title="Portfolio Distribution",
                     color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_pie, width='stretch')

with col2:
    st.subheader("Individual Returns")
    fig_bar = px.bar(df, x='Stock', y='Return', 
                     title="Stock Performance (%)",
                     color='Return',
                     color_continuous_scale='RdYlGn')
    st.plotly_chart(fig_bar, width='stretch')


# Sample portfolio table
st.subheader("📋 Portfolio Holdings")
st.dataframe(df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; font-size: 0.8em;">💼 Built by Aadya — Powered by Streamlit</div>',
    unsafe_allow_html=True
)