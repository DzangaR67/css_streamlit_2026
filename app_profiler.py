import streamlit as st




# --- Page Config ---
st.set_page_config(page_title="Researcher Profile", page_icon="🔬", layout="centered")

# --- Custom CSS for Themed Background ---
profile_theme_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f0f4f8 0%, #d9e4ec 50%, #fdfdfd 100%);
    background-attachment: fixed;
    color: #1a1a1a;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: #ffffff;
}
h1, h2, h3 {
    color: #2c3e50;
}
</style>
"""
st.markdown(profile_theme_bg, unsafe_allow_html=True)

# --- Header ---
st.title("🔬 Researcher Profile")

st.header("Researcher Overview")
# --- Profile Card ---
st.markdown("""
### Dzanga Rambuda | Data Scientist
""")

field = "Information and Communications Technology"
st.markdown("""
**Education:** Bachelor of ICT (Honours, Distinction) 

**Currently:** Master’s in Explainable AI & Public Health
""")
institution = "University of Mpumalanga"

# Display basic profile information

st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


st.image(
    "https://github.com/DzangaR67/css_streamlit_2026/blob/main/brainstorm.png?raw=true",
    caption="IT Brainstorm",
    width=500
)


# --- Introduction Paragraph ---
st.subheader("About me")
st.markdown("""
I am Dzanga Rambuda, an IT Graduate from the University of Mpumalanga and a researcher passionate about the intersection of artificial intelligence and public health and risk communication.
My research explores this intersection, 
with a focus on developing transparent, explainable systems that empower communities to make safer choices.  
I am currently building AI-driven ingredient safety tools, which assess cosmetic and consumer product risks through predictive analytics and curated databases.  
By combining machine learning, natural language processing, and scalable infrastructure design, my work aims to humanize technical research, transforming complex data into clear, actionable insights that support ethical decision-making, health advocacy, and sustainable innovation.
""")


# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["📖 Research Focus", "🛠 Skills", "🌍 Vision"])

with tab1:
    st.subheader("Research Focus")
    st.markdown("""
    - AI for Public Health: Developing explainable AI systems to assess cosmetic ingredient safety and monitor health risks. 
    - Infrastructure & Data Science: Building scalable, transparent tools for community health, sanitation, and ethical technology adoption.  
    - Interdisciplinary Impact: Bridging technical research with everyday consumer empowerment and advocacy. 
    """)

with tab2:
    st.subheader("Skills & Expertise")
    st.markdown("""
    - Python
    -Typescript, React
    - SQl
    - Data Analytics
    - Predictive analytics,
    - Machine learning, NLP  
    - Database curation & risk-ranking engines  
    - Academic writing & science communication  
    """)

with tab3:
    st.subheader("Vision")
    st.info("Humanizing technical research, using  AI to introduce transparency , help communities make informed choices, and advancing AI for public health.")




# Add a contact section
st.header("Contact Information")
email = "dzangarambuda839@gmail.com"
st.write(f"You can reach me at {email}.")