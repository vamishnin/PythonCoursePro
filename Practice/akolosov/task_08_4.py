import argparse
import os
import cv2
import numpy
import math
from PIL import Image, ImageDraw
from numpy.lib.polynomial import polyfit

# The target params:
CENTER = [447, 452]
R10 = 67
R_NEXT = 41

def get_score(shot: tuple):
    distance = math.hypot(CENTER[0] - shot[0], CENTER[1] - shot[1])
    res = 0
    r = R10
    for i in range(10):
        if distance < r:
            res = 10 - i
            break
        r += R_NEXT
    return res


def shot_coordinate(current_img_path, pattern_img_path):
    '''
    Return the center of match of the pattern
    '''
    current_img = Image.open(current_img_path)
    pattern_img = Image.open(pattern_img_path)
    current_img_arr = cv2.cvtColor(numpy.array(current_img), cv2.COLOR_RGB2BGR555)
    pattern_img_arr = cv2.cvtColor(numpy.array(pattern_img), cv2.COLOR_RGB2BGR555)
    res = cv2.matchTemplate(current_img_arr, pattern_img_arr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    size = pattern_img_arr.shape
    return max_loc[0] + size[1] / 2, max_loc[1] + size[0] / 2


def parse_args():
    parser = argparse.ArgumentParser(description='Find the score of a shot.')
    parser.add_argument('src_path', help='Path to source file')
    parser.add_argument('pattern_path', help='Path to pattern file')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    shot = shot_coordinate(args.src_path, args.pattern_path)
    print(f"The score is {get_score(shot)}")
