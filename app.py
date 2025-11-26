import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import os
import tempfile

# ==========================================
# 1. SETUP & CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="SpeakGenie 🧞", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header styling */
    .stTitle {
        color: #ffffff !important;
        text-align: center;
        font-size: 3.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        padding: 1rem 0;
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #ffffff;
        font-size: 1.5rem;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Remove default chat container background */
    .stChatFloatingInputContainer {
        display: none !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f093fb 0%, #f5576c 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.2rem;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    /* Chat message styling */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    
    .stChatMessage p {
        color: #333 !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
    }
    
    /* User message - left side with different color */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
    }
    
    /* Assistant message - right side */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* Info box styling */
    .stInfo {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 1rem;
    }
    
    .stInfo p, .stInfo div {
        color: white !important;
    }
    
    /* Error styling */
    .stError {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
    }
    
    .stError p {
        color: white !important;
    }
    
    /* Radio buttons */
    [data-testid="stRadio"] > label {
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    /* Select box */
    [data-testid="stSelectbox"] > label {
        font-weight: bold;
        font-size: 1.1rem;
    }

    /* Slider styling */
    [data-testid="stSlider"] > label {
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .feature-card h3 {
        color: #667eea;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .feature-card p {
        color: #333;
        font-size: 0.95rem;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Welcome message */
    .welcome-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .welcome-box h2 {
        color: #667eea;
        margin-bottom: 1rem;
    }
    
    .welcome-box p {
        color: #666;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Section header styling */
    .section-header {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        margin: 1.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
GOOGLE_API_KEY = "AIzaSyCYxhSlJQJtnwakzVvMLBl4Vo6d-QaeR4U"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-flash-latest')
except Exception as e:
    st.error("⚠️ API Key missing or invalid. Please check configuration.")

# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================

def listen_to_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return "API Error"
        except:
            return None

def speak_text(text, lang_code='en'):
    try:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(tfile.name + ".mp3")
        return tfile.name + ".mp3"
    except Exception as e:
        return None

# ==========================================
# 3. UI LAYOUT & LOGIC
# ==========================================

# Header
st.markdown('<h1 class="stTitle">🎙️ SpeakGenie 🧞</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ Learn Languages through Talk & Play! ✨</p>', unsafe_allow_html=True)

# Sidebar Settings
st.sidebar.markdown("## ⚙️ Settings")
st.sidebar.markdown("---")

# 1. Mode Selection
mode = st.sidebar.radio(
    "🎯 Select Mode:",
    ["Free Chat 🗣️", "Roleplay 🎭"],
    help="Choose between free conversation or guided roleplay scenarios"
)

st.sidebar.markdown("---")

# 2. Age Selection
user_age = st.sidebar.slider(
    "🎂 Your Age:",
    min_value=6,
    max_value=16,
    value=10,
    help="Genie will adjust the difficulty based on your age!"
)

st.sidebar.markdown("---")

# 3. Native Language
native_lang = st.sidebar.selectbox(
    "🌍 Play Audio in:",
    ["English", "Hindi", "Marathi", "Tamil"],
    help="Select your preferred language for audio playback"
)

lang_map = {"English": "en", "Hindi": "hi", "Marathi": "mr", "Tamil": "ta"}
selected_lang_code = lang_map[native_lang]

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Quick Tips")
st.sidebar.markdown("""
<div style='background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px;'>
    <p style='color: white; margin: 0.5rem 0;'><strong>💡 Speak clearly and loudly</strong></p>
    <p style='color: white; margin: 0.5rem 0;'><strong>🎯 Keep sentences short</strong></p>
    <p style='color: white; margin: 0.5rem 0;'><strong>😊 Have fun learning!</strong></p>
</div>
""", unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome Section (Only show if no messages)
if len(st.session_state.messages) == 0:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="welcome-box">
            <h2>👋 Welcome to SpeakGenie!</h2>
            <p>I see you are <strong>{user_age} years old</strong>! I'm Genie, your friendly AI tutor.</p>
            <p>I will adjust my English to match your level.</p>
            <p>🎤 Click the button below to start!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature cards
        feat_col1, feat_col2 = st.columns(2)
        
        with feat_col1:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🗣️</div>
                <h3>Free Chat</h3>
                <p>Practice speaking naturally with your AI tutor</p>
            </div>
            """, unsafe_allow_html=True)
        
        with feat_col2:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🎭</div>
                <h3>Roleplay</h3>
                <p>Learn through real-life scenarios and situations</p>
            </div>
            """, unsafe_allow_html=True)

# Age-based instruction
age_instruction = ""
if user_age <= 9:
    age_instruction = "User is a young child (6-9). Use very simple words. Keep sentences extremely short (5-8 words). Be very playful and encouraging."
elif user_age <= 13:
    age_instruction = "User is a pre-teen (10-13). Use moderate vocabulary. Complete sentences are okay. Be friendly but educational."
else:
    age_instruction = "User is a teenager (14-16). Use conversational, standard English. You can discuss slightly more complex topics. Be supportive."

# AI Personality Setup
if mode == "Free Chat 🗣️":
    prompt_context = f"""You are Genie, a friendly English tutor.
    
IMPORTANT - ADAPT TO AGE: {age_instruction}

Goals:
- Teach English in a fun way.
- Correct grammar gently.
- Keep the child engaged.

Style:
- Use emojis.
- Be supportive.
- Short responses (max 2 sentences).

Multilingual Option:
- If native language support is ON, give a short translation in the child's chosen language (Hindi/Marathi/Tamil).
"""
    if len(st.session_state.messages) > 0:
        st.markdown('<p class="section-header">🤖 Chat with Genie</p>', unsafe_allow_html=True)
else:
    scenario = st.sidebar.selectbox(
        "🎬 Choose Scenario:",
        ["At the Shop 🛒", "At School 🏫", "At the Doctor 🩺"],
        help="Select a roleplay scenario to practice"
    )
    
    prompt_context = f"""You are Genie, playing a character in this scenario: {scenario}.  
    
IMPORTANT - ADAPT TO AGE: {age_instruction}

Behavior:
- Speak ONLY one line at a time.
- Keep dialog short and clear.
- Wait for the child (User) to respond.
"""
    if len(st.session_state.messages) > 0:
        st.markdown(f'<p class="section-header">🎭 Roleplay: {scenario}</p>', unsafe_allow_html=True)

# Display Chat History (without white box wrapper)
if len(st.session_state.messages) > 0:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# ==========================================
# 5. MAIN INTERACTION LOOP
# ==========================================

# Center the speak button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎤 Click to Speak", use_container_width=True):
        user_text = listen_to_user()
        
        if user_text:
            # 1. Show User Input
            st.session_state.messages.append({"role": "user", "content": user_text})
            with st.chat_message("user"):
                st.write(user_text)

            # 2. Generate Initial AI Response (English)
            full_prompt = prompt_context + f"\nUser said: {user_text}"
            response = model.generate_content(full_prompt)
            ai_reply = response.text 

            # 3. TRANSLATION LOGIC
            if selected_lang_code != 'en':
                translation_prompt = f"Translate the following text to {native_lang}. Output ONLY the translated text. Text: '{ai_reply}'"
                trans_response = model.generate_content(translation_prompt)
                ai_reply = trans_response.text

            # 4. Display AI Response
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            with st.chat_message("assistant"):
                st.write(ai_reply)

                # 5. Speak the Response
                audio_file = speak_text(ai_reply, selected_lang_code)
                if audio_file:
                    st.audio(audio_file, format='audio/mp3', autoplay=True)
                    
        else:
            st.error("😕 I didn't catch that. Please try again!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 1rem;'>
    <p>Made with ❤️ by SpeakGenie Team | Powered by AI 🤖</p>
    <p style='font-size: 0.9rem;'>Backed by Amity University 🎓</p>
</div>
""", unsafe_allow_html=True)
    
        
        
    
    
       

        
  

    
    

            
