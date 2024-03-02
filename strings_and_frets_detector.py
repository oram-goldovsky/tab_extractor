from matplotlib import pyplot as plt
import numpy as np
from image import Image
from strings import Strings
from rotate_crop import rotate_neck_picture, crop_neck_picture
from grid_detection import string_detection, fret_detection
import cv2


# class StringDetector:


def detect_strings_edges(img):
    tuning = ["E", "A", "D", "G", "B", "E6"]
    chord_image = img
    rotation_angle, rotated_image = rotate_neck_picture(chord_image)
    first_y_cut, last_y_cut, cropped_image = crop_neck_picture(rotated_image)
    cropped_width, cropped_length, _ = cropped_image.image.shape

    string_edges_cropped_rotated = string_detection(cropped_image)[0]
    string_edges_uncropped = string_edges_cropped_rotated.__copy__()
    for i in range(len(string_edges_uncropped)):
        right_edge, left_edge = string_edges_uncropped.separating_lines[tuning[i]]
        # string_edges_uncropped.separating_lines[self.tuning[i]] = [(cropped_width - 1, right_extreme), (0, left_extreme)]
        list(right_edge)[1] = (right_edge[1] + first_y_cut)
        list(left_edge)[1] = (left_edge[1] + first_y_cut)
        string_edges_uncropped.separating_lines[tuning[i]] = right_edge, left_edge

    (cropped_h, cropped_w) = cropped_image.image.shape[:2]
    (uncropped_h, uncropped_w) = (cropped_h + first_y_cut + last_y_cut, cropped_w)
    uncropped_center = (uncropped_w / 2, uncropped_h / 2)
    cropped_center = (cropped_w / 2, cropped_h / 2)  # testing - better then uncropped in getRotationMatrix2D???
    M_reverse = cv2.getRotationMatrix2D(cropped_center, rotation_angle, 1.0)  # why is angle better than -angle? ans: the rotation function rotates -angle!
    string_edges_in_original_crds = string_edges_uncropped.__copy__()
    for i in range(len(string_edges_in_original_crds)):
        old_edges = string_edges_in_original_crds.separating_lines[tuning[i]]
        old_edges0_mat = np.array([old_edges[0][0], old_edges[0][1], 1]).transpose()
        old_edges1_mat = np.array([old_edges[1][0], old_edges[1][1], 1]).transpose()
        new_edge0 = np.matmul(M_reverse, old_edges0_mat)
        new_edge1 = np.matmul(M_reverse, old_edges1_mat)
        # new_edges = cv2.warpAffine(old_edges, M_reverse, (uncropped_w, uncropped_h))
        string_edges_in_original_crds.separating_lines[tuning[i]] = [new_edge0.astype(int), new_edge1.astype(int)]
        string_edges_in_original_crds.separating_lines[tuning[i]][0][1] = string_edges_in_original_crds.separating_lines[tuning[i]][0][1] + first_y_cut - 10
        string_edges_in_original_crds.separating_lines[tuning[i]][1][1] = string_edges_in_original_crds.separating_lines[tuning[i]][1][1] + first_y_cut - 10

    return string_edges_in_original_crds
    # return string_edges_uncropped


def detect_frets_edges(img):
    chord_image = img
    rotation_angle, rotated_image = rotate_neck_picture(chord_image)
    first_y_cut, last_y_cut, cropped_image = crop_neck_picture(rotated_image)
    cropped_width, cropped_length, _ = cropped_image.image.shape

    fret_edges_cropped_rotated, _ = fret_detection(cropped_image)
    fret_edges_uncropped = fret_edges_cropped_rotated.copy()

    for i in range(len(fret_edges_uncropped)):
        top_edge, bottom_edge = fret_edges_uncropped[i]
        # string_edges_uncropped.separating_lines[self.tuning[i]] = [(cropped_width - 1, right_extreme), (0, left_extreme)]
        list(top_edge)[1] = (top_edge[1] + first_y_cut)
        list(bottom_edge)[1] = (bottom_edge[1] + first_y_cut)
        fret_edges_uncropped[i] = top_edge, bottom_edge

    (cropped_h, cropped_w) = cropped_image.image.shape[:2]
    (uncropped_h, uncropped_w) = (cropped_h + first_y_cut + last_y_cut, cropped_w)
    cropped_center = (cropped_w / 2, cropped_h / 2)
    uncropped_center = (uncropped_w / 2, uncropped_h / 2)
    M_reverse = cv2.getRotationMatrix2D(cropped_center, 1.45*rotation_angle, 1.0)  # TODO: multiplying angle by ~1.45 seems not fix, not sure why???
    fret_edges_in_original_crds = fret_edges_uncropped.copy()
    for i in range(len(fret_edges_in_original_crds)):
        old_edges = fret_edges_in_original_crds[i]
        old_edges0_mat = np.array([old_edges[0][0], old_edges[0][1], 1]).transpose()
        old_edges1_mat = np.array([old_edges[1][0], old_edges[1][1], 1]).transpose()
        new_edge0 = np.matmul(M_reverse, old_edges0_mat)
        new_edge1 = np.matmul(M_reverse, old_edges1_mat)
        # new_edges = cv2.warpAffine(old_edges, M_reverse, (uncropped_w, uncropped_h))
        fret_edges_in_original_crds[i] = [new_edge0.astype(int), new_edge1.astype(int)]
        fret_edges_in_original_crds[i][0][1] = fret_edges_in_original_crds[i][0][1] + first_y_cut - 10
        fret_edges_in_original_crds[i][1][1] = fret_edges_in_original_crds[i][1][1] + first_y_cut - 10

    return fret_edges_in_original_crds


