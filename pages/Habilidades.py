import streamlit as st

st.title("Habilidades :mag_right:")

with st.container():
    hab, prof = st.columns(2)

    with hab:
        st.title("Python :snake:")

    with prof:
        st.slider(min_value = 0, max_value = 100, value = 90, disabled = True, label = "Python", label_visibility = "hidden")

with st.container():
    hab, prof = st.columns(2)

    with hab:
        st.title("SQL :desktop_computer:")

    with prof:
        st.slider(min_value = 0, max_value = 100, value = 80, disabled = True, label = "SQL", label_visibility = "hidden")

with st.container():
    hab, prof = st.columns(2)

    with hab:
        st.title("Metabase :bar_chart:")

    with prof:
        st.slider(min_value = 0, max_value = 100, value = 100, disabled = True, label = "Metabase", label_visibility = "hidden")

with st.container():
    hab, prof = st.columns(2)

    with hab:
        st.title("APIs :satellite_antenna:")

    with prof:
        st.slider(min_value = 0, max_value = 100, value = 80, disabled = True, label = "APIs", label_visibility = "hidden")

with st.container():
    hab, prof = st.columns(2)

    with hab:
        st.title("Google Cloud Platform :cloud:")

    with prof:
        st.slider(min_value = 0, max_value = 100, value = 60, disabled = True, label = "GCP", label_visibility = "hidden")
