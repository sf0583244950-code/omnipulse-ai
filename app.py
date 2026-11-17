import streamlit as st
from google import genai

st.set_page_config(page_title="OmniPulse AI", page_icon="⚡", layout="centered")

st.title("⚡ OmniPulse AI")
st.caption("Mobile-Optimized Gemini AI Assistant")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Please configure your GEMINI_API_KEY in Streamlit Secrets.")
else:
    client = genai.Client(api_key=api_key)

    user_prompt = st.text_area("Ask OmniPulse:", placeholder="Type your prompt here...")

    if st.button("Send", type="primary"):
        if user_prompt.strip():
            with st.spinner("Thinking..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_prompt,
                    )
                    st.markdown("### Response:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt first.")
