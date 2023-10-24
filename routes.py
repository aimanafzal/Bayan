from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect-tone', methods=['POST'])
def detect_tone_api():
    data = request.json
    text = data.get('text')
    detected_tone = detect_tone(text)
    suggested_tone = suggest_tone(detected_tone)
    return jsonify({'detected_tone': detected_tone, 'suggested_tone': suggested_tone})

if __name__ == '__main__':
    app.run(debug=True)

