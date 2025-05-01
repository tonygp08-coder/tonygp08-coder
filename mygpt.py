import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyArQG1kpxvVOWpN-O4XrStX2ejnkWNPqQY")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot")
st.title("🤖 Ask-ai Gemini-Powered")

# Session state for conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    
    # Generate Gemini response
    try:
        response = model.generate_content(user_input)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"
    
    st.session_state.chat_history.append(("bot", bot_reply))

# Display conversation
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"🧑‍💻 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Gemini:** {msg}")
