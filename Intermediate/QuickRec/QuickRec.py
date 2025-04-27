import sounddevice as sd
import numpy as np
import wave
import os
import time
import threading
from pynput import keyboard

# ตั้งค่าค่าต่างๆ
SAMPLE_RATE = 44100  # อัตราการบันทึกเสียง (Hz)
CHANNELS = 1  # จำนวนช่องเสียง
DEVICE_ID = 1  # เลือกอุปกรณ์อินพุตที่ต้องการใช้
recording = []
is_recording = False
recording_thread = None
file_index = 1  # เริ่มจากไฟล์ 01.wav
keys_pressed = set()  # ใช้เก็บปุ่มที่ถูกกด

def get_filename():
    """ สร้างชื่อไฟล์ลำดับถัดไป เช่น 01.wav, 02.wav """
    global file_index
    while True:
        filename = f"{file_index:02d}.wav"
        if not os.path.exists(filename):  # ตรวจสอบว่าไฟล์ยังไม่มีอยู่
            return filename
        file_index += 1  # เพิ่มเลขไฟล์

def record_audio():
    """ ฟังก์ชันบันทึกเสียงที่ทำงานใน thread """
    global is_recording, recording
    is_recording = True
    recording = []

    def callback(indata, frames, time, status):
        if status:
            print(f"⚠ Warning: {status}", flush=True)
        if is_recording:
            recording.append(indata.copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, device=DEVICE_ID, dtype='int16', callback=callback) as stream:
        while is_recording:
            time.sleep(0.1)  # ป้องกันการใช้ CPU สูงเกินไป

    if recording:
        filename = get_filename()
        audio_data = np.concatenate(recording, axis=0)
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  # 16-bit PCM
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio_data.tobytes())
        print(f"✅ บันทึกเสียงเสร็จ: {filename}")

def on_press(key):
    global is_recording, recording_thread, keys_pressed
    keys_pressed.add(key)  # บันทึกปุ่มที่ถูกกด
    if keyboard.Key.alt_l in keys_pressed and keyboard.KeyCode.from_char('k') in keys_pressed:
        if not is_recording:
            print("🎤 เริ่มบันทึก...")
            recording_thread = threading.Thread(target=record_audio)
            recording_thread.start()

def on_release(key):
    global is_recording, recording_thread, keys_pressed
    if key in keys_pressed:
        keys_pressed.remove(key)  # เอาปุ่มที่ปล่อยออกจากเซ็ต
    
    # หยุดบันทึกเมื่อปล่อยทั้ง Alt และ K
    if keyboard.Key.alt_l not in keys_pressed and keyboard.KeyCode.from_char('k') not in keys_pressed:
        if is_recording:
            is_recording = False
            if recording_thread:
                recording_thread.join()  # รอให้การบันทึกเสียงเสร็จสิ้น
            print("⏹ หยุดบันทึก")

# เริ่มตรวจจับปุ่ม
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("🔄 กด 'Alt + K' ค้างไว้เพื่อบันทึกเสียง... ปล่อยทั้งสองปุ่มเพื่อหยุด")

listener.join()
