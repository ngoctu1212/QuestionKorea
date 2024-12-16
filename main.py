from flask import Flask, render_template, request, jsonify
import os
import random
import pygame
import threading
import time

app = Flask(__name__)

# Thư mục chứa file âm thanh
AUDIO_FOLDER = r"C:\Users\Nguyen Tu\PycharmProjects\CrawDataHanCuc\Bai1"

# Phát âm thanh đa luồng
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

@app.route('/')
def index():
    """Trang chủ."""
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_random_files():
    """API để phát ngẫu nhiên 5 file ghi âm."""
    audio_files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith('.mp3') or f.endswith('.wav')]

    if len(audio_files) < 5:
        return jsonify({"error": "Không đủ file ghi âm trong thư mục!"}), 400

    random_files = random.sample(audio_files, 10)

    def play_files():
        for file in random_files:
            file_path = os.path.join(AUDIO_FOLDER, file)
            play_audio(file_path)
            time.sleep(10)  # Chờ 30 giây giữa các file

    threading.Thread(target=play_files).start()
    return jsonify({"status": "Đang phát các file", "files": random_files})

if __name__ == '__main__':
    app.run(debug=True)
