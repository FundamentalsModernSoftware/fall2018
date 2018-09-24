import sys
import imageio

DURATION = 0.2   # seconds per frame
OUTPUT_FILE = 'animated.gif'

images = []
for filename in sys.argv[1:]:
    images.append(imageio.imread(filename))

imageio.mimwrite(OUTPUT_FILE, images, format='GIF-PIL',duration=DURATION)
