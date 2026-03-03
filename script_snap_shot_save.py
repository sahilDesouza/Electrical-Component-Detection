# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Snapshot for data set collection
#
# Note: You will need an SD card to run this example.
# You can use your OpenMV Cam to save image files.

import sensor
import time
import machine
import image

led = machine.LED("LED_BLUE")
count = 10
image_name = "background"
image_format = ".jpg"
image_count_down = 3
width = 96                              # Width of frame (pixels)
height = 96
img_photo_count = 40

sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.set_windowing(width, height)   # Crop sensor frame to this resolution
sensor.skip_frames(time=2000)  # Wait for settings take effect.



start = time.ticks_ms()
img = sensor.snapshot()

while (count < img_photo_count):
    img = sensor.snapshot()
    if time.ticks_diff(time.ticks_ms(), start) >= 1000:
        start = time.ticks_ms()
        if image_count_down > 0:
            image_count_down -= 1
        elif image_count_down == 0:
            img.save(image_name + str(count) + image_format)
            img.draw_rectangle(0, 0, width, height, color=(0,0,0), fill=True)
            image_count_down = 3

            time.sleep_ms(100)
            print("Saving image:", image_name + str(count) + image_format)
            count += 1
    if image_count_down != 0:
        img.draw_string(
            int(width / 2 + 0.5) - 35,
            int(height / 2 + 0.5) - 50,
            str(image_count_down),
            scale=10.0)

raise (Exception("Please reset the camera to see the new file."))







