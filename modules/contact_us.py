import streamlit as st

def show():
    st.title("✉️ Contact Us")
    st.write("We'd love to hear from you! Please fill out the form below:")

    # Contact Information
    st.markdown("""
    <style>
    .contact-info {
        font-size: 20px;
        margin-bottom: 10px;
    }
    .form-field {
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="contact-info">📧 Email: contact@carprice.com</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info">📞 Phone: +123456789</p>', unsafe_allow_html=True)

    # Form Fields
    name = st.text_input('👤 Your Name', key='name')
    email = st.text_input('📧 Your Email', key='email')
    message = st.text_area('📝 Your Message', key='message')

    if st.button("📬 Send"):
        if name and email and message:
            st.success("✅ Your message has been sent successfully!")
        else:
            st.error("❌ Please fill in all fields.")

