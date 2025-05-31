import streamlit as st
from base64 import b64encode
import os

# Page Configuration
st.set_page_config(page_title="Abdullah Afzaal's Portfolio", page_icon="📄")

def web_portfolio():
    # Title
    st.markdown("""
    <div style='text-align: center;'>
        <h1>Hello! My name is <span style='color: #4CAF50;'>Abdullah Afzaal</span> 👋</h1>
    </div>
    """, unsafe_allow_html=True)

    # Profile Image
    if os.path.exists("abd.png"):
        with open("abd.png", "rb") as img_file:
            img = "data:image/png;base64," + b64encode(img_file.read()).decode()
        st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="{img}" style="width: 200px; height: 200px; border-radius: 50%;">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Profile image (dp.png) not found.")

    st.write("##")

    # About Me
    st.subheader("About Me")
    st.markdown("""
    I am **Abdullah Afzaal**, a passionate and motivated Python developer with a strong interest in **Machine Learning**, **Deep Learning**, and **NLP**.

    ### 🚀 My Projects:
    - **Churn Modeling**: Built a predictive model to identify customer churn.
    - **Streamlit App**: Created interactive data apps using Streamlit.
    - **ANN for NLP**: Used artificial neural networks to perform text classification.

    ### 🎯 Skills:
    Python, Machine Learning, Streamlit, NLP, Deep Learning

    ### 📫 Contact:
    - Email: **abdullahafzaal1043@gmail.com**
    - Location: Pakistan
    """)

    st.write("##")

    # Social Links
    social_icons_data = { "GitHub": ["https://github.com/Abdullahafzaal-1", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    "Facebook": ["https://www.facebook.com/profile.php?id=61570949032152", "https://cdn-icons-png.flaticon.com/128/733/733547.png"],
    "TikTok": ["https://www.tiktok.com/@abdullah.afzaal509", "https://cdn-icons-png.flaticon.com/128/3046/3046122.png"],
    "YouTube": ["https://www.youtube.com/@MuhammadAbdullah-m8m7e", "https://cdn-icons-png.flaticon.com/128/1384/1384060.png"]
}

    social_icons_html = [
        f"<a href='{url}' target='_blank' style='margin-right: 15px;'>"
        f"<img src='{icon}' alt='{name}' style='width: 30px; height: 30px;'></a>"
        for name, (url, icon) in social_icons_data.items()
    ]

    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin-top: 10px;">
        {''.join(social_icons_html)}
    </div>
    """, unsafe_allow_html=True)

    st.write("##")

    # PDF Download
    if os.path.exists("Abdullah_Afzaal_Portfolio.pdf"):
        with open("Abdullah_Afzaal_Portfolio.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download My Portfolio",
            data=pdf_bytes,
            file_name="Abdullah_Afzaal_Portfolio.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Portfolio PDF not found.")

    st.write("##")

    # Footer
    st.markdown("""
    <div style='text-align: center;'>🌟 Thank you for visiting! Stay connected. 🌟</div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
