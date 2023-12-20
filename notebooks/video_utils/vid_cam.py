"""
Module to process video camera related functionality.
"""

import os
import sys
from math import floor
from os import path
from time import time

import cv2

CAPTURE_WIDTH = 640
CAPTURE_HEIGHT = 480
IMAGE_DIRECTORY = path.join(path.dirname(__file__), "..", "..", "dataset",
                            "captures")


def capture_image_from_stream(cam_node,
                              height=CAPTURE_HEIGHT,
                              width=CAPTURE_WIDTH,
                              imgdir=IMAGE_DIRECTORY,
                              imgname=None):
    """
    Usage: capture_image_from_stream(cam_node[, height[, width[, filename]]])

    Parameters:
        cam_node: An int representing the camera video node of the right camera
        height: An int signifying the height of the video capture
        width: An int signifying the width of the video capture
        imgidr: A pathlike for the directory to save the image in
        imgname: A string containing the path of the output image file
    Returns:
        None

    Side Effects:
        Writes an image to the path specified at imgdir/imgname
    """
    v_cap = cv2.VideoCapture(cam_node)

    # Check if camera is opened successfully

    if not v_cap.isOpened():
        print("Video camera opening failed")
        sys.exit(-1)

    # Set capture resolution
    v_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    v_cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    # Start frame-by-frame capture

    while True:
        _, frame = v_cap.read()
        cv2.flip(frame, 1)
        cv2.imshow("preview", frame)

        # Wait for user quit input
        key = cv2.waitKey(1) & 0xFF

        if key and key == ord("q"):
            break

        if key == ord("c"):
            try:
                os.stat(imgdir)
            except FileNotFoundError:
                os.mkdir(imgdir)

            if imgname is not None:
                cv2.imwrite(path.join(imgdir, imgname), frame)
            else:
                cv2.imwrite(path.join(imgdir, f"capture{floor(time())}.jpg"),
                            frame)

    # Release camera after completion
    v_cap.release()
    cv2.destroyAllWindows()
