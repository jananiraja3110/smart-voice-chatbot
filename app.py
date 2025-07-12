import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import speech_recognition as sr
import tempfile

from responses import get_bot_response
from fun_facts import get_random_fact

st.set_page_config(page_title="Funny AI Chatbot 🤖", layout="centered")

st.title("🎙️ Smart Voice Chatbot")
st.markdown("Talk to me and I'll respond with jokes, facts, and sarcasm!")

# Function: Listen to voice and return text
def listen_to_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"🗣️ You said: {text}")
        return text
    except:
        st.error("❌ Sorry, I couldn't understand that.")
        return ""

# Function: Convert text to speech and play it
def speak(text):
    tts = gTTS(text=text, lang='en')
    
    # Create temp file manually instead of keeping it open
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        temp_path = tmp.name
    
    tts.save(temp_path)
    audio = AudioSegment.from_mp3(temp_path)
    play(audio)
    
    os.remove(temp_path)  # Clean up the temp file


# Button to start voice input
if st.button("🎤 Start Talking"):
    user_input = listen_to_mic()
    if user_input:
        bot_reply = get_bot_response(user_input)
        st.success(f"🤖 Bot: {bot_reply}")
        speak(bot_reply)

        st.divider()
        st.subheader("😂 Random Fun Fact:")
        st.info(get_random_fact())

st.markdown("---")
st.caption("Built with ❤️ using Python + Streamlit")
