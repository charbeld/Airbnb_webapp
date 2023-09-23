import streamlit as st
import pandas as pd

from Tabs.Price_room_comb import Price_room_comb 
from Tabs.Price_Min_Nights_Room_Type import Price_Min_Nights_Room_Type 
from Tabs.Map import create_map

airbnb_data = pd.read_csv("Airbnb.csv")

# Create a Streamlit app
def main():
    user_menu = st.sidebar.radio(
        'Select an Option',
        ('Home Page', 'Property Distribution', 'Price Range by Room Type', 'Price vs Min Nights & Room Type')
    )

    if user_menu == "Home Page":
        # Display title, description, and photo for the Home Page
        st.title("Welcome to Airbnb NY Data Analysis")
        st.write("This is the home page of our Airbnb New York Analysis app. "
                 "Explore different tabs to drill through different elements for Analysis")
        st.image("Media/New York Animated.gif", use_column_width=True)


    elif user_menu == "Property Distribution":
        # Title for the "Property Distribution" tab
        st.title("Property Distribution Analysis")
        
        # Calling the function of the Property Distribution option
        create_map(airbnb_data)
        
    elif user_menu == "Price Range by Room Type":
        # Title for the "Composition of Price Range by Room Type" tab
        st.title("Composition of Price Range by Room Type")
        
        # Calling the function of the Composition of Price Range by Room Type option
        Price_room_comb(airbnb_data)
        
    elif user_menu == "Price vs Min Nights & Room Type":
        # Title for the "Price vs Min Nights & Room Type" tab
        st.title("Price vs Minimum Nights by Room Type")

        # Calling the function of the Price vs Min Nights & Room Type option
        Price_Min_Nights_Room_Type(airbnb_data)


if __name__ == "__main__":
    main()
