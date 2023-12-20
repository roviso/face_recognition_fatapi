from math import floor
from os import path
from time import time

from video_utils import vid_cam

vid_cam.capture_image_from_stream(0,
                                  imgdir=path.join(
                                      path.abspath(path.dirname(__file__)),
                                      "..", "dataset", "captures"))
