import streamlit as st

# ==========================
# HEADER (Photo + Name)
# ==========================
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpeg", width=180)  # <-- Make sure your photo file is named profile.jpeg

with col2:
    st.markdown("<h1 style='margin-bottom:0;'>CHARUKESHI A/P THINAGARAN</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: gray; margin-top:0;'>IT Student</h3>", unsafe_allow_html=True)
    st.write("📍 Kelantan, Malaysia")
    st.write("📧 charu.email@example.com")
    st.write("📞 +60 12-345 6789")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/charu-thinagaran) | [GitHub](https://github.com/charukeshi)")

st.markdown("---")

# ==========================
# ABOUT ME
# ==========================
st.header("🙋 About Me")
st.write("""
I am a fourth-semester undergraduate student at UMK, motivated and adaptable, seeking to expand my skills, gain new knowledge, and grow both personally and academically while embracing challenges beyond the classroom.
""")

st.markdown("""
- **Date of Birth:** 29 April 2003  
- **Gender:** Female  
- **Race:** Indian  
- **Religion:** Hindu  
- **Nationality:** Malaysian  
- **Email:** charu.email@example.com  
- **Phone:** +60 12-345 6789  
""")

# ==========================
# EDUCATION
# ==========================
st.header("🎓 Education")
st.markdown("""
- **2023 - Present**: Bachelor of Information Technology with Honours (UMK) – CGPA: 3.83  
- **2022**: Diploma Vokasional Malaysia, Database Management System – Certified with DKM, SKM, Level 4  
- **2021**: Malaysian Certification Skills Application Development – Certified with Level 3  
- **2021**: Diploma in Database Management System, Technology & Web Application – CGPA: 3.45
""")

# ==========================
# WORK EXPERIENCE
# ==========================
st.header("💼 Work Experience")
st.markdown("""
- **2023**: Graphic Designer (Internship) – GIC Computer & Internet Centre
""")

# ==========================
# OUTSTANDING ACHIEVEMENTS
# ==========================
st.header("🏆 Outstanding Achievements")
st.markdown("""
- 2025: Netball Club Member  
- 2024: Facilitator, Avira 1.0 | Assisted in event coordination & participant guidance  
- 2024: Exco, Netball Club (Entrepreneurship) | Contributed to club management & event planning  
- 2023: Final Year Project | Developed an E-Attendance System using Arduino with fingerprint sensors  
""")

# ==========================
# HONORS & AWARDS
# ==========================
st.header("🎖 Honors and Awards")
st.markdown("""
- Dean’s List Award (Semester 3) – Bachelor of IT  
- District Level Netball Athlete  
- Gold Award – Final Year Project & Innovation Poster Competition (2024)  
""")

# ==========================
# CO-CURRICULAR
# ==========================
st.header("🤝 Co-Curricular Achievements")
st.markdown("""
- 2024: Competed in Kejohanan Bola Jaring Terbuka UMK  
- 2024: Multimedia Committee Member for District-Level National Youth Day Event @ UMK  
- 2023: Podcast Seminar Participant  
- 2022: Outstanding Student Award (Competition KVSP)  
- 2022: Participated in Bengkel Pembudayaan Inovasi  
""")

# ==========================
# PERSONAL SKILLS
# ==========================
st.header("🧩 Personal Skills")
st.markdown("""
- Teamwork  
- Creative  
- Organised  
- Communication  
""")

# ==========================
# CORE STRENGTHS
# ==========================
st.header("💡 Core Strengths")
st.markdown("""
- Computer Software Applications (Word, Excel, PowerPoint)  
- Web Design & Development  
- Programming (Java, PHP, HTML, CSS)  
- Mobile App Development  
- Software Testing & Quality Assurance  
- Project Management & Leadership  
""")

# ==========================
# LANGUAGES
# ==========================
st.header("🌐 Languages")
st.markdown("""
- English – Expert  
- Malay – Expert  
- Tamil – Expert  
- Mandarin – Beginner  
- French – Beginner  
""")

# ==========================
# REFERENCE
# ==========================
st.header("📎 Reference")
st.markdown("""
**Prof. Madya Dr. Nooraini Binti Yusoff**  
Advisor – Universiti Malaysia Kelantan  
""")

# ==========================
# FOOTER LINE
# ==========================
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 Charukeshi A/P Thinagaran | Streamlit Resume</p>", unsafe_allow_html=True)
