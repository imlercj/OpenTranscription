# OpenTranscription

Playing around with [Open AIs Whisper model](https://github.com/openai/whisper). With this you can record and transcribe the audio output from you PC. You need to enable [Stereo Mix](https://www.howtogeek.com/howto/39532/how-to-enable-stereo-mix-in-windows-7-to-record-audio/). 
Stereo Mix is a tool that allows the user to record the output stream of a computer such as broadcasting radio, speaker outputs, live streaming audios, even system sounds

## Whisper - intro
Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.

![Approach](/assets/approach.png)

## This repo contains:

- Record.ipynb: for recording audio using Pyaudio and Stereo Mix .

- config.py: common audio parameters

- parse_wisper.py: transcribe audio

- play_file.py: play audio file


## Goals / Possibilities 😎:

- create a web app / gui to start and stop audio recordings
  - move audio recording to a separate thread
- implement contineus transcription
  - feed back to GUI
- post process transcription
  - summary
  - knowledge graph
  - Entity extraction, NER
  - word cloud (low hanging fruit) 🍎