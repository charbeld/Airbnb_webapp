import streamlit as st
import pandas as pd
import plotly.express as px

def Price_room_comb(df):

    # Add text description
    st.write("The chart below the number of rooms in each price range and room type combination.")
    
    # Pivot the table and count the occurrences of each room type
    pivot_df = df.pivot_table(index='price_bin', columns='room type', values='lat', aggfunc='count').fillna(0).reset_index()

    # Melt the DataFrame to create a suitable format for the stacked bar chart
    melted_df = pd.melt(pivot_df, id_vars='price_bin', value_vars=pivot_df.columns[1:], var_name='room type', value_name='Count')

    # Define the order of bins for the x-axis
    bin_order = ['50-350', '351-650', '651-950', '951-1250']

    # Create the figure with a white background
    fig = px.bar(melted_df, x='price_bin', y='Count', color='room type',
                 labels={'room type': 'Room Type Count'}, template='plotly_white')

    fig.update_layout(barmode='stack')

    # Remove gridlines
    fig.update_xaxes(showgrid=False, title_text="Price Range")
    fig.update_yaxes(showgrid=False, title_text="Room Type Count")

    # Set the order of bins on the x-axis
    bin_order = ['50-350', '351-650', '651-950', '951-1250']
    fig.update_xaxes(categoryorder='array', categoryarray=bin_order)

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

    # Add text description
    st.plotly_chart(fig)


