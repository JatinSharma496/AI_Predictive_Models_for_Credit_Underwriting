import streamlit as st
from styles import apply_styles
def show():
    apply_styles()
    st.title("👨‍💻 About Me")
    
    st.markdown("""
    ## Hi there! I'm **Jatin Sharma**, a AI & Machine Learning Enthusiast 🚀
    
    ### 🌟 Key Areas of Interest:
    - Artificial Intelligence (AI)
    - Machine Learning (ML)
    
    ### 📬 Let's Connect:
    - **LinkedIn**: [Jatin Sharma](https://linkedin.com/in/jatin-sharma496)
    - **GitHub**: [JatinSharma496](https://github.com/JatinSharma496)
    - **Email**: [heyiamjatin001@gmail.com](mailto:heyiamjatin001@gmail.com)

    Feel free to reach out for collaborations, learning, or discussions on anything AI & ML-related!
    """)

    st.markdown("___")
    st.markdown("I'm always excited to connect with like-minded individuals and share knowledge!")
