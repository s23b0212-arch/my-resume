import streamlit as st

# Title
st.title("Your Name's Resume")

# Contact Information
st.header("Contact Information")
st.markdown("""
- **Email:** your.email@example.com  
- **Phone:** (123) 456-7890  
- **LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
""")

# Education
st.header("Education")
st.write("BSc in Computer Science, University Name, 2025")

# Work Experience
st.header("Work Experience")
st.subheader("Job Title – Company Name (2023–2024)")
st.markdown("""
- Developed and maintained web applications  
- Improved data processing efficiency by 20%  
- Collaborated with cross-functional teams
""")

# Skills
st.header("Skills")
st.markdown("""
- Python, Streamlit, SQL  
- Data Visualization (Matplotlib, Plotly)  
- Web Development (HTML, CSS, JavaScript)
""")

# Projects
st.header("Projects")
st.subheader("Personal Portfolio Website")
st.write("Built a portfolio website using Streamlit to showcase projects and skills.")

