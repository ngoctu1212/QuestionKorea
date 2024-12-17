from flask import Flask, render_template, send_from_directory, jsonify
import os
import random

app = Flask(__name__)
AUDIO_FOLDER = "audio"  # Thư mục chứa file ghi âm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-audio-files', methods=['GET'])
def get_audio_files():
    """API trả về danh sách ngẫu nhiên 5 file âm thanh."""
    audio_files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith('.mp3') or f.endswith('.m4a')]
    if len(audio_files) < 5:
        return jsonify({"error": "Không đủ file ghi âm!"}), 400
    random_files = random.sample(audio_files, 30)
    return jsonify({"files": random_files})

@app.route('/audio/<filename>')
def serve_audio(filename):
    """Phục vụ file âm thanh để phát trên trình duyệt."""
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
