from config import * 
import simpleaudio as sa



#playsound(WAVE_OUTPUT_FILENAME)


filename = WAVE_OUTPUT_FILENAME
print(WAVE_OUTPUT_FILENAME)
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing