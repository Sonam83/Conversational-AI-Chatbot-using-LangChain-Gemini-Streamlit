import streamlit as st
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  #establishes connection to llm feom dotenv to access output

import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

st.title("Simple Gemini Model as a Regular Model")

prompt=st.text_area("Type your query")

if st.button("Give Answer"):
    rmodel=GoogleGenerativeAI(model="gemini-2.5-flash")
    response=rmodel.invoke(prompt)
    st.write(response)