# Building a chefbot

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# Defining Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Act as a cooking chef"),
        ("user","Question:{question}")
    ]
    )

# UI
st.title("Talk with the chef 👨‍🍳")
inputText = st.text_input("Ask questions about dishes")

groqApi = ChatGroq(model="gemma-7b-It",temperature=1) #0-2
outputparser = StrOutputParser()
chainSec = prompt|groqApi|outputparser
    
if inputText:
    st.write(chainSec.invoke({'question':inputText}))