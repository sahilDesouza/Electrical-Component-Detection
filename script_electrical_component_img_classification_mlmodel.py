import sensor
import image
import time
from ei_classifier import *

# Initialize camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)  # 320x240
sensor.skip_frames(time=2000)

clock = time.clock()
CONF_THRESHOLD = 0.8  # Only consider strong predictions

while True:
    clock.tick()
    img = sensor.snapshot()

    # Run Edge Impulse classifier
    result = classify(img)

    if result:
        predictions = result[0]['classification']

        # Get label with highest confidence
        max_label = max(predictions, key=predictions.get)
        confidence = predictions[max_label]

        if confidence > CONF_THRESHOLD:
            if max_label == "led":
                print("LED detected!")
            elif max_label == "resistor":
                print("Resistor detected!")
        else:
            print("Background / uncertain")

        # Optional: display on image
        img.draw_string(10, 10, "%s: %.2f" % (max_label, confidence),
                        color=(255,0,0), scale=2)

    print("FPS:", clock.fps())
