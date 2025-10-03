import streamlit as st

# ===== Resume Page =====
# Centered Name
st.markdown(
    """
    <h1 style='text-align: center; color: black;'>
        CHARUKESHI A/P THINAGARAN
    </h1>
    """,
    unsafe_allow_html=True
)

# Centered profile image
st.markdown(
    """
    <div style="text-align: center;">
        <img src="profile.jpeg" width="180">
    </div>
    """,
    unsafe_allow_html=True
)

# Contact Information
st.markdown("### 📞 Contact Information")
st.write(" Email: charukeshithinagaran.email@gmail.com")
st.write(" Phone: +60 16-345 6789")
st.write(" LinkedIn: linkedin.com/in/charu-thinagaran")
st.write(" GitHub: github.com/charukeshi")

# About Me
st.markdown("### 👩 About Me")
st.write("I am a fourth-semester undergraduate student at UMK, motivated and adaptable, seeking to expand my skills, gain new knowledge, and grow both personally and academically while embracing challenges beyond the classroom.")

# Education
st.markdown("### 🎓 Education")
st.write("2023 - Present: Bachelor of Information Technology with Honours, UMK")

# Work Experience
st.markdown("### 💼 Work Experience")
st.write("2023: Graphic Designer (Internship), Computer Centre")

# Skills
st.markdown("### 🛠 Skills")
st.write("- Teamwork")
st.write("- Creative & Organised")
st.write("- Communication")
st.write("- Microsoft Office (Word, Excel, PowerPoint)")
st.write("- Programming (Java, PHP, HTML, CSS)")
st.write("- Web & Mobile App Development")

# Projects / Achievements
st.markdown("### 🚀 Projects & Achievements")
st.write("- Facilitator, Avira 1.0 Event (2024)")
st.write("- Dean’s List Award (Semester 3)")

# Reference
st.markdown("### 📎 Reference")
st.write("Prof. Madya Dr. Nooraini Binti Yusoff - Advisor, Universiti Malaysia Kelantan")
