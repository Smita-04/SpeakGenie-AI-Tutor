# 🧞‍♂️  SpeakGenie: Real-Time AI Voice Tutor for Kids
![alt text](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)![alt text](https://img.shields.io/badge/Python-3.11-blue)![alt text](https://img.shields.io/badge/AI-Google_Gemini-orange)

- **SpeakGenie** is an interactive, voice-first AI application designed to help children (ages 6-16) practice English conversation. It uses Generative AI to adapt to the child's age, correct grammar gently, and supports roleplay scenarios to build confidence.
---
## 🌟 Key Features
### 1️⃣ 🗣️ Real-Time Voice Interaction
- **Voice-to-Voice:** The child speaks, and Genie replies instantly with audio.
- **Web-Ready:** Uses streamlit-mic-recorder for seamless browser-based microphone access.
- 
### 2️⃣ 🎂 Smart Age Adaptation
- **Dynamic Complexity:** The AI adjusts its vocabulary, sentence length, and tone based on the child's age (Slider: 6 to 16 years).
- **Ages 6-9:** Simple words, playful tone, short sentences.
- **Ages 10-16:** Conversational English, encouraging tone.
  
### 3️⃣ 🎭 Interactive Roleplay Mode
- **Scenario-Based Learning:** Students practice real-life situations.
- 🛒 **At the Shop:** Buying items, asking prices.
- 🏫 **At School:** Talking to a teacher.
- 🩺 **At the Doctor:** Describing symptoms.
### 4️⃣ 🌏 Native Language Bridge (Bonus Feature)
- **Visual & Audio Translation:** If a child speaks English but needs help understanding the reply, the app can:
- Display the English text (for reading practice).
- Speak the response in their native language (Hindi, Tamil, Marathi).
- Display the translated text on-screen.
---

## 📸 Demo
<img width="1920" height="975" alt="Screenshot (549)" src="https://github.com/user-attachments/assets/f0842b03-018d-4883-ac5d-634be17a1bc8" />

<img width="1920" height="972" alt="Screenshot (550)" src="https://github.com/user-attachments/assets/c9e5e8d6-e2d6-424b-8288-92b9b6326402" />


### 🔹 1. Interactive Chat
<img width="1920" height="977" alt="Screenshot (551)" src="https://github.com/user-attachments/assets/e8c28337-175b-4dc3-be25-97df96214c27" />


### 🔹 2. Roleplay Mode (Shopping)
<img width="1920" height="969" alt="Screenshot (553)" src="https://github.com/user-attachments/assets/2b62bc2b-dc46-41be-9b1a-722a2a68e88d" />


### 🔹 3. Hindi Translation Support
<img width="1920" height="977" alt="Screenshot (554)" src="https://github.com/user-attachments/assets/83ea5e73-eb61-41ca-9534-f6b5961305f7" />


---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Brain:** Google Gemini 1.5 Flash
- **Voice Input:** SpeechRecognition
- **Audio Output:** gTTS (Google Text-to-Speech)
- This project was built using Python and the following libraries:

| Component        | Technology / Library        | Purpose                                       |
|------------------|------------------------------|------------------------------------------------|
| Frontend UI      | Streamlit                    | Rapid web application interface.               |
| Audio Input      | streamlit-mic-recorder       | Browser-compatible microphone recording.        |
| Speech Processing| SpeechRecognition            | Converting WAV audio to text (STT).            |
| The "Brain"      | Google Gemini 1.5 Flash      | LLM for generating intelligent, age-appropriate responses. |
| Audio Output     | gTTS (Google TTS)            | Converting AI text response to MP3 audio.      |


---

## 🚀 How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/Smita-04/SpeakGenie-AI-Tutor.git
