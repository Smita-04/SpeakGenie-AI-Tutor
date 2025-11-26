# 🧞‍♂️  SpeakGenie: Real-Time AI Voice Tutor for Kids
![alt text](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

![alt text](https://img.shields.io/badge/Python-3.11-blue)

![alt text](https://img.shields.io/badge/AI-Google_Gemini-orange)

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

### 1️⃣ 🗣️ Free-Flow AI Chat
- Acts as a friendly, safe English teacher.
- Corrects grammar politely and keeps answers age-appropriate.

### 2️⃣ 🎭 Interactive Roleplay Mode
- **Scenarios:** "At the Shop", "At School", "At the Doctor".
- The AI adopts a persona (e.g., Shopkeeper) to practice real-life dialogues.

### 3️⃣ 🌏 Native Language Bridge (Key Feature)
- **Input:** Speak in English.
- **Output:** The AI replies in English (text) for reading practice, but speaks in **Hindi/Tamil/Marathi** for understanding.
- **Visual Translation:** Displays the translated text on screen instantly.

---

## 📸 Demo

### 🔹 1. Interactive Chat
![Chat Demo](./screenshots/chat.png)

### 🔹 2. Roleplay Mode (Shopping)
![Roleplay Demo](./screenshots/roleplay.png)

### 🔹 3. Hindi Translation Support
![Hindi Mode](./screenshots/hindi.png)

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Brain:** Google Gemini 1.5 Flash
- **Voice Input:** SpeechRecognition
- **Audio Output:** gTTS (Google Text-to-Speech)

---

## 🚀 How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/SpeakGenie-AI-Tutor.git
