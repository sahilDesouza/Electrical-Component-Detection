#
# Electrical Component Classification model script
#
# Note: You will need an SD card to run this example.
# You can use your OpenMV Cam to save image files.

import sensor
import time
import ml

# Setup values
width = 96                             # Width of frame (pixels)
height = 96
THRESHOLD = 0.45

#setup camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing(width, height)    # Crop sensor frame to this resolution
sensor.skip_frames(time=2000)

#Load the ML model trained on edge impulse
model = ml.Model("trained.tflite")
print(model)

clock = time.clock()
print("/********************LIVE IMAGE CLASSIFICATION********************/")
while True:
    clock.tick()
    img = sensor.snapshot()

    output = model.predict([img])[0].flatten().tolist()

    if len(output) == 0:
        print("NO OUTPUT DETECTED)")
        continue
    elif output[0] > THRESHOLD:
        print("BACKGROUND DETECTED")
    elif output[1] > THRESHOLD:
        print("LED DETECTED")
    elif output[2] > THRESHOLD:
        print("RESISTOR DETECTED")

    #print(clock.fps(), "fps\t", "%s = %f\t" % (scores[0][0], scores[0][1]))
