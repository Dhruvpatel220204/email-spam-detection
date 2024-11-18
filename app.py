import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))


st.title("Email Spam Classification Application")
