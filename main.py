import streamlit as st

# ===== Title with Profile Picture =====
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpeg", width=150)  # <-- replace with your photo file

with col2:
    st.title("Charu Thinagaran")
    st.write("📍 Kelantan, Malaysia")
    st.write("💼 Undergraduate Student | Aspiring Software Engineer")

# ===== Contact Information =====
st.header("📞 Contact Information")
st.markdown("""
- **Email:** charu.email@example.com  
- **Phone:** +60 12-345 6789  
- **LinkedIn:** [linkedin.com/in/charu-thinagaran](https://linkedin.com/in/charu-thinagaran)  
- **GitHub:** [github.com/charukeshi](https://github.com/charukeshi)
""")

# ===== Education =====
st.header("🎓 Education")
st.markdown("""
**Bachelor of Information Technology** – Universiti Malaysia Kelantan (2022 – Present)  
- Major: Software Engineering  
- CGPA: 3.6/4.0
""")

# ===== Work Experience =====
st.header("💼 Work Experience")
st.subheader("Intern – ABC Tech Solutions (2024)")
st.markdown("""
- Assisted in developing a dashboard using Streamlit  
- Improved data visualization workflows  
- Documented processes and supported user training
""")

# ===== Skills =====
st.header("🛠 Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Python  
    - Java  
    - SQL  
    - Streamlit
    """)

with col2:
    st.markdown("""
    - HTML, CSS, JavaScript  
    - GitHub  
    - Excel, PowerPoint  
    - Communication & Teamwork
    """)

# ===== Projects & Achievements =====
st.header("🚀 Projects & Achievements")
st.subheader("Portfolio Website")
st.write("Created a personal resume website using Streamlit.")

st.subheader("Gold Award – Innovation Competition")
st.write("Won Gold for innovative project design at university-level competition.")

st.subheader("National Youth Day – Multimedia Committee")
st.write("Contributed as Multimedia Committee member for district-level event at UMK.")

# ===== Extra Section =====
st.header("✨ Co-Curricular Activities")
st.markdown("""
- Netball Club Member (2023 – Present)  
- Active participant in seminars and volunteer programs  
""")
