from distance_of_points import distance


def is_collision(object_1, object_2):
    left_top = [object_2.x - object_2.width / 2, object_2.y + 73.5]
    right_top = [object_2.x + object_2.width / 2, object_2.y + 73.5]
    left_bottom = [object_2.x - object_2.width / 2, object_2.y - 73.5]
    right_bottom = [object_2.x + object_2.width / 2, object_2.y - 73.5]

    object_1_center = [object_1.x, object_1.y]
    collision_distance = object_1.height / 2

    return distance(left_top, object_1_center) <= collision_distance \
        or distance(right_top, object_1_center) <= collision_distance \
        or distance(left_bottom, object_1_center) <= collision_distance \
        or distance(right_bottom, object_1_center) <= collision_distance \
        or (object_2.x - object_2.width / 2 <= object_1.x + object_1.height / 2
            and object_1.x - object_1.width / 2 <= object_2.x + object_2.width / 2
            and (object_1.y - object_1.height / 2 < right_bottom[1] or object_1.y + object_1.height / 2 > right_top[1]))
