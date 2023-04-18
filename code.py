import board
import neopixel
import time

# Constants
NUM_PIXELS = 30  # Number of pixels in the strip
PIN = board.D7   # Data pin connected to the NeoPixel strip
BRIGHTNESS = 0.3 # Brightness level (0 to 1)

# Initialize the NeoPixel strip
pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, pixel_order=neopixel.RGBW, auto_write=False, brightness=BRIGHTNESS)

# Define colors as RGBW tuples
RED = (255, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
WHITE = (0, 0, 0, 255)

# Create a list of colors
colors = [RED, GREEN, BLUE, WHITE]

# Function to set all pixels to a specific color
def set_color(color):
    for i in range(NUM_PIXELS):
        pixels[i] = color
    pixels.show()

# Main loop
while True:
    for color in colors:
        set_color(color)
        time.sleep(1)

