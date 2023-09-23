import streamlit as st
import pandas as pd
import plotly.express as px

# Function to create the map and display the text
def create_map(df):
    
    # Sort neighborhoods alphabetically
    neighborhoods = sorted(df['neighbourhood'].astype(str).unique())

    # Define the colors for the price bins
    colors = {
        '50-350': 'blue',
        '351-650': 'red',
        '651-950': 'black',
        '951-1250': 'yellow'
    }

    # Sidebar filters with default values
    st.sidebar.title("Filters")
    neighborhood_filter = st.sidebar.selectbox("Select Neighborhood", neighborhoods, index=neighborhoods.index('Kensington'))
    price_bin_filter = st.sidebar.selectbox("Select Price Bin", list(colors.keys()), index=list(colors.keys()).index('50-350'))
    review_rate_filter = st.sidebar.multiselect("Select Review Rate", list(range(1, 6)), default=[5])

    # Filter the data based on selected filters
    filtered_data = df[
        (df['neighbourhood'] == neighborhood_filter) &
        (df['price_bin'] == price_bin_filter) &
        (df['review rate number'].isin(review_rate_filter))
    ]

    # Create the scatter_mapbox plot
    fig = px.scatter_mapbox(filtered_data, lat="lat", lon="long", color="price_bin",
                            color_discrete_map=colors, zoom=8.5)

    fig.update_layout(
        mapbox_style="open-street-map", showlegend=False
    )

    # Display the map
    st.plotly_chart(fig)

    # Create and display the well-formatted text
    selected_neighborhood = neighborhood_filter
    selected_rates = review_rate_filter
    price_range = price_bin_filter

    text = f"In the {selected_neighborhood} neighborhood, for the price range of {price_range} there are:\n"

    for rate in selected_rates:
        count = len(filtered_data[filtered_data['review rate number'] == rate])
        text += f"{count} location{'s' if count > 1 else ''} for the rate of {rate}\n"

    st.text(text)

