import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="MD ATICK HASSAN | Data And Research Analyst ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# THEME — Deep Teal + Coral (instead of the original black theme)
# ----------------------------------------------------------------------------
PRIMARY_BG = "#0B3D3A"      # deep teal
SECONDARY_BG = "#0F4C4A"    # slightly lighter teal for cards
ACCENT = "#FF6B4A"          # coral accent
ACCENT_SOFT = "#FFB199"     # soft coral for tags
TEXT_LIGHT = "#F4F1EC"      # warm off-white text
TEXT_MUTED = "#B9D6D2"      # muted teal-grey text

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {PRIMARY_BG};
        color: {TEXT_LIGHT};
    }}
    #MainMenu, footer, header {{visibility: hidden;}}

    section.main > div {{
        padding-top: 1.5rem;
        max-width: 1100px;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT_LIGHT} !important;
        font-family: 'Helvetica Neue', sans-serif;
    }}
    p, li, span, div {{
        font-family: 'Helvetica Neue', sans-serif;
    }}

    .nav-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 0 1.5rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 2rem;
    }}
    .nav-logo {{
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: {ACCENT} !important;
    }}
    .nav-links a {{
        color: {TEXT_MUTED};
        text-decoration: none;
        margin-left: 1.5rem;
        font-size: 0.9rem;
        font-weight: 500;
    }}
    .nav-links a:hover {{
        color: {ACCENT};
    }}

    .hero-title {{
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 0.3rem;
    }}
    .hero-accent {{
        color: {ACCENT};
    }}
    .hero-sub {{
        color: {TEXT_MUTED};
        font-size: 1.15rem;
        max-width: 640px;
        margin-top: 1rem;
        margin-bottom: 2rem;
    }}

    .badge {{
        display: inline-block;
        background: rgba(255,107,74,0.15);
        color: {ACCENT};
        border: 1px solid {ACCENT};
        border-radius: 999px;
        padding: 0.2rem 0.8rem;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }}

    .card {{
        background-color: {SECONDARY_BG};
        border-radius: 14px;
        padding: 1.6rem;
        margin-bottom: 1.2rem;
        border: 1px solid rgba(255,255,255,0.06);
        transition: transform 0.15s ease;
    }}
    .card:hover {{
        border: 1px solid {ACCENT};
    }}

    .tag {{
        display: inline-block;
        background: rgba(244,241,236,0.08);
        color: {TEXT_MUTED};
        border-radius: 6px;
        padding: 0.15rem 0.6rem;
        font-size: 0.75rem;
        margin-right: 0.4rem;
        margin-top: 0.5rem;
    }}

    .category-label {{
        color: {ACCENT};
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .section-heading {{
        font-size: 2rem;
        font-weight: 800;
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid {ACCENT};
        padding-left: 0.8rem;
    }}

    .skill-pill {{
        display: inline-block;
        background: {SECONDARY_BG};
        color: {TEXT_LIGHT};
        border: 1px solid {ACCENT_SOFT};
        border-radius: 8px;
        padding: 0.4rem 0.9rem;
        margin: 0.25rem;
        font-size: 0.9rem;
        font-weight: 600;
    }}

    .footer {{
        text-align: center;
        color: {TEXT_MUTED};
        padding: 2.5rem 0 1rem 0;
        border-top: 1px solid rgba(255,255,255,0.1);
        margin-top: 3rem;
        font-size: 0.85rem;
    }}

    div.stButton > button {{
        background-color: {ACCENT};
        color: {PRIMARY_BG};
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.4rem;
    }}
    div.stButton > button:hover {{
        background-color: {ACCENT_SOFT};
        color: {PRIMARY_BG};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# NAV BAR
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="nav-bar">
        <div class="nav-logo">ATICK.</div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#expertise">Expertise</a>
            <a href="#work">Work</a>
            <a href="#booking">Book a Call</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown('<div class="badge">UPWORK DATA & RESEARCH ANALYST</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-title">MD ATICK HASSAN<br><span class="hero-accent">Data & Research Analyst</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="hero-sub">
    I help organizations and individuals extract powerful predictive insights
    from complex datasets. Data & Research Analyst on Upwork with 150+
    completed projects globally.
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.link_button("Book Consultation", "https://meet.google.com/cex-wfed-meo")
with col2:
    st.link_button("Hire Me on Fiverr", "https://www.fiverr.com/atick_hassan/")
    st.link_button("Hire Me on Upwork", "https://www.upwork.com/freelancers/~01f546868f99a434e3")

# ----------------------------------------------------------------------------
# EXPERTISE / ENGINE ROOM
# ----------------------------------------------------------------------------
st.markdown('<div id="expertise"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Expertise</div>', unsafe_allow_html=True)
st.markdown(
    f"""
    <p style="color:{TEXT_MUTED}; max-width:800px; font-size:1.02rem;">
    Hi there!</br>
My goal is to provide solutions that meet or exceed my clients' expectations.</br>

Do you need accurate insights from your survey or research data to make informed decisions 
using statistical data analysis or data science projects? I help researchers and organizations 
turn complex datasets into rigorous findings, reproducible workflows, and stakeholder-ready reports.

I am a Data and Research Analyst with 3+ years of experience and 1,000+ completed projects.
My work spans data cleaning, exploratory analysis, hypothesis testing, regression, 
forecasting, machine learning, and data visualization.
I usually do most of my work in R, though I also used • Python • SQL • Power BI • Excel • R (RStudio) • SPSS • JASP • Jamovi in the past.

📑 CORE EXPERTISE BUT NOT LIMITED TO! </br>
👉Data cleaning/preprocessing ( messy or Unstructured data ) to conduct the research and get accurate result.</br>
👉 Data Analysis, Large Survey Data Analytics and Data Visualization for business and research.</br>
👉Descriptive Statistics(Mean, median, range, IQR, frequency, percentage)</br>
👉Bi-variate analyses such as t-tests, correlations, chi-square tests and non-parametric tests for normal and non-normal data.</br>
👉 Multivariate analyses such as ANOVA, MANOVA, PCA and factoring analysis, regression analysis.</br>
👉Correlation and Regression Analysis: To explore relationships and enable predictive insights.</br>
👉Dimensionality Reduction: Feature Extraction & Selection.</br>
👉Business Analysis.</br>
👉Time Series Analysis: To see the trends and patterns for the business.</br>
👉Clustering(k-means, DB-scan and Hirearical Clustering)</br>
👉Machine Learning.</br>

What you receive:</br>
• A clear analysis plan aligned with your question</br>
• Clean, documented, reproducible code</br>
• Publication- or decision-ready tables and visualizations</br>
• Detailed interpretation of results</br>
• Report writing of the study, results, and interpretation</br>


I work carefully, communicate clearly, and can support a project from initial scoping through final reporting. Send your research question, data format, and deadline, and I’ll recommend the best approach.</br>
Looking forward to working with you soon,
    </p>
    """,
    unsafe_allow_html=True,
)

edu_col, skill_col = st.columns(2)

with edu_col:
    st.markdown(
        """
        <div class="card">
            <div class="category-label">Academic Foundation</div>
            <h4>BBA In Port Management & Loogistics</h4>
            <p>Bangladesh Maritime University</p>
            <h4>Data Exploration And Research</h4>
            <p>Data Solution 360</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with skill_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="category-label">Core Languages</div>', unsafe_allow_html=True)
    st.markdown(
        "".join(f'<span class="skill-pill">{s}</span>' for s in ["R", "Python", "SQL"]),
        unsafe_allow_html=True,
    )
    st.markdown('<br><br><div class="category-label">Modeling &amp; Algorithms</div>', unsafe_allow_html=True)
    st.markdown(
        "".join(
            f'<span class="skill-pill">{s}</span>'
            for s in [
                "Machine Learning",
                "Structural Equation Modeling",
                "Regression Models",
                "Time Series Forecasting",
                "Classification & Clustering",
                "Hypothesis Testing",
                "Statistical Anaalysis"
            ]
        ),
        unsafe_allow_html=True,
    )
    st.markdown('<br><br><div class="category-label">Tools &amp; Environments</div>', unsafe_allow_html=True)
    st.markdown(
        "".join(
            f'<span class="skill-pill">{s}</span>'
            for s in ["SPSS / R / Stata", "Python", "Power BI", "R Markdown","Excel", "JASP", "Jamovi","Postgresql"]
        ),
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PROJECTS / WORK
# ----------------------------------------------------------------------------
st.markdown('<div id="work"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Some of Deployed Solutions</div>', unsafe_allow_html=True)

projects = [
    {
        "category": "FinTech / Predictive",
        "title": "Customer Churn Analysis & Prediction",
        "desc":"Customer churn directly erodes recurring revenue, so identifying which customers are at risk — and "
        "why gives a business a concrete lever to act on. This project analyzes a telecom customer dataset end-to-end:"
        "cleaning the data, exploring churn patterns visually, statistically testing whether contract type drives churn,and building a predictive model to flag at-risk customers before they leave",
        "tags": ["Data Visualization", "R Markdown", "Financial Analytics"],
        "image": "images/rfm_analysis.png",
        "link": "https://github.com/mdatickhassan/",
    },
    {
        "category": "Business Intelligence / SQL",
        "title": "RFM Customer Segmentation & Sales Analysis",
        "desc": (
            "Built an end-to-end SQL Server pipeline: imported a raw sales flat "
            "file into a PortfolioProjects database, profiled every column with "
            "DISTINCT checks, then aggregated revenue by product line, year, "
            "month, and deal size. Applied RFM (Recency, Frequency, Monetary) "
            "logic with DATEDIFF() to rank customers by value — Euro Shopping "
            "Channel came out on top with the highest spend and order frequency, "
            "and Classic Cars was the strongest product line at roughly $3.9M "
            "in revenue."
        ),
        "tags": ["SQL", "RFM Analysis", "Customer Segmentation"],
        "image": "images/rfm_analysis.png",
        "link": "https://github.com/mdatickhassan/",
    },
    {
        "category": "Applied Statistics / Predictive Modeling",
        "title": "Predicting Speaker Identity from Speech Prosody",
        "desc": (
            "Built a binomial logistic regression model in SPSS to classify "
            "which host (John Oliver vs. Trevor Noah) was speaking, using two "
            "prosodic features — pitch level and pitch variation. The model "
            "reached 62.4% overall classification accuracy, correctly "
            "identifying John Oliver in 92.3% of cases. Both predictors were "
            "statistically significant (p < .001 and p = .001), yielding the "
            "equation Logit(p) = -1.756 + 0.009·PitchLevel − 1.475·PitchVariation, "
            "and odds-ratio interpretation of each coefficient."
        ),
        "tags": ["SPSS", "Logistic Regression", "Speech Analytics"],
        "image": "images/logistic_regression.png",
        "link": "https://github.com/mdatickhassan/",
    },
    {
        "category": "Predictive Analytics / R",
        "title": "Customer Churn Analysis & Prediction",
        "desc": (
            "Customer churn directly erodes recurring revenue, so identifying "
            "which customers are at risk — and why — gives a business a "
            "concrete lever to act on. This project analyzes a telecom "
            "customer dataset end-to-end: cleaning the data, exploring churn "
            "patterns visually, statistically testing whether contract type "
            "drives churn, and building a predictive model to flag at-risk "
            "customers before they leave."
        ),
        "tags": ["R", "R Markdown", "Statistical Testing", "Churn Modeling"],
        "image": "images/churn_analysis.png",
        "link": "https://github.com/mdatickhassan/",
    },
    {
        "category": "Business Intelligence / Power BI",
        "title": "Healthcare Admissions & Billing Dashboard",
        "desc": (
            "Designed an interactive Power BI dashboard covering 55,500 "
            "admitted patients across multiple hospitals. Surfaces KPIs like "
            "admission YoY, average billing amount ($25.54K), and total "
            "billing (over $1.4B), with slicers for year, gender, and "
            "condition (arthritis, asthma, cancer, diabetes, hypertension). "
            "Includes a length-of-stay breakdown and a hospital-by-condition "
            "matrix so stakeholders can drill from a top-level KPI straight "
            "down to a specific hospital's patient mix."
        ),
        "tags": ["Power BI", "Dashboarding", "Healthcare Analytics", "DAX"],
        "image": "images/healthcare_dashboard.png",
        "link": "https://github.com/mdatickhassan/",
    },
]


proj_cols = st.columns(2)
for i, proj in enumerate(projects):
    with proj_cols[i % 2]:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in proj["tags"])
        st.markdown(
            f"""
            <div class="card">
                <div class="category-label">{proj['category']}</div>
                <h3>{proj['title']}</h3>
                <p style="color:{TEXT_MUTED};">{proj['desc']}</p>
                {tags_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------------------------
# BOOKING
# ----------------------------------------------------------------------------
st.markdown('<div id="booking"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Let\'s Talk</div>', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="card">
        <h3>Choose a time that works for you.</h3>
        <p style="color:{TEXT_MUTED};">
        Book a one-on-one appointment to discuss your data, research, or
        analytics project and the clearest path forward.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("booking_form"):
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
    with b_col2:
        date = st.date_input("Preferred Date")
        topic = st.selectbox(
            "Project Type",
            ["Predictive Modeling", "Data Visualization", "Statistical Analysis","Classification","Other"],
        )
    message = st.text_area("Tell me about your project")
    submitted = st.form_submit_button("Request a Slot")
    if submitted:
        st.success(f"Thanks {name or 'there'}! Your request for {date} has been noted.")

# ----------------------------------------------------------------------------
# CONTACT
# ----------------------------------------------------------------------------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Let\'s Solve Problems With Data.</div>', unsafe_allow_html=True)

st.markdown(
    f"""
    <p style="color:{TEXT_MUTED}; max-width:800px; font-size:1.02rem;">
    Every dataset holds the answer to a complex challenge. Whether you need to
    uncover hidden trends, identify operational bottlenecks, or build predictive
    models for strategic growth, I am ready to transform your raw data into
    actionable solutions.
    </p>
    """,
    unsafe_allow_html=True,
)

st.link_button("Send an Email", "mailto:mdatickhassansustian72@gmail.com")

link_cols = st.columns(4)
links = [
    ("LinkedIn", "https://www.linkedin.com/in/md-atick-hassan/"),
    ("Fiverr", "https://www.fiverr.com/s/gD7z2oA"),
    ("Upwork", "https://www.upwork.com/freelancers/~01f546868f99a434e3?p=2077839586975793152"),
    ("YouTube", "https://www.youtube.com/@MDAtickhassan72"),
    ("Facebook", "https://www.facebook.com/crushking.atick"),
]
for col, (label, url) in zip(link_cols, links):
    with col:
        st.markdown(f'<a href="{url}" style="color:{ACCENT}; font-weight:600;">{label}</a>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown(
    '<div class="footer">© MD Atick Hassan. All rights reserved.',
    unsafe_allow_html=True,
)
