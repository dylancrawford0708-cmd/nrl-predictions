
import streamlit as st

st.set_page_config(page_title="NRL Predictor", page_icon="🏉")

st.title("🏉 NRL Match Predictor")
st.write("Welcome to your NRL prediction dashboard!")

st.info(
    "This is our first version. The predictions are a demo, "
    "not real forecasts based on historical NRL data."
)

home_team = st.selectbox(
    "Choose the home team",
    [
        "Brisbane Broncos",
        "Canterbury Bulldogs",
        "Cronulla Sharks",
        "Melbourne Storm",
        "Penrith Panthers",
        "Sydney Roosters",
        "Other"
    ]
)

away_team = st.selectbox(
    "Choose the away team",
    [
        "Melbourne Storm",
        "Brisbane Broncos",
        "Canterbury Bulldogs",
        "Cronulla Sharks",
        "Penrith Panthers",
        "Sydney Roosters",
        "Other"
    ],
    index=1
)

if st.button("Analyse Match"):
    if home_team == away_team:
        st.warning("Please choose two different teams.")
    else:
        st.subheader(f"{home_team} vs {away_team}")
        st.write("Your match dashboard is ready for the next stage.")
        st.write("Next, we'll add real statistics and prediction models.")
