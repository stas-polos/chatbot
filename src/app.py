import os

import streamlit as st
from openai import OpenAI


base_url = os.environ.get("LLM_URL")
model_name = os.environ.get("LLM_MODEL")

st.set_page_config(page_title="Chatbot", layout="wide")
st.title(f"Chatbot ({model_name})")
st.markdown(
    """
<style>
body {
    background-color: #fafafa;
}
.chat-message {
    padding: 10px 16px;
    border-radius: 10px;
    margin-bottom: 10px;
    max-width: 80%;
    line-height: 1.5;
}
.user {
    background-color: #404040;
    align-self: flex-end;
    margin-left: auto;
}
.assistant {
    background-color: #1C1C1C;
    align-self: flex-start;
    margin-right: auto;
}
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 6px;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
}
input[type="text"] {
    border-radius: 8px;
}
</style>
""",
    unsafe_allow_html=True,
)


if not base_url or not model_name:
    st.error("Model base url and name not configured. Ensure Docker Model Runner is enabled and Compose is set up.")
    st.stop()

client = OpenAI(api_key="dummy_key", base_url=base_url)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue

    st.markdown(f"<div class='chat-message {msg['role']}'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

user_input = st.text_input("Type your message:", key="input", label_visibility="collapsed")
if st.button("Send", use_container_width=True) and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model=model_name, messages=st.session_state.messages)
    if content := response.choices[0].message.content:
        reply = content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
