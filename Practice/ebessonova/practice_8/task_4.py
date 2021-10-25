from Tasks.opencv_task import cvsimple
from PIL import Image
import math
import enum


class PointConst(enum.IntEnum):
    POINTS = 10


def calc_target_centre(current_img_path):
    current_img = Image.open(current_img_path)
    width, height = current_img.size
    target_centre = width // 2
    return target_centre


def calc_point_bounds(current_img_path):
    target_centre = calc_target_centre(current_img_path)
    radius_step = target_centre // (PointConst.POINTS + 1)  # считаем по ширине так как картинка примерно квадратная
    point_steps = []
    st = radius_step * 2  # десятка занимает два шага
    while st < target_centre:
        point_steps.append(st)
        st += radius_step

    return point_steps


def get_points(point_steps, target_centre, shoot_area):

    shoot_centre = [(shoot_area[2] + shoot_area[0]) // 2, (shoot_area[3] + shoot_area[1]) // 2]
    shoot_distance_to_centre = math.sqrt(math.pow(target_centre - shoot_centre[0], 2) +
                                         math.pow(target_centre - shoot_centre[1], 2))

    points = PointConst.POINTS
    for aim in point_steps:
        if int(shoot_distance_to_centre) <= aim:
            return points
        else:
            points -= 1
    return points


if __name__ == '__main__':
    args = cvsimple.parse_args()
    max_val, closest_area = cvsimple.image_match_template(args.source, args.pattern)
    points = get_points(calc_point_bounds(args.source), calc_target_centre(args.source), closest_area)
    print(f'You scored {points}')

