import streamlit as st

def about():
    # Title and subtitle
    st.title("About  ProcurAlytics🛠️")
    st.markdown(""" 
    Welcome to **ProcurAlytics**, a revolutionary tool designed to transform procurement processes for **Tata Steel Downstream Products Limited (TSDPL)**.  
    By leveraging the power of **Generative AI**, we aim to optimize costs, ensure compliance, and streamline operations.  
    """)

    # Topic overview with visuals
    st.markdown("### What is ProcurAlytics? 🤖")
    st.write("""
    ProcurAlytics harnesses artificial intelligence to analyze and optimize **Purchase Requests (PRs)** and **Purchase Orders (POs)**.  
    It provides actionable insights to ensure procurement is cost-effective, efficient, and compliant with company policies.
    """)

    

    # Key features section
    st.markdown("### Key Features 🚀")
    st.write("""
    1. **Automated Spend Categorization**:  
       Classify PRs and POs into meaningful categories for better visibility and management.  
       
    2. **Cost Optimization Insights**:  
       Gain recommendations to minimize costs and identify savings opportunities.  
       
    3. **Supplier Analysis**:  
       Evaluate suppliers based on performance, cost-effectiveness, and reliability.  
       
    4. **Spend Forecasting**:  
       Predict future spending patterns using advanced machine learning algorithms.  
    """)

    # Why it matters section
    st.markdown("### Why Does It Matter? 🌟")
    st.info("""
    - **Cost Efficiency**: Save money by identifying cost-saving opportunities.  
    - **Improved Compliance**: Ensure procurement aligns with company policies.  
    - **Data-Driven Decisions**: Leverage AI insights to make smarter choices.  
    - **Supplier Reliability**: Choose the right suppliers with confidence.  
    """)

    # Interactive section
    st.markdown("### How It Works 🔧")
    with st.expander("Click to learn about the technology behind Procurement GenAI"):
        st.write("""
        Procurement GenAI uses **Natural Language Processing (NLP)** and **Machine Learning (ML)** to:  
        - Analyze unstructured data in PRs and POs.  
        - Categorize spend data into structured formats.  
        - Provide predictions and insights for optimization.  
        """)

    # Footer
    st.markdown("---")
    st.markdown("Built with ❤️ for TSDPL to redefine procurement excellence.")


about()


