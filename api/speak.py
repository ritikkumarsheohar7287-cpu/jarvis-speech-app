from flask import Flask, request, jsonify
import pyttsx3
import uuid

app = Flask(__name__)

@app.route("/speak", methods=["POST"])
def speak():
    data = request.json
    text = data.get("text", "")

    engine = pyttsx3.init()
    filename = f"audio_{uuid.uuid4()}.mp3"
    engine.save_to_file(text, filename)
    engine.runAndWait()

    return jsonify({"message": "Speech generated", "file": filename})

if __name__ == "__main__":
    app.run(debug=True)
