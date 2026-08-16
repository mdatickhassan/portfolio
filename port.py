# import os
# import streamlit as st

# # ============================================================================
# # PAGE CONFIG
# # ============================================================================
# st.set_page_config(
#     page_title="MD ATICK HASSAN | Data And Research Analyst",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ============================================================================
# # ✏️  EDIT-ME ZONE #1 — YOUR BASIC INFO
# # ----------------------------------------------------------------------------
# # Change these values to your own. Nothing else below this block needs to
# # be touched unless you want to restyle the page.
# # ============================================================================
# NAME = "MD ATICK HASSAN"
# NAV_LOGO = "ATICK HASSAN"
# TITLE = "Data & Research Analyst"
# BADGE_TEXT = "UPWORK DATA And RESEARCH ANALYST"
# TAGLINE = (
#     "I help organizations and individuals extract powerful predictive insights "
#     "from complex datasets. Data & Research Analyst on Upwork with 150+ "
#     "completed projects globally."
# )
# EMAIL = "mdatickhassansustian72@gmail.com"
# BOOKING_URL = "https://meet.google.com/cex-wfed-meo"
# FIVERR_URL = "https://www.fiverr.com/atick_hassan/"
# UPWORK_URL = "https://www.upwork.com/freelancers/~01f546868f99a434e3?p=2077839586975793152"

# SOCIAL_LINKS = [
#     ("LinkedIn", "https://www.linkedin.com/in/md-atick-hassan/"),
#     ("Fiverr", "https://www.fiverr.com/atick_hassan/"),
#     ("Upwork", "https://www.upwork.com/freelancers/~01f546868f99a434e3?p=2077839586975793152"),
#     ("YouTube", "https://www.youtube.com/@MDAtickhassan72"),
#     ("Facebook", "https://www.facebook.com/crushking.atick"),
# ]

# ABOUT_HTML = """
# Hi there!<br><br>
# My goal is to provide solutions that meet or exceed my clients' expectations.<br><br>
# Do you need accurate insights from your survey or research data to make informed decisions
# using statistical data analysis or data science projects? I help researchers and organizations
# turn complex datasets into rigorous findings, reproducible workflows, and stakeholder-ready reports.<br><br>
# I am a Data and Research Analyst with 3+ years of experience and 1,000+ completed projects.
# My work spans data cleaning, exploratory analysis, hypothesis testing, regression,
# forecasting, machine learning, and data visualization. I usually do most of my work in R,
# though I also use Python, SQL, Power BI, Excel, SPSS, JASP, and Jamovi.
# """

# CORE_EXPERTISE = [
#     "Data cleaning/preprocessing (messy or unstructured data) to conduct research and get accurate results",
#     "Data Analysis, large survey data analytics and data visualization for business and research",
#     "Descriptive Statistics (mean, median, range, IQR, frequency, percentage)",
#     "Bi-variate analyses: t-tests, correlations, chi-square tests, and non-parametric tests",
#     "Multivariate analyses: ANOVA, MANOVA, PCA, factor analysis, regression analysis",
#     "Correlation and Regression Analysis to explore relationships and enable predictive insights",
#     "Dimensionality Reduction: feature extraction & selection",
#     "Time Series Analysis to identify trends and patterns for business",
#     "Clustering (k-means, DBSCAN, hierarchical clustering)",
#     "Machine Learning",
# ]

# DELIVERABLES = [
#     "A clear analysis plan aligned with your question",
#     "Clean, documented, reproducible code",
#     "Publication- or decision-ready tables and visualizations",
#     "Detailed interpretation of results",
#     "A full report of the study, results, and interpretation",
# ]

# # ============================================================================
# # ✏️  EDIT-ME ZONE #2 — YOUR PROJECTS
# # ----------------------------------------------------------------------------
# # For each project fill in:
# #   "image" -> path to a picture on YOUR computer. Put your screenshots/plots
# #              inside the "images" folder next to this .py file and just
# #              reference the filename, e.g. "images/rfm_analysis.png".
# #              If a file isn't found, a placeholder box is shown instead —
# #              nothing breaks.
# #   "link"  -> URL to the live project, GitHub repo, or PDF write-up.
# #              Leave as "" to hide the button for that project.
# # ============================================================================
# PROJECTS = [
#     {
#         "category": "Business Intelligence / SQL",
#         "title": "RFM Customer Segmentation & Sales Analysis",
#         "desc": (
#             "Built an end-to-end SQL pipeline: imported a raw sales flat file "
#             "into a database, profiled every column with DISTINCT checks, then "
#             "aggregated revenue by product line, year, month, and deal size. "
#             "Applied RFM (Recency, Frequency, Monetary) logic with DATEDIFF() "
#             "to rank customers by value — the top account came out ahead on "
#             "both spend and order frequency, with one product line driving "
#             "roughly $3.9M in revenue."
#         ),
#         "tags": ["SQL", "RFM Analysis", "Customer Segmentation"],
#         "image": "images/rfm_analysis.png",
#         "link": "https://github.com/mdatickhassan/",
#     },
#     {
#         "category": "Applied Statistics / Predictive Modeling",
#         "title": "Predicting Speaker Identity from Speech Prosody",
#         "desc": (
#             "Built a binomial logistic regression model in SPSS to classify "
#             "which of two hosts was speaking, using two prosodic features — "
#             "pitch level and pitch variation. The model reached 62.4% overall "
#             "classification accuracy. Both predictors were statistically "
#             "significant (p < .001 and p = .001), with odds-ratio "
#             "interpretation for each coefficient."
#         ),
#         "tags": ["SPSS", "Logistic Regression", "Speech Analytics"],
#         "image": "images1/log1.png",
#         "link": "https://github.com/mdatickhassan/",
#     },
#     {
#         "category": "Predictive Analytics / R",
#         "title": "Customer Churn Analysis & Prediction",
#         "desc": (
#             "Customer churn directly erodes recurring revenue, so identifying "
#             "which customers are at risk — and why — gives a business a "
#             "concrete lever to act on. This project analyzes a telecom "
#             "customer dataset end-to-end: cleaning the data, exploring churn "
#             "patterns visually, statistically testing whether contract type "
#             "drives churn, and building a predictive model to flag at-risk "
#             "customers before they leave."
#         ),
#         "tags": ["R", "R Markdown", "Statistical Testing", "Churn Modeling"],
#         "image": "images2/churn_dashboard.png",
#         "link": "https://github.com/mdatickhassan/",
#     },
#     {
#         "category": "Business Intelligence / Power BI",
#         "title": "Healthcare Admissions & Billing Dashboard",
#         "desc": (
#             "Designed an interactive Power BI dashboard covering 55,500 "
#             "admitted patients across multiple hospitals. Surfaces KPIs like "
#             "admission YoY, average billing amount, and total billing, with "
#             "slicers for year, gender, and condition (arthritis, asthma, "
#             "cancer, diabetes, hypertension). Includes a length-of-stay "
#             "breakdown and a hospital-by-condition matrix so stakeholders can "
#             "drill from a top-level KPI straight down to a specific "
#             "hospital's patient mix."
#         ),
#         "tags": ["Power BI", "Dashboarding", "Healthcare Analytics", "DAX"],
#         "image": "images3/Healthcare Project.png",
#         "link": "https://github.com/mdatickhassan/",
#     },
# ]

# # ============================================================================
# # THEME — Midnight Indigo + Amber Gold (new palette, distinct from black
# # and from the earlier teal/coral version)
# # ============================================================================
# PRIMARY_BG = "#141127"      # deep indigo-black
# SECONDARY_BG = "#1E1A3C"    # slightly lighter violet-navy for cards
# ACCENT = "#F2B705"          # amber gold accent
# ACCENT_SOFT = "#F7D488"     # soft gold for tags/borders
# TEXT_LIGHT = "#F5F3FF"      # near-white with a violet tint
# TEXT_MUTED = "#B7B2D9"      # muted lavender-grey text

# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-color: {PRIMARY_BG};
#         color: {TEXT_LIGHT};
#     }}
#     #MainMenu, footer, header {{visibility: hidden;}}

#     section.main > div {{
#         padding-top: 1.5rem;
#         max-width: 1100px;
#     }}

#     h1, h2, h3, h4 {{
#         color: {TEXT_LIGHT} !important;
#         font-family: 'Helvetica Neue', sans-serif;
#     }}
#     p, li, span, div {{
#         font-family: 'Helvetica Neue', sans-serif;
#     }}

#     .nav-bar {{
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         padding: 0.5rem 0 1.5rem 0;
#         border-bottom: 1px solid rgba(255,255,255,0.1);
#         margin-bottom: 2rem;
#     }}
#     .nav-logo {{
#         font-size: 1.4rem;
#         font-weight: 800;
#         letter-spacing: 2px;
#         color: {ACCENT} !important;
#     }}
#     .nav-links a {{
#         color: {TEXT_MUTED};
#         text-decoration: none;
#         margin-left: 1.5rem;
#         font-size: 0.9rem;
#         font-weight: 500;
#     }}
#     .nav-links a:hover {{
#         color: {ACCENT};
#     }}

#     .hero-title {{
#         font-size: 3.1rem;
#         font-weight: 800;
#         line-height: 1.1;
#         margin-bottom: 0.3rem;
#     }}
#     .hero-accent {{
#         color: {ACCENT};
#     }}
#     .hero-sub {{
#         color: {TEXT_MUTED};
#         font-size: 1.15rem;
#         max-width: 640px;
#         margin-top: 1rem;
#         margin-bottom: 2rem;
#     }}

#     .badge {{
#         display: inline-block;
#         background: rgba(242,183,5,0.12);
#         color: {ACCENT};
#         border: 1px solid {ACCENT};
#         border-radius: 999px;
#         padding: 0.2rem 0.8rem;
#         font-size: 0.8rem;
#         font-weight: 600;
#         margin-bottom: 1rem;
#     }}

#     .card {{
#         background-color: {SECONDARY_BG};
#         border-radius: 14px;
#         padding: 1.4rem 1.6rem 1.6rem 1.6rem;
#         margin-bottom: 1.2rem;
#         border: 1px solid rgba(255,255,255,0.06);
#     }}
#     .card:hover {{
#         border: 1px solid {ACCENT};
#     }}

#     .img-placeholder {{
#         width: 100%;
#         height: 170px;
#         border-radius: 10px;
#         margin-bottom: 1rem;
#         background: repeating-linear-gradient(
#             45deg,
#             rgba(242,183,5,0.08),
#             rgba(242,183,5,0.08) 10px,
#             rgba(255,255,255,0.03) 10px,
#             rgba(255,255,255,0.03) 20px
#         );
#         border: 1px dashed {ACCENT_SOFT};
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         color: {TEXT_MUTED};
#         font-size: 0.8rem;
#         text-align: center;
#         padding: 0.5rem;
#     }}

#     .tag {{
#         display: inline-block;
#         background: rgba(245,243,255,0.08);
#         color: {TEXT_MUTED};
#         border-radius: 6px;
#         padding: 0.15rem 0.6rem;
#         font-size: 0.75rem;
#         margin-right: 0.4rem;
#         margin-top: 0.5rem;
#     }}

#     .category-label {{
#         color: {ACCENT};
#         font-size: 0.8rem;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#     }}

#     .section-heading {{
#         font-size: 2rem;
#         font-weight: 800;
#         margin-top: 3rem;
#         margin-bottom: 1.5rem;
#         border-left: 4px solid {ACCENT};
#         padding-left: 0.8rem;
#     }}

#     .skill-pill {{
#         display: inline-block;
#         background: {SECONDARY_BG};
#         color: {TEXT_LIGHT};
#         border: 1px solid {ACCENT_SOFT};
#         border-radius: 8px;
#         padding: 0.4rem 0.9rem;
#         margin: 0.25rem;
#         font-size: 0.9rem;
#         font-weight: 600;
#     }}

#     .expertise-list li, .deliverables-list li {{
#         color: {TEXT_MUTED};
#         margin-bottom: 0.4rem;
#         line-height: 1.5;
#     }}

#     .footer {{
#         text-align: center;
#         color: {TEXT_MUTED};
#         padding: 2.5rem 0 1rem 0;
#         border-top: 1px solid rgba(255,255,255,0.1);
#         margin-top: 3rem;
#         font-size: 0.85rem;
#     }}

#     div.stButton > button, div.stLinkButton > a {{
#         background-color: {ACCENT} !important;
#         color: {PRIMARY_BG} !important;
#         font-weight: 700;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5rem 1.2rem;
#     }}
#     div.stButton > button:hover, div.stLinkButton > a:hover {{
#         background-color: {ACCENT_SOFT} !important;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ============================================================================
# # NAV BAR
# # ============================================================================
# st.markdown(
#     f"""
#     <div class="nav-bar">
#         <div class="nav-logo">{NAV_LOGO}</div>
#         <div class="nav-links">
#             <a href="#home">Home</a>
#             <a href="#expertise">Expertise</a>
#             <a href="#work">Work</a>
#             <a href="#booking">Book a Call</a>
#             <a href="#contact">Contact</a>
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # ============================================================================
# # HERO
# # ============================================================================
# st.markdown('<div id="home"></div>', unsafe_allow_html=True)
# st.markdown(f'<div class="badge">{BADGE_TEXT}</div>', unsafe_allow_html=True)
# st.markdown(
#     f'<div class="hero-title">{NAME}<br><span class="hero-accent">{TITLE}</span></div>',
#     unsafe_allow_html=True,
# )
# st.markdown(f'<div class="hero-sub">{TAGLINE}</div>', unsafe_allow_html=True)

# col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
# with col1:
#     st.link_button("Book Consultation", BOOKING_URL)
# with col2:
#     st.link_button("Hire Me on Fiverr", FIVERR_URL)
# with col3:
#     st.link_button("Hire Me on Upwork", UPWORK_URL)

# # ============================================================================
# # EXPERTISE
# # ============================================================================
# st.markdown('<div id="expertise"></div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Expertise</div>', unsafe_allow_html=True)
# st.markdown(
#     f'<p style="color:{TEXT_MUTED}; max-width:800px; font-size:1.02rem;">{ABOUT_HTML}</p>',
#     unsafe_allow_html=True,
# )

# exp_col1, exp_col2 = st.columns(2)
# with exp_col1:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="category-label">Core Expertise</div>', unsafe_allow_html=True)
#     st.markdown(
#         '<ul class="expertise-list">' + "".join(f"<li>{item}</li>" for item in CORE_EXPERTISE) + "</ul>",
#         unsafe_allow_html=True,
#     )
#     st.markdown("</div>", unsafe_allow_html=True)

# with exp_col2:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="category-label">What You Receive</div>', unsafe_allow_html=True)
#     st.markdown(
#         '<ul class="deliverables-list">' + "".join(f"<li>{item}</li>" for item in DELIVERABLES) + "</ul>",
#         unsafe_allow_html=True,
#     )
#     st.markdown("</div>", unsafe_allow_html=True)

# edu_col, skill_col = st.columns(2)

# with edu_col:
#     st.markdown(
#         """
#         <div class="card">
#             <div class="category-label">Academic Foundation</div>
#             <h4>BBA in Port Management &amp; Logistics</h4>
#             <p>Bangladesh Maritime University</p>
#             <h4>Data Exploration &amp; Research</h4>
#             <p>Data Solution 360</p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# with skill_col:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="category-label">Core Languages</div>', unsafe_allow_html=True)
#     st.markdown(
#         "".join(f'<span class="skill-pill">{s}</span>' for s in ["R", "Python", "SQL"]),
#         unsafe_allow_html=True,
#     )
#     st.markdown('<br><br><div class="category-label">Modeling &amp; Algorithms</div>', unsafe_allow_html=True)
#     st.markdown(
#         "".join(
#             f'<span class="skill-pill">{s}</span>'
#             for s in [
#                 "Machine Learning",
#                 "Structural Equation Modeling",
#                 "Regression Models",
#                 "Time Series Forecasting",
#                 "Classification & Clustering",
#                 "Hypothesis Testing",
#                 "Statistical Analysis",
#             ]
#         ),
#         unsafe_allow_html=True,
#     )
#     st.markdown('<br><br><div class="category-label">Tools &amp; Environments</div>', unsafe_allow_html=True)
#     st.markdown(
#         "".join(
#             f'<span class="skill-pill">{s}</span>'
#             for s in ["SPSS", "R", "Stata", "Python", "Power BI", "R Markdown", "Excel", "JASP", "Jamovi", "PostgreSQL"]
#         ),
#         unsafe_allow_html=True,
#     )
#     st.markdown("</div>", unsafe_allow_html=True)

# # ============================================================================
# # PROJECTS / WORK
# # ============================================================================
# st.markdown('<div id="work"></div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Some of Deployed Solutions</div>', unsafe_allow_html=True)

# # Folder that this script lives in, so relative image paths always resolve
# # no matter where you launch `streamlit run` from.
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# def render_project(project: dict) -> None:
#     """Render one project card: local image (or placeholder), text, tags, link."""
#     st.markdown('<div class="card">', unsafe_allow_html=True)

#     img_path = project.get("image", "")
#     resolved_path = img_path if os.path.isabs(img_path) else os.path.join(BASE_DIR, img_path)

#     if img_path and os.path.exists(resolved_path):
#         st.image(resolved_path, use_container_width=True)
#     else:
#         st.markdown(
#             f'<div class="img-placeholder">Drop an image at<br><code>{img_path or "images/your_project.png"}</code></div>',
#             unsafe_allow_html=True,
#         )

#     tags_html = "".join(f'<span class="tag">{t}</span>' for t in project["tags"])
#     st.markdown(
#         f"""
#         <div class="category-label">{project['category']}</div>
#         <h3>{project['title']}</h3>
#         <p style="color:{TEXT_MUTED};">{project['desc']}</p>
#         {tags_html}
#         """,
#         unsafe_allow_html=True,
#     )

#     if project.get("link"):
#         st.link_button("View Project ↗", project["link"])

#     st.markdown("</div>", unsafe_allow_html=True)


# proj_cols = st.columns(2)
# for i, proj in enumerate(PROJECTS):
#     with proj_cols[i % 2]:
#         render_project(proj)

# # ============================================================================
# # BOOKING
# # ============================================================================
# st.markdown('<div id="booking"></div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Let\'s Talk</div>', unsafe_allow_html=True)

# st.markdown(
#     f"""
#     <div class="card">
#         <h3>Choose a time that works for you.</h3>
#         <p style="color:{TEXT_MUTED};">
#         Book a one-on-one appointment to discuss your data, research, or
#         analytics project and the clearest path forward.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# with st.form("booking_form"):
#     b_col1, b_col2 = st.columns(2)
#     with b_col1:
#         name = st.text_input("Your Name")
#         email = st.text_input("Email Address")
#     with b_col2:
#         date = st.date_input("Preferred Date")
#         topic = st.selectbox(
#             "Project Type",
#             ["Predictive Modeling", "Data Visualization", "Statistical Analysis", "Classification", "Other"],
#         )
#     message = st.text_area("Tell me about your project")
#     submitted = st.form_submit_button("Book a consultation")
#     if submitted:
#         st.success(f"Thanks {name or 'there'}! Your request for {date} has been noted.")

# # ============================================================================
# # CONTACT
# # ============================================================================
# st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Let\'s Solve Problems With Data.</div>', unsafe_allow_html=True)

# st.markdown(
#     f"""
#     <p style="color:{TEXT_MUTED}; max-width:800px; font-size:1.02rem;">
#     Every dataset holds the answer to a complex challenge. Whether you need to
#     uncover hidden trends, identify operational bottlenecks, or build predictive
#     models for strategic growth, I am ready to transform your raw data into
#     actionable solutions.
#     </p>
#     """,
#     unsafe_allow_html=True,
# )

# st.link_button("Send an Email", f"mailto:{EMAIL}")

# link_cols = st.columns(len(SOCIAL_LINKS))
# for col, (label, url) in zip(link_cols, SOCIAL_LINKS):
#     with col:
#         st.markdown(f'<a href="{url}" style="color:{ACCENT}; font-weight:600;">{label}</a>', unsafe_allow_html=True)

# # ============================================================================
# # FOOTER
# # ============================================================================
# st.markdown(
#     f'<div class="footer">© {NAME}. All rights reserved.'
#     '<br><span style="opacity:0.6;"></span></div>',
#     unsafe_allow_html=True,
# )
import os
import streamlit as st

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="MD ATICK HASSAN | Data And Research Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================================
# ✏️  EDIT-ME ZONE #1 — YOUR BASIC INFO
# ----------------------------------------------------------------------------
# Change these values to your own. Nothing else below this block needs to
# be touched unless you want to restyle the page.
# ============================================================================
NAME = "MD ATICK HASSAN"
NAV_LOGO = "ATICK HASSAN"
TITLE = "Data & Research Analyst"
BADGE_TEXT = "UPWORK DATA And RESEARCH ANALYST"
TAGLINE = (
    "I help organizations and individuals extract powerful predictive insights "
    "from complex datasets. Data & Research Analyst on Upwork with 150+ "
    "completed projects globally."
)
EMAIL = "mdatickhassansustian72@gmail.com"
BOOKING_URL = "https://meet.google.com/cex-wfed-meo"
FIVERR_URL = "https://www.fiverr.com/atick_hassan/"
UPWORK_URL = "https://www.upwork.com/freelancers/~01f546868f99a434e3?p=2077839586975793152"

# Your headshot for the hero section. Put the file inside the "images"
# folder next to this script and point to it here. If the file isn't
# found, the hero simply shows text only — nothing breaks.
PROFILE_IMAGE = "images/profile.jpg"

SOCIAL_LINKS = [
    ("LinkedIn", "https://www.linkedin.com/in/md-atick-hassan/"),
    ("Fiverr", "https://www.fiverr.com/atick_hassan/"),
    ("Upwork", "https://www.upwork.com/freelancers/~01f546868f99a434e3?p=2077839586975793152"),
    ("YouTube", "https://www.youtube.com/@MDAtickhassan72"),
    ("Facebook", "https://www.facebook.com/crushking.atick"),
]

ABOUT_HTML = """
Hi there!<br><br>
My goal is to provide solutions that meet or exceed my clients' expectations.<br><br>
Do you need accurate insights from your survey or research data to make informed decisions
using statistical data analysis or data science projects? I help researchers and organizations
turn complex datasets into rigorous findings, reproducible workflows, and stakeholder-ready reports.<br><br>
I am a Data and Research Analyst with 3+ years of experience and 1,000+ completed projects.
My work spans data cleaning, exploratory analysis, hypothesis testing, regression,
forecasting, machine learning, and data visualization. I usually do most of my work in R,
though I also use Python, SQL, Power BI, Excel, SPSS, JASP, and Jamovi.
"""

CORE_EXPERTISE = [
    "Data cleaning/preprocessing (messy or unstructured data) to conduct research and get accurate results",
    "Data Analysis, large survey data analytics and data visualization for business and research",
    "Descriptive Statistics (mean, median, range, IQR, frequency, percentage)",
    "Bi-variate analyses: t-tests, correlations, chi-square tests, and non-parametric tests",
    "Multivariate analyses: ANOVA, MANOVA, PCA, factor analysis, regression analysis",
    "Correlation and Regression Analysis to explore relationships and enable predictive insights",
    "Dimensionality Reduction: feature extraction & selection",
    "Time Series Analysis to identify trends and patterns for business",
    "Clustering (k-means, DBSCAN, hierarchical clustering)",
    "Machine Learning",
]

DELIVERABLES = [
    "A clear analysis plan aligned with your question",
    "Clean, documented, reproducible code",
    "Publication- or decision-ready tables and visualizations",
    "Detailed interpretation of results",
    "A full report of the study, results, and interpretation",
]

# ============================================================================
# ✏️  EDIT-ME ZONE #2 — YOUR PROJECTS
# ----------------------------------------------------------------------------
# For each project fill in:
#   "image" -> path to a picture on YOUR computer. Put your screenshots/plots
#              inside the "images" folder next to this .py file and just
#              reference the filename, e.g. "images/rfm_analysis.png".
#              If a file isn't found, a placeholder box is shown instead —
#              nothing breaks.
#   "link"  -> URL to the live project, GitHub repo, or PDF write-up.
#              Leave as "" to hide the button for that project.
# ============================================================================
PROJECTS = [
    {
        "category": "Business Intelligence / SQL",
        "title": "RFM Customer Segmentation & Sales Analysis",
        "desc": (
            "Built an end-to-end SQL pipeline: imported a raw sales flat file "
            "into a database, profiled every column with DISTINCT checks, then "
            "aggregated revenue by product line, year, month, and deal size. "
            "Applied RFM (Recency, Frequency, Monetary) logic with DATEDIFF() "
            "to rank customers by value — the top account came out ahead on "
            "both spend and order frequency, with one product line driving "
            "roughly $3.9M in revenue."
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
            "which of two hosts was speaking, using two prosodic features — "
            "pitch level and pitch variation. The model reached 62.4% overall "
            "classification accuracy. Both predictors were statistically "
            "significant (p < .001 and p = .001), with odds-ratio "
            "interpretation for each coefficient."
        ),
        "tags": ["SPSS", "Logistic Regression", "Speech Analytics"],
        "image": "images1/log1.png",
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
        "image": "images2/churn_dashboard.png",
        "link": "https://github.com/mdatickhassan/",
    },
    {
        "category": "Business Intelligence / Power BI",
        "title": "Healthcare Admissions & Billing Dashboard",
        "desc": (
            "Designed an interactive Power BI dashboard covering 55,500 "
            "admitted patients across multiple hospitals. Surfaces KPIs like "
            "admission YoY, average billing amount, and total billing, with "
            "slicers for year, gender, and condition (arthritis, asthma, "
            "cancer, diabetes, hypertension). Includes a length-of-stay "
            "breakdown and a hospital-by-condition matrix so stakeholders can "
            "drill from a top-level KPI straight down to a specific "
            "hospital's patient mix."
        ),
        "tags": ["Power BI", "Dashboarding", "Healthcare Analytics", "DAX"],
        "image": "images3/Healthcare Project.png",
        "link": "https://github.com/mdatickhassan/",
    },
]

# ============================================================================
# THEME — Midnight Indigo + Amber Gold (new palette, distinct from black
# and from the earlier teal/coral version)
# ============================================================================
PRIMARY_BG = "#141127"      # deep indigo-black
SECONDARY_BG = "#1E1A3C"    # slightly lighter violet-navy for cards
ACCENT = "#F2B705"          # amber gold accent
ACCENT_SOFT = "#F7D488"     # soft gold for tags/borders
TEXT_LIGHT = "#F5F3FF"      # near-white with a violet tint
TEXT_MUTED = "#B7B2D9"      # muted lavender-grey text

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
        font-size: 3.1rem;
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
        background: rgba(242,183,5,0.12);
        color: {ACCENT};
        border: 1px solid {ACCENT};
        border-radius: 999px;
        padding: 0.2rem 0.8rem;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }}

    .profile-photo-wrap {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 0.5rem;
    }}
    .profile-photo-wrap img {{
        width: 220px;
        height: 220px;
        object-fit: cover;
        border-radius: 50%;
        border: 4px solid {ACCENT};
        box-shadow: 0 0 0 6px rgba(242,183,5,0.15);
    }}

    .card {{
        background-color: {SECONDARY_BG};
        border-radius: 14px;
        padding: 1.4rem 1.6rem 1.6rem 1.6rem;
        margin-bottom: 1.2rem;
        border: 1px solid rgba(255,255,255,0.06);
    }}
    .card:hover {{
        border: 1px solid {ACCENT};
    }}

    .img-placeholder {{
        width: 100%;
        height: 170px;
        border-radius: 10px;
        margin-bottom: 1rem;
        background: repeating-linear-gradient(
            45deg,
            rgba(242,183,5,0.08),
            rgba(242,183,5,0.08) 10px,
            rgba(255,255,255,0.03) 10px,
            rgba(255,255,255,0.03) 20px
        );
        border: 1px dashed {ACCENT_SOFT};
        display: flex;
        align-items: center;
        justify-content: center;
        color: {TEXT_MUTED};
        font-size: 0.8rem;
        text-align: center;
        padding: 0.5rem;
    }}

    .tag {{
        display: inline-block;
        background: rgba(245,243,255,0.08);
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

    .expertise-list li, .deliverables-list li {{
        color: {TEXT_MUTED};
        margin-bottom: 0.4rem;
        line-height: 1.5;
    }}

    .footer {{
        text-align: center;
        color: {TEXT_MUTED};
        padding: 2.5rem 0 1rem 0;
        border-top: 1px solid rgba(255,255,255,0.1);
        margin-top: 3rem;
        font-size: 0.85rem;
    }}

    div.stButton > button, div.stLinkButton > a {{
        background-color: {ACCENT} !important;
        color: {PRIMARY_BG} !important;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
    }}
    div.stButton > button:hover, div.stLinkButton > a:hover {{
        background-color: {ACCENT_SOFT} !important;
    }}

    /* ---- Booking form styling ---- */
    div[data-testid="stForm"] {{
        background-color: {SECONDARY_BG};
        border: 1px solid {ACCENT_SOFT};
        border-radius: 14px;
        padding: 1.8rem 1.8rem 1.2rem 1.8rem;
    }}
    div[data-testid="stForm"] label p {{
        color: {ACCENT_SOFT} !important;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    div[data-testid="stForm"] input,
    div[data-testid="stForm"] textarea,
    div[data-testid="stForm"] div[data-baseweb="select"] > div,
    div[data-testid="stForm"] div[data-baseweb="input"] {{
        background-color: {PRIMARY_BG} !important;
        color: {TEXT_LIGHT} !important;
        border: 1px solid rgba(247,212,136,0.35) !important;
        border-radius: 8px !important;
    }}
    div[data-testid="stForm"] input:focus,
    div[data-testid="stForm"] textarea:focus {{
        border: 1px solid {ACCENT} !important;
        box-shadow: 0 0 0 1px {ACCENT} !important;
    }}
    div[data-testid="stForm"] svg {{
        fill: {ACCENT_SOFT} !important;
    }}
    div[data-testid="stForm"] div.stButton > button {{
        width: 100%;
        margin-top: 0.5rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================================
# NAV BAR
# ============================================================================
st.markdown(
    f"""
    <div class="nav-bar">
        <div class="nav-logo">{NAV_LOGO}</div>
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

# ============================================================================
# HERO
# ============================================================================
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
profile_resolved = PROFILE_IMAGE if os.path.isabs(PROFILE_IMAGE) else os.path.join(BASE_DIR, PROFILE_IMAGE)
has_profile_photo = bool(PROFILE_IMAGE) and os.path.exists(profile_resolved)

if has_profile_photo:
    hero_text_col, hero_photo_col = st.columns([3, 1])
else:
    hero_text_col = st.container()

with hero_text_col:
    st.markdown(f'<div class="badge">{BADGE_TEXT}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="hero-title">{NAME}<br><span class="hero-accent">{TITLE}</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="hero-sub">{TAGLINE}</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
    with col1:
        st.link_button("Book Consultation", BOOKING_URL)
    with col2:
        st.link_button("Hire Me on Fiverr", FIVERR_URL)
    with col3:
        st.link_button("Hire Me on Upwork", UPWORK_URL)

if has_profile_photo:
    with hero_photo_col:
        st.markdown('<div class="profile-photo-wrap">', unsafe_allow_html=True)
        st.image(profile_resolved)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# EXPERTISE
# ============================================================================
st.markdown('<div id="expertise"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Expertise</div>', unsafe_allow_html=True)
st.markdown(
    f'<p style="color:{TEXT_MUTED}; max-width:800px; font-size:1.02rem;">{ABOUT_HTML}</p>',
    unsafe_allow_html=True,
)

exp_col1, exp_col2 = st.columns(2)
with exp_col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="category-label">Core Expertise</div>', unsafe_allow_html=True)
    st.markdown(
        '<ul class="expertise-list">' + "".join(f"<li>{item}</li>" for item in CORE_EXPERTISE) + "</ul>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

with exp_col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="category-label">What You Receive</div>', unsafe_allow_html=True)
    st.markdown(
        '<ul class="deliverables-list">' + "".join(f"<li>{item}</li>" for item in DELIVERABLES) + "</ul>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

edu_col, skill_col = st.columns(2)

with edu_col:
    st.markdown(
        """
        <div class="card">
            <div class="category-label">Academic Foundation</div>
            <h4>BBA in Port Management &amp; Logistics</h4>
            <p>Bangladesh Maritime University</p>
            <h4>Data Exploration &amp; Research</h4>
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
                "Statistical Analysis",
            ]
        ),
        unsafe_allow_html=True,
    )
    st.markdown('<br><br><div class="category-label">Tools &amp; Environments</div>', unsafe_allow_html=True)
    st.markdown(
        "".join(
            f'<span class="skill-pill">{s}</span>'
            for s in ["SPSS", "R", "Stata", "Python", "Power BI", "R Markdown", "Excel", "JASP", "Jamovi", "PostgreSQL"]
        ),
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# PROJECTS / WORK
# ============================================================================
st.markdown('<div id="work"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Some of Deployed Solutions</div>', unsafe_allow_html=True)


def render_project(project: dict) -> None:
    """Render one project card: local image (or placeholder), text, tags, link."""
    st.markdown('<div class="card">', unsafe_allow_html=True)

    img_path = project.get("image", "")
    resolved_path = img_path if os.path.isabs(img_path) else os.path.join(BASE_DIR, img_path)

    if img_path and os.path.exists(resolved_path):
        st.image(resolved_path, use_container_width=True)
    else:
        st.markdown(
            f'<div class="img-placeholder">Drop an image at<br><code>{img_path or "images/your_project.png"}</code></div>',
            unsafe_allow_html=True,
        )

    tags_html = "".join(f'<span class="tag">{t}</span>' for t in project["tags"])
    st.markdown(
        f"""
        <div class="category-label">{project['category']}</div>
        <h3>{project['title']}</h3>
        <p style="color:{TEXT_MUTED};">{project['desc']}</p>
        {tags_html}
        """,
        unsafe_allow_html=True,
    )

    if project.get("link"):
        st.link_button("View Project ↗", project["link"])

    st.markdown("</div>", unsafe_allow_html=True)


proj_cols = st.columns(2)
for i, proj in enumerate(PROJECTS):
    with proj_cols[i % 2]:
        render_project(proj)

# ============================================================================
# BOOKING
# ============================================================================
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
            ["Predictive Modeling", "Data Visualization", "Statistical Analysis", "Classification", "Other"],
        )
    message = st.text_area("Tell me about your project")
    submitted = st.form_submit_button("Book a consultation")
    if submitted:
        st.success(f"Thanks {name or 'there'}! Your request for {date} has been noted.")

# ============================================================================
# CONTACT
# ============================================================================
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

st.link_button("Send an Email", f"mailto:{EMAIL}")

link_cols = st.columns(len(SOCIAL_LINKS))
for col, (label, url) in zip(link_cols, SOCIAL_LINKS):
    with col:
        st.markdown(f'<a href="{url}" style="color:{ACCENT}; font-weight:600;">{label}</a>', unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown(
    f'<div class="footer">© {NAME}. All rights reserved.'
    '<br><span style="opacity:0.6;"></span></div>',
    unsafe_allow_html=True,
)
