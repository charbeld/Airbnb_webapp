import streamlit as st
import pandas as pd
import plotly.express as px

def Price_Min_Nights_Room_Type(df):

    st.sidebar.title("Filters")
    
    # Number slider for the maximum amount of minimum nights
    max_minimum_nights = st.sidebar.slider("Minimum Nights Range", min_value=0, max_value=500, value=350)

    # Multi-select box for filtering by room type
    selected_room_types = st.sidebar.multiselect("Select Room Types", df['room type'].unique(), default=['Private room'])

    # Create a subset DataFrame based on the selected filters
    subset_df = df[(df['minimum nights'] >= 0) & (df['minimum nights'] <= max_minimum_nights) & (df['room type'].isin(selected_room_types))]

    fig = px.scatter(
        subset_df,
        x="minimum nights",
        y="price",
        color="room type",
        template='plotly_white'
    )

    # Remove gridlines and update axes
    fig.update_xaxes(showgrid=False, title_text="Minimum Nights")
    fig.update_yaxes(showgrid=False, title_text="Price")

    fig.update_layout(
        legend=dict(
            title="Room Type",
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color="black"
            ),
            borderwidth=2,
            bordercolor="black",
            bgcolor="white"
        )
    )

    st.write("The scatter plot below shows the relationship between price and minimum nights by room type.")

    st.plotly_chart(fig)
