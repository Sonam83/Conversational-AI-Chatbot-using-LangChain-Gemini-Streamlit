import streamlit as st
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  #establishes connection to llm feom dotenv to access output,and loads everything into current environment on accessing api from .env
#also loads everything from .env to current environment from any of the files in same env folder

import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

st.set_page_config(page_title='Chat_Bot',page_icon='😍')
st.title("Chat Bot with Langchain and Streamlit")
# ----------------- till above part 1-------------------------



#-------------------------below is part 2---------------------------

#Below is used to check all previous messages as memory with session state, used as loop
if "conv" not in st.session_state:
    st.session_state["conv"]=[] #stores conversation
    st.session_state["memory"]=[] #act as memory
    st.session_state["memory"].append(("system","act as 6 year old child")) #works after 1st loop and prompt for conversational model is list of messages, so appending to list of memory to fetch whenever required

#------------------------------below is part 4 --------------------------
for y in st.session_state["conv"]:  #to see everything on interface as chatgpt from start at every loop
    with st.chat_message(y["role"]):
        st.write(y["content"])


# -----------------------below is part 3 ---------------------------------
prompt=st.chat_input("Type your Queries")

if prompt:
    st.session_state["conv"].append({"role":"user","content":prompt}) #user role in chatgpt style interface
    st.session_state["memory"].append(("user",prompt))

    with st.chat_message("user"):  #display on chat interface
        st.write(prompt)

    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response=model.invoke(st.session_state["memory"]) #as memory has system and user msg as list of msg

    with st.chat_message("ai"):  #display on chat interface
        st.write(response.content)


    st.session_state["conv"].append({"role":"ai","content":response.content}) #ai role
    st.session_state["memory"].append(("ai",response.content))

