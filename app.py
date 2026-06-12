import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------------------------------
# Page setup
# ---------------------------------------------------
st.set_page_config(
    page_title="Luxury Housing Sales Analysis Dashboard",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Load data
# ---------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_luxury_housing.csv")

    # Basic cleaning
    df.columns = df.columns.str.strip()

    # Safe conversions
    numeric_cols = [
        "Unit_Size_Sqft", "Ticket_Price_Cr", "Connectivity_Score",
        "Amenity_Score", "Locality_Infra_Score", "Avg_Traffic_Time_Min",
        "Price_per_Sqft", "Quarter_Number", "Booking_Flag"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Clean price column
    if "Price_per_Sqft" in df.columns:
        df = df[df["Price_per_Sqft"] > 0]
        df = df[df["Price_per_Sqft"] < 100000]

    # Purchase quarter date
    if "Purchase_Quarter" in df.columns:
        df["Purchase_Quarter"] = pd.to_datetime(df["Purchase_Quarter"])
        df["Year_Quarter"] = df["Purchase_Quarter"].dt.to_period("Q").astype(str)
    else:
        df["Year_Quarter"] = None

    # Booking status column for stacked charts
    if "Booking_Flag" in df.columns:
        df["Booking_Status"] = df["Booking_Flag"].map({1: "Booked", 0: "Not Booked"})
    else:
        df["Booking_Status"] = "Unknown"

    # Quarter label
    if "Quarter_Number" in df.columns:
        df["Quarter_Label"] = df["Quarter_Number"].apply(
            lambda x: f"Q{int(x)}" if pd.notnull(x) else None
        )

    return df


df = load_data()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Analysis 1", "Analysis 2", "Analysis 3"])

# ---------------------------------------------------
# HOME
# ---------------------------------------------------
if page == "Home":
    st.markdown("""
    <div style='text-align: center; margin-top: 110px;'>
        <h1 style='color:#F5B041; font-size:56px; font-weight:bold;'>
            Luxury Housing Sales Analysis Dashboard
        </h1>
        <p style='color:#D5D8DC; font-size:22px;'>
            A quick look at booking trends, pricing patterns, and buyer behavior in the luxury housing market.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# ANALYSIS 1 : Q1 to Q4
# ---------------------------------------------------
elif page == "Analysis 1":
    st.markdown("""
    <h2 style='text-align: center; color:#F5B041;'>📊 Analysis 1: Market Trends & Performance</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Q1 Market Trends
    with col1:
        top_markets = (
            df.groupby("Micro_Market")["Booking_Flag"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .index
        )

        q1 = df[df["Micro_Market"].isin(top_markets)]
        q1 = q1.groupby(["Quarter_Label", "Micro_Market"], as_index=False)["Booking_Flag"].sum()

        quarter_order = ["Q1", "Q2", "Q3", "Q4"]
        q1["Quarter_Label"] = pd.Categorical(
            q1["Quarter_Label"],
            categories=quarter_order,
            ordered=True
        )
        q1 = q1.sort_values("Quarter_Label")

        fig1 = px.line(
            q1,
            x="Quarter_Label",
            y="Booking_Flag",
            color="Micro_Market",
            markers=True,
        )

        fig1.update_layout(
            title={
                "text": "Q1. Market Trends: Bookings by Quarter Across Top Micro Markets",
                "x": 0.5,
                "xanchor": "center"
            },
            xaxis_title="Quarter",
            yaxis_title="Booking Count")
        
        st.plotly_chart(fig1)


    #----------- Q2 Builder Performance------------

    with col2:
        q2 = (
            df.groupby("Developer_Name", as_index=False).agg(Total_Sales=("Ticket_Price_Cr", "sum"),
            Avg_Ticket_Size=("Ticket_Price_Cr", "mean")).sort_values("Total_Sales", ascending=False).head(10))
        
        q2["Rank"] = range(1, len(q2)+1)
        q2["Label"] = q2["Rank"].astype(str) + ". " + q2["Developer_Name"]

        fig2 = px.bar(q2,
        x="Total_Sales",
        y="Developer_Name",
        orientation="h",
        color="Total_Sales",
        color_continuous_scale="Blues")

        fig2.update_layout(
        title={ "text":"Q2. Builder Performance: Highest Total Ticket Sales", "x":0.5, "xanchor":"center" },
        xaxis_title="Total Sales (Cr)",
        yaxis_title="Builder",
        height=400,
        coloraxis_showscale=False)

        # ✅ Keep ONLY ONE of each
        fig2.update_yaxes(categoryorder="total ascending")

        fig2.update_traces(
            texttemplate='%{x:.0f}',
            textposition='outside'
        )

        st.plotly_chart(fig2)

    st.write("")
    st.write("")

    col3, col4 = st.columns(2)

    # Q3: Amenity Impact (Aggregated)
    with col3:
        q3 = (
            df.groupby("Micro_Market", as_index=False)
            .agg(
                Amenity_Score=("Amenity_Score", "mean"),
                Conversion_Rate=("Booking_Flag", "mean"),
                Avg_Price=("Ticket_Price_Cr", "mean")
            )
            .sort_values("Conversion_Rate", ascending=False)
            .head(10)
        )

        fig3 = px.scatter(
            q3,
            x="Amenity_Score",
            y="Conversion_Rate",
            size="Avg_Price",
            color="Conversion_Rate",
            color_continuous_scale="Viridis",
            text="Micro_Market"
        )

        fig3.update_traces(
            textposition="top center",
            marker=dict(line=dict(width=1, color="white"))
        )

        fig3.update_layout(
            title={
                "text": "Q3. Amenity Score vs Booking Conversion Rate",
                "x": 0.5,
                "xanchor": "center"
            },
            xaxis_title="Avg Amenity Score",
            yaxis_title="Conversion Rate",
            height=400,
            showlegend=False,
            coloraxis_colorbar_title="Conversion Rate"
        )

        st.plotly_chart(fig3)


    # Q4 Booking Conversion (Percentage View)
    with col4:
        df_q4 = df.copy()
        df_q4["Booking_Status"] = df_q4["Booking_Flag"].map({1: "Booked", 0: "Not Booked"})

        top_bottom = (
            df_q4.groupby("Micro_Market")["Booking_Flag"]
            .mean()
            .sort_values(ascending=False)
        )

        selected_markets = list(top_bottom.head(5).index) + list(top_bottom.tail(5).index)

        df_q4 = df_q4[df_q4["Micro_Market"].isin(selected_markets)]

        q4 = (
            df_q4.groupby(["Micro_Market", "Booking_Status"])
            .size()
            .reset_index(name="Count")
        )

        q4["Percentage"] = q4.groupby("Micro_Market")["Count"].transform(
            lambda x: x / x.sum() * 100
        )

        fig4 = px.bar(
            q4,
            x="Micro_Market",
            y="Percentage",
            color="Booking_Status",
            barmode="stack",
            color_discrete_map={
                "Booked": "#4FC3F7",
                "Not Booked": "#90A4AE"
            }
        )

        fig4.update_traces(
            marker_line_width=0.5,
            marker_line_color="white"
        )

        fig4.update_layout(
            title={
                "text": "Q4. Booking Conversion Rate (%) by Micro Market",
                "x": 0.5,
                "xanchor": "center"
            },
            xaxis_title="Micro Market",
            yaxis_title="% Booking Status",
            xaxis_tickangle=-30,
            height=400,
            legend_title_text="Booking Status"
        )

        st.plotly_chart(fig4)

# ---------------------------------------------------
# ANALYSIS 2 : Q5 to Q7
# ---------------------------------------------------
elif page == "Analysis 2":
    st.markdown("""
    <h2 style='color:#F5B041;'>💰 Analysis 2: Demand, Sales Channel & Builder Contribution</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Q5 Configuration Demand

    with col1:
        q5 = (df.groupby("Configuration", as_index=False)["Booking_Flag"].sum().sort_values("Booking_Flag", ascending=False))
        
        fig5 = px.pie(
            q5,
            names="Configuration",
            values="Booking_Flag",
            hole=0.55,
            color_discrete_sequence=[
            "#4FC3F7",
            "#7C4DFF",
            "#26A69A",
            "#FFB74D",
            "#EC407A"])

        fig5.update_traces(
            textinfo="percent+label",
            pull=[0.03, 0, 0, 0, 0])

        fig5.update_layout(
            title={
                "text": "Q5. Configuration Demand (Bookings Share)",
                "x": 0.5,
                "xanchor": "center"
            },
            legend_title="Configuration",
            height=420
        )

        st.plotly_chart(fig5)

    # ==================================================
    # Q6 SALES CHANNEL EFFICIENCY
    # ==================================================

    with col2:

    # Create Booking Status
        df_q6 = df.copy()

        df_q6["Booking_Status"] = df_q6["Booking_Flag"].map({
            1: "Booked",
            0: "Not Booked"
        })

        # Group data
        q6 = (
            df_q6.groupby(["Sales_Channel", "Booking_Status"])
            .size()
            .reset_index(name="Count")
        )

        # Convert to percentage
        q6["Percentage"] = q6.groupby("Sales_Channel")["Count"].transform(
            lambda x: x / x.sum() * 100
        )

        # Plot
        fig6 = px.bar(
            q6,
            x="Sales_Channel",
            y="Percentage",
            color="Booking_Status",
            barmode="stack",
            text=q6["Percentage"].round(1).astype(str) + "%",
            color_discrete_map={
                "Booked": "#00C49A",
                "Not Booked": "#7F8C8D"
            }
        )

        fig6.update_traces(
            textposition="inside"
        )

        fig6.update_layout(
            title={
                "text": "Q6. Booking Conversion Rate by Sales Channel",
                "x": 0.5,
                "xanchor": "center"
            },
            xaxis_title="Sales Channel",
            yaxis_title="Percentage (%)",
            yaxis=dict(range=[0, 100]),
            legend_title="Booking Status",
            height=420
        )

        st.plotly_chart(fig6)

        st.write("")
        st.write("")


    # ==================================================
    # Q7 QUARTERLY BUILDER CONTRIBUTION
    # ==================================================

    st.markdown(
    "<h5 style='text-align:center;'> Q7. Quarterly Builder Contribution </h5>",
    unsafe_allow_html=True)

    # Create matrix table
    q7 = pd.pivot_table(df,
        values="Ticket_Price_Cr",
        index="Developer_Name",
        columns="Quarter_Label",
        aggfunc="sum")

    # Round values
    q7 = q7.round(0)

    # Optional → sort by total sales
    q7["Total"] = q7.sum(axis=1)
    q7 = q7.sort_values("Total", ascending=False).drop(columns="Total")

    # Display
    st.dataframe(q7)

# ---------------------------------------------------
# ANALYSIS 3 : Q8 to Q10
# ---------------------------------------------------
elif page == "Analysis 3":

    st.markdown("""
    <h2 style='color:#F5B041;'>📍 Analysis 3: Possession, Geography & Top Performers</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # ==================================================
    # Q8 POSSESSION STATUS ANALYSIS
    # ==================================================
    with col1:

        q8 = df.copy()

        # Convert booking flag to labels
        q8["Booking_Status"] = q8["Booking_Flag"].map({
            1: "Booked",
            0: "Not Booked"
        })

        # Group data
        q8 = (
            q8.groupby(
                ["Possession_Status", "Booking_Status", "Buyer_Type"],
                as_index=False
            )
            .size()
            .rename(columns={"size": "Count"})
        )

        # Plot
        fig8 = px.bar(
            q8,
            x="Possession_Status",
            y="Count",
            color="Buyer_Type",
            barmode="group",
            facet_col="Booking_Status",
            text="Count",
            color_discrete_sequence=[
                "#4FC3F7",
                "#AB47BC",
                "#26A69A",
                "#FFA726"
            ]
        )

        fig8.update_traces(
            textposition="outside"
        )

        fig8.update_layout(
            title={
                "text": "Q8. Possession Status vs Booking Decisions",
                "x": 0.5,
                "xanchor": "center"
            },
            xaxis_title="Possession Status",
            yaxis_title="Count",
            legend_title="Buyer Type",
            height=500
        )

        st.plotly_chart(fig8)

    # ==================================================
    # Q9 GEOGRAPHICAL INSIGHTS:
    # ==================================================

    with col2:
        q9 = (
            df.groupby("Micro_Market", as_index=False)
            .agg(Project_Count=("Property_ID", "count"))
            .sort_values("Project_Count", ascending=False)
            .head(10))

        fig9 = px.bar(
            q9,
            x="Project_Count",
            y="Micro_Market",
            orientation="h",
            title="Q9. Geographical Insights: Project Concentration by Micro Market")
            
        fig9.update_layout(
            title_x=0.5,
            xaxis_title="Project Count",
            yaxis_title="Micro Market")
        
        
        fig9.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig9)
        st.write("")
        st.write("")

    # ==================================================
    # Q10 TOP PERFORMERS
    # ==================================================

    st.markdown(
    "<h2 style='text-align:center;'> Q10. Top Performers </h2>",
    unsafe_allow_html=True)

    # Top builders by revenue
    top_builders = (
        df.groupby("Developer_Name")
        .agg(
            Revenue=("Ticket_Price_Cr", "sum"),
            Successful_Bookings=("Booking_Flag", "sum")
        )
        .sort_values("Revenue", ascending=False)
        .head(5)
        .reset_index()
    )

    # KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i, row in top_builders.iterrows():

        with cols[i]:

            st.metric(
                label=row["Developer_Name"],
                value=f"₹ {row['Revenue']:,.0f} Cr",
                delta=f"{int(row['Successful_Bookings'])} Bookings"
            )
            st.write("")

    st.markdown("### Top 5 Builder Performance")

    st.dataframe(top_builders)