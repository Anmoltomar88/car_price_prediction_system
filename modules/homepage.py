import streamlit as st

def show():
    st.markdown(
        """
        <style>
        
        .header {
            font-size: 24px;
            color: #4CAF50;
            margin-top: 20px;
            z-index: 2;  /* Ensures the header is above the image */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # # Add the image using the relative path
    # st.markdown(
    #     """
    #     <div class="background-container">
    #         <img src="assets/car_image.jpg" class="background-image">
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )    

    st.title("🚗 Welcome to the Car Price Prediction App")

    # Stylish header
    st.markdown(
        '<div class="header">Predict the price of your car with ease!</div>', 
        unsafe_allow_html=True
    )

    # Add some content with icons
    st.markdown(
        """
        ### Features:
        - 🛠 **User-Friendly Interface**: Easy to navigate and use.
        - 📈 **Accurate Predictions**: Based on advanced machine learning models.
        - 📞 **Contact Us**: We're here to help you with any questions.

        **Get started now by selecting the options from the sidebar!**
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="footer">
            <p>© 2024 Car Price Prediction App. All rights reserved. Developed by TheDots.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
