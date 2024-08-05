import matplotlib as plt
import streamlit as st
import requests


title = st.text_input("Enter title to search")
if title:
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey=cb60844f"
        re = requests.get(url)
        re = re.json()
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(re["Poster"])
        with col2:
            st.subheader(re["Title"])
            st.caption(f"Genre: {re["Genre"]}")
            st.caption(f"Release Year: {re["Year"]}")
            st.write(re["Plot"])
            st.text(f"{re["imdbRating"]}")
            st.progress(float(re["imdbRating"])/10)
    except:
        st.error("No movie found with that title")
