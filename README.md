# Jarvis Speech App 🎤

## Features
- Write text → Converts to speech
- API built using Flask
- Frontend built with HTML+JS
- Ready to deploy on Vercel

## How to Run Locally
```bash
pip install -r requirements.txt
python api/speak.py

---

## 🚀 Deployment Steps (Vercel)

1. Create **GitHub Repository**
2. Push all files
3. Go to **https://vercel.com**
4. Click **New Project → Import from GitHub**
5. Deploy 🚀

---

## ⚠ Important Notes

| Feature | Status on Vercel |
|---------|-------------------|
| pyttsx3 speech locally | ✔ Works |
| pyttsx3 on Vercel | ❌ NOT POSSIBLE |
| Can we use Web Speech API? | ✔ YES (Best way) |

👉 **Better Solution = Browser Speech API only** (No backend needed!)

Example:
```html
<script>
  function speakText() {
    const text = document.getElementById('text').value;
    const speech = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(speech);
  }
</script>
