import pygame
import numpy as np
import tkinter as tk
from particles import Particle, emit_particles
from audio import load_audio, get_beats, get_energy
from tkinter import filedialog

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

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

pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

beat_index = 0

start_time = pygame.time.get_ticks()

overlay = pygame.Surface((800, 600))
overlay.set_alpha(22)
overlay.fill((0, 0, 0))

song_length = len(y) / sr

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = (pygame.time.get_ticks() - start_time) / 1000.0

    if beat_index < len(beat_times):
        next_beat = beat_times[beat_index]
        if current_time >= next_beat - 0.1:
            beat_index += 1
            energy_index = min(np.searchsorted(energy_times, current_time), len(energy) - 1)
            current_energy = energy[energy_index]
            test_particles.extend(emit_particles((400, 300), current_energy * 50, 20))

    screen.blit(overlay, (0, 0))
    for i in test_particles:
        i.update()
        if i.is_alive():
            pygame.draw.circle(screen, i.color, (int(i.position[0]), int(i.position[1])), i.size)
    bar_width = int((current_time / song_length) * 800)
    pygame.draw.rect(screen, (100, 100, 100), (0, 580, 800, 10))
    pygame.draw.rect(screen, (255, 255, 255), (0, 580, bar_width, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()