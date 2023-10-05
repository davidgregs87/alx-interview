#!/usr/bin/python3
'''
LOCKBOXES
'''


def canUnlockAll(boxes):
    ''' Returns a boolean if all the boxes can be opened '''
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        current_box = boxes[current_key]

        for key in current_box:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.append(key)

    return all(unlocked_boxes)
