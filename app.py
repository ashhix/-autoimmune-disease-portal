import streamlit as st
import pandas as pd
import os

# Set Page Title and Icon (appears in browser tab)
st.set_page_config(page_title="Autoimmune Disease Database", page_icon="🧬")

# Page Title with Logo
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="https://www.shutterstock.com/shutterstock/photos/627082940/display_1500/stock-vector-logo-of-rheumatism-campaign-autoimmune-disorder-joints-mixed-connective-tissue-disease-abstract-627082940.jpg" width="80" style="margin-right: 15px;">
        <h1 style="color: white; padding: 10px; border-radius: 10px;">
            Autoimmune Disease Database
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar Tools
st.sidebar.header("Tools")
tools = ["BLAST", "KEGG", "Primer Designing Tool", "Transcription & Translation Tool", "Complementary Tool", "UniProt", "ChEMBL"]
for tool in tools:
    st.sidebar.button(tool)

# Upload dataset (Sidebar)
st.sidebar.subheader("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Autoimmune Dataset (CSV)", type=["csv"])

# Function to load dataset
@st.cache_data
def load_dataset(file):
    if file is not None:
        return pd.read_csv(file)
    return None

# Load dataset
df = load_dataset(uploaded_file)

# Main Section Layout
col1, col2 = st.columns([2, 3])

with col1:
    # Autoimmune Disease Info
    st.subheader("Autoimmune Diseases")
    st.write(
        "Autoimmune diseases occur when the body's immune system mistakenly attacks its own tissues. "
        "This database provides key insights into genetic markers associated with autoimmune disorders."
    )
    st.markdown("[Click here to learn more about Autoimmune Diseases](https://www.mayoclinic.org/diseases-conditions/autoimmune-disorders/)", unsafe_allow_html=True)

    # Search Functionality
    st.subheader("Search Gene / HLA Allele")
    search_term = st.text_input("Enter Gene or HLA Allele:")

    if st.button("Search"):
        if df is not None:
            results = df[df.astype(str).apply(lambda row: row.str.contains(search_term, case=False, na=False).any(), axis=1)]
            if not results.empty:
                st.write(results[['HLA Allele', 'Allele Classification', 'Disease', 'Clinical Significance']])
            else:
                st.warning("No results found. Please try another search term.")
        else:
            st.error("Dataset not found. Please upload the dataset.")

with col2:
    # Display images from URLs with adjustable sizes
    image_urls = [
        "https://admin.opentran.net/dictionary/wlibrary/a/5ff5b1cf50c323.45196897.jpg",
        "https://i.ytimg.com/vi/0XCG2kAg2qI/mqdefault.jpg",
        "https://gdb.voanews.com/01000000-0a00-0242-69d6-08dc274347ba_cx2_cy0_cw95_w1080_h608_s.jpg"
    ]

    for image_url in image_urls:
        st.image(image_url, width=400)  # Set width dynamically

# Display dataset preview (if uploaded)
if df is not None:
    st.subheader("Dataset Preview")
    st.write(df.head())
