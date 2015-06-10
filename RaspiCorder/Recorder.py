#!/usr/bin/python

import pyaudio
import time
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()

class Recorder:
	fname = "_"

	def __init__(self, instrument):
		self.fname = instrument + "_" + time.strftime("%Y-%m-%d_%H-%M-%S")

	def record():
		stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
		frames = []
 
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    	data = stream.read(CHUNK)
    	frames.append(data) 
 
		# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()
		 
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()