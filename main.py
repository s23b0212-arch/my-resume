import streamlit as st

# ===== Background Color (CSS) =====
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f2f2f2;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
h1, h2, h3 {
    color: DarkBlue;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ===== Resume Content =====
st.title("Charukeshi A/P Thinagaran")
st.image("profile.jpeg", width=180)

# Contact Information
st.header("Contact Information")
st.write("📧 Email: charu.email@example.com")
st.write("📱 Phone: +60 12-345 6789")
st.write("🔗 LinkedIn: linkedin.com/in/charu-thinagaran")
st.write("💻 GitHub: github.com/charukeshi")

# About Me
st.header("About Me")
st.write("I am a fourth-semester undergraduate student at UMK, motivated and adaptable, seeking to expand my skills, gain new knowledge, and grow both personally and academically while embracing challenges beyond the classroom.")

# Education
st.header("Education")
st.write("2023 - Present: Bachelor of Information Technology with Honours, UMK")

# Work Experience
st.header("Work Experience")
st.write("2023: Graphic Designer (Internship), GIC Computer & Internet Centre")

# Skills
st.header("Skills")
st.write("- Teamwork")
st.write("- Creative & Organised")
st.write("- Communication")
st.write("- Microsoft Office (Word, Excel, PowerPoint)")
st.write("- Programming (Java, PHP, HTML, CSS)")
st.write("- Web & Mobile App Development")

# Projects / Achievements
st.header("Projects & Achievements")
st.write("- Final Year Project: E-Attendance System using Arduino with fingerprint sensors")
st.write("- Facilitator, Avira 1.0 Event (2024)")
st.write("- Dean’s List Award (Semester 3)")

# Reference
st.header("Reference")
st.write("Prof. Madya Dr. Nooraini Binti Yusoff - Advisor, Universiti Malaysia Kelantan")
