# ## Conversational Q&A Chatbot
# import streamlit as st
# from langchain.schema import HumanMessage, SystemMessage, AIMessage
# import os
# from dotenv import load_dotenv
# import requests

# # Load environment variables from .env file if present
# load_dotenv()

# # Set API key from environment variable or prompt for it
# api_key = os.getenv("GROQ_API_KEY") or st.text_input("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", type="password")

# # Check if the API key is provided
# if not api_key:
#     st.error("API key is missing! Please provide your GROQ API Key.")
#     st.stop()

# # Initialize the ChatGroq model without passing `headers`
# from langchain_groq import ChatGroq

# try:
#     # Set up the Groq chat model
#     llm = ChatGroq(
#         model="llama-3.1-70b-versatile",
#         temperature=0,
#         max_tokens=None,
#         max_retries=3,
#         timeout=30  # Set the timeout to 30 seconds
#     )
# except Exception as e:
#     st.error(f"Error initializing ChatGroq model: {str(e)}")
#     st.stop()

# ## Streamlit UI
# st.set_page_config(page_title="Conversational Q&A Chatbot")
# st.header("Hey, Let's Chat")

# # Ensure session state for 'flowmessages' is initialized
# if 'flowmessages' not in st.session_state:
#     st.session_state['flowmessages'] = [
#         SystemMessage(content="You are an AI assistant designed to provide informative, helpful, and engaging responses. Your role is to assist users by answering questions, providing recommendations, and facilitating conversations in a friendly and professional manner. Always prioritize user satisfaction and ensure your responses are clear, accurate, and contextually relevant. Use your knowledge to empower users with information, while maintaining a respectful and supportive tone throughout the interaction.")
#     ]

# # Function to load the LLM model and get the response
# def get_chatmodel_response(question):
#     try:
#         # Append user question to session state
#         st.session_state['flowmessages'].append(HumanMessage(content=question))
        
#         # Get the response from the chat model using the `invoke` method
#         answer = llm.invoke(st.session_state['flowmessages'])
        
#         # Append the AI response to session state
#         st.session_state['flowmessages'].append(AIMessage(content=answer.content))
#         return answer.content
#     except requests.exceptions.Timeout:
#         st.error("Request timed out. Please try again later.")
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")
#     return None

# # Input field for user input
# input_text = st.text_input("Input: ", key="input")

# # Button to submit the question
# submit = st.button("Ask the question")

# # If the button is clicked, process the input and get the response
# if submit and input_text.strip():
#     response = get_chatmodel_response(input_text.strip())
    
#     # Display the response from the model
#     if response:
#         st.subheader("The Response is")
#         st.write(response)
# else:
#     if submit:
#         st.error("Please enter a question before submitting!")

## Conversational Q&A Chatbot
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file if present
load_dotenv()

# Set API key from environment variable or prompt for it
api_key = os.getenv("GROQ_API_KEY") or st.text_input("Enter your GROQ API Key:", type="password")

# Check if the API key is provided
if not api_key:
    st.error("API key is missing! Please provide your GROQ API Key.")
    st.stop()

# Initialize the ChatGroq model without passing `headers`
from langchain_groq import ChatGroq

try:
    # Set up the Groq chat model
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        max_tokens=None,
        max_retries=3,
        timeout=30  # Set the timeout to 30 seconds
    )
except Exception as e:
    st.error(f"Error initializing ChatGroq model: {str(e)}")
    st.stop()

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Ensure session state for 'flowmessages' is initialized
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are an AI assistant designed to provide informative, helpful, and engaging responses. Your role is to assist users by answering questions, providing recommendations, and facilitating conversations in a friendly and professional manner. Always prioritize user satisfaction and ensure your responses are clear, accurate, and contextually relevant. Use your knowledge to empower users with information, while maintaining a respectful and supportive tone throughout the interaction.")
    ]

# Function to load the LLM model and get the response
def get_chatmodel_response(question):
    try:
        # Append user question to session state
        st.session_state['flowmessages'].append(HumanMessage(content=question))
        
        # Get the response from the chat model using the `invoke` method
        answer = llm.invoke(st.session_state['flowmessages'])
        
        # Append the AI response to session state
        st.session_state['flowmessages'].append(AIMessage(content=answer.content))
        return answer.content
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again later.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    return None

# Input field for user input
input_text = st.text_area("Type your message:", key="input", height=100)

# Button to submit the question
submit = st.button("Send")

# If the button is clicked, process the input and get the response
if submit and input_text.strip():
    response = get_chatmodel_response(input_text.strip())
    
    # Display the response from the model
    if response:
        st.subheader("The Response is")
        st.write(response)

# Display conversation in a WhatsApp-like format
if st.session_state['flowmessages']:
    st.subheader("Chat:")
    for message in st.session_state['flowmessages']:
        if isinstance(message, HumanMessage):
            st.markdown(f"<div style='background-color: #dcf8c6; border-radius: 10px; padding: 10px; margin: 5px 0; text-align: right;'>"
                        f"<strong>You:</strong> {message.content}</div>", unsafe_allow_html=True)
        elif isinstance(message, AIMessage):
            st.markdown(f"<div style='background-color: #f1f0f0; border-radius: 10px; padding: 10px; margin: 5px 0; text-align: left;'>"
                        f"<strong>Assistant:</strong> {message.content}</div>", unsafe_allow_html=True)
        elif isinstance(message, SystemMessage):
            st.markdown(f"<div style='background-color: #e8e8e8; border-radius: 10px; padding: 10px; margin: 5px 0; text-align: left;'>"
                        f"<strong>System:</strong> {message.content}</div>", unsafe_allow_html=True)
