import pygame
import random
import numpy as np
import tkinter as tk
from particles import Particle, emit_particles
from audio import load_audio, get_beats, get_energy, get_frequency_bands
from tkinter import filedialog

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

screen_width = screen.get_width()
screen_height = screen.get_height()

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select a song",
    filetypes=[("Audio files", "*.mp3 *.wav")]
)

if not file_path:
    exit()

test_particles = []#emit_particles((400, 300), 3.0, 20)



y, sr = load_audio(file_path)
tempo, beat_times = get_beats(y, sr)
energy, energy_times = get_energy(y, sr)
bass_energy, mid_energy, treble_energy = get_frequency_bands(y, sr)
bass_energy = bass_energy / np.max(bass_energy)
mid_energy = mid_energy / np.max(mid_energy)
treble_energy = treble_energy / np.max(treble_energy)

pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

beat_index = 0

start_time = pygame.time.get_ticks()

overlay = pygame.Surface((screen_width, screen_height))
overlay.set_alpha(15)
overlay.fill((0, 0, 0))

song_length = len(y) / sr

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    current_time = (pygame.time.get_ticks() - start_time) / 1000.0

    freq_index = min(np.searchsorted(energy_times, current_time), len(bass_energy) - 1)
    current_bass = bass_energy[freq_index]
    current_mid = mid_energy[freq_index]
    current_treble = treble_energy[freq_index]

    r = int(max(current_bass * 255, 50))
    g = int(max(current_mid * 255, 50))
    b = int(max(current_treble * 255, 50))
    color = (r, g, b)

    if beat_index < len(beat_times):
        next_beat = beat_times[beat_index]
        if current_time >= next_beat - 0.1:
            beat_index += 1
            energy_index = min(np.searchsorted(energy_times, current_time), len(energy) - 1)
            current_energy = energy[energy_index]
            x = random.randint(20, screen_width - 50)
            y_pos = random.randint(20, screen_height - 50)
            test_particles.extend(emit_particles((x, y_pos), current_energy * 50, 20, color=color))

    screen.blit(overlay, (0, 0))
    for i in test_particles:
        i.update()
        if i.is_alive():
            pygame.draw.circle(screen, i.color, (int(i.position[0]), int(i.position[1])), i.size)
    bar_width = int((current_time / song_length) * screen_width)
    pygame.draw.rect(screen, (100, 100, 100), (0, (screen_height - 20), screen_width, 10))
    pygame.draw.rect(screen, (255, 255, 255), (0, (screen_height - 20), bar_width, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()