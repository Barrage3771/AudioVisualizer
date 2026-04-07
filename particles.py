import random

class Particle:
    def __init__(self, position, velocity, size, color, lifespan):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.color = color
        self.lifespan = lifespan

    def update(self):
        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1])
        self.lifespan -= 1

    def is_alive(self):
        return self.lifespan > 0

def emit_particles(center, energy, num_particles, color=(255, 255, 255)):
    particles = []
    for _ in range(num_particles):
        new_particle = Particle(
            position=center,
            velocity=(random.uniform(-1,1) * energy , random.uniform(-1,1) * energy),
            size=5,
            color=color,
            lifespan=60
        )
        particles.append(new_particle)
    return particles


#if __name__ == "__main__":
    burst = emit_particles(center=(400, 300), energy=3.0, num_particles=10)
    print(f"Created {len(burst)} particles")
    print(f"First particle position: {burst[0].position}")
    print(f"First particle velocity: {burst[0].velocity}")

    # simulate 5 frames
    for frame in range(5):
        burst[0].update()
    
    print(f"Position after 5 frames: {burst[0].position}")
    print(f"Lifespan after 5 frames: {burst[0].lifespan}")