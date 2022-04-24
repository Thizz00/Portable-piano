from pprint import pprint

import numpy as np

samplerate = 44100 #Frequecy in Hz
#g(f)=A*sin(2*pi*f*t)

def get_wave(freq, duration=0.3):  
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

a_wave = get_wave(440, 1)

#wave features
print(len(a_wave)) # 44100
print(np.max(a_wave)) # 4096
print(np.min(a_wave)) # -4096

def get_piano_notes():
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0 # silent note
    
    return(note_freqs)
get_piano_notes()


import numpy as np

def get_song_data(music_notes):
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

#music_notes_fromuser=str()

music_notes = 'C-g-d'
data = get_song_data(music_notes)
print(data)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
from scipy.io.wavfile import write
write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))