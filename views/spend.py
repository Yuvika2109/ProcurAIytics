import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_excel(
    io="Book2.xlsx",
    engine="openpyxl",
    sheet_name="Sheet1"
)

# Sidebar filters
st.sidebar.header("Please enter filter here:")
category = st.sidebar.selectbox(
    "Select a particular Category",
    options=df["category"].unique()
)
scale_options = {"Rupees": 1, "Lakhs": 1e5, "Crores": 1e7}
scale_label = st.sidebar.selectbox("Select scale for Spend", list(scale_options.keys()))
scale_factor = scale_options[scale_label]
df["Scaled Spend"] = df["spend"] / scale_factor
# Title
st.markdown(
    """
    <h1 style='text-align: center;'>&#128202; Spend Dashboard</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("#")

# Total Spend for all categories combined
total_spend_all_categories = df["spend"].sum()
scaled_total_spend_all_categories = total_spend_all_categories / scale_factor
left_column, middle_column, right_column = st.columns(3)
with middle_column:
    st.subheader("Total Spend:")
    st.subheader(f"{scaled_total_spend_all_categories:,.2f} {scale_label}")

st.markdown("---")
total_spend_by_category = df.groupby("category")["spend"].sum().reset_index()
total_spend_by_category["Scaled Spend"] = total_spend_by_category["spend"] / scale_factor
bar_fig = px.bar(
    total_spend_by_category,
    x="category",
    y="Scaled Spend",
    title=f"Total Spend by Category ({scale_label})",
    color="category",
    text_auto=True,
    template="plotly_white"
)
bar_fig.update_yaxes(title_text=f"Spend ({scale_label})")
bar_fig.update_xaxes(title_text="Category")

st.plotly_chart(bar_fig, use_container_width=True)

df_filtered = df[df["category"] == category].copy()
if not df_filtered.empty:
    pie_fig = px.pie(
        df_filtered,
        names="code",  
        values="spend",
        title=f"Spend Distribution for {category} (in {scale_label})",
        template="plotly_white",
        hole=0.4  
    )
    pie_fig.update_traces(
        textinfo="percent+label",  
        textposition="inside"      
    )

    st.plotly_chart(pie_fig, use_container_width=True)

    
    st.markdown(f"### Material Codes and Descriptions for {category}")
    st.dataframe(df_filtered[["code", "description","spend"]].sort_values("spend", ascending=False).reset_index(drop=True), use_container_width=True)  
else:
    st.warning(f"No data available for category: {category}") 









