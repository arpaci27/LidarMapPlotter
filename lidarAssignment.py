import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def parse_data(data_lines):
    angles, distances = [], []
    for line in data_lines:
        parts = line.split(' :/: ')
        angle = float(parts[0].split(' -> ')[1])
        distance = float(parts[1])
        angles.append(angle)
        distances.append(distance)
    return angles, distances


def polar_to_cartesian(angles, distances):
    x = distances * np.cos(np.radians(angles))
    y = distances * np.sin(np.radians(angles))
    return x, y


background_image_path = 'empty.png'
background = Image.open(background_image_path)

fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.imshow(background, extent=[0, 1000, 0, 1000])

center_x, center_y = 500, 500

ax.axis('off')

output_image_path = 'lidar_map.png'
plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=100, transparent=True)

print(output_image_path)
