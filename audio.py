import librosa

def load_audio(file_path):
    y, sr = librosa.load(file_path)
    return y, sr



def get_beats(y, sr):

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo = float(tempo[0])
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return tempo, beat_times

def get_energy(y, sr):

    energy = librosa.feature.rms(y=y)[0]
    frames = range(len(energy))
    times = librosa.frames_to_time(frames, sr=sr)
    return energy, times


#if __name__ == "__main__":
    y, sr = load_audio("assets/AmericanIdiot.mp3")
    print(f"Sample rate: {sr}")
    print(f"Duration: {len(y) / sr:.2f} seconds")
    
    tempo, beat_times = get_beats(y, sr)
    print(f"Tempo: {tempo:.1f} BPM")
    print(f"First 5 beats at: {beat_times[:5]} seconds")

    energy, energy_times = get_energy(y, sr)
    print(f"Energy frames: {len(energy)}")
    print(f"First 5 energy values: {energy[:5]}")
    print(f"First 5 energy times: {energy_times[:5]}")