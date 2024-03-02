import os
import time
from strings_and_frets_detector import detect_strings_edges, detect_frets_edges
from matplotlib import pyplot as plt
from image import Image
from rotate_crop import rotate_neck_picture, crop_neck_picture
from grid_detection import string_detection, fret_detection
import cv2

# if __name__ == "__main__":  # string check
#     tuning = ["E", "A", "D", "G", "B", "E6"]
#     plt.figure(1)
#     filename = os.listdir('./pictures/')[0]
#     print("File found: " + filename + " - Processing...")
#     test_image = Image(path='./pictures/' + filename)
#     original_crds_edges = detect_strings_edges(test_image)
#     for i in range(len(original_crds_edges)):
#         print(f"{tuning[i]} string coordinates in image are: {original_crds_edges.separating_lines[tuning[i]]}")
#
#     for i in range(len(original_crds_edges)):
#         cv2.line(test_image.image, original_crds_edges.separating_lines[tuning[i]][0], original_crds_edges.separating_lines[tuning[i]][1], (0, 0, 255), 2)
#     plt.imshow(cv2.cvtColor(test_image.image, cv2.COLOR_BGR2RGB))
#     plt.show()
#     cv2.waitKey(0)


if __name__ == "__main__":  # frets check
    plt.figure(1)
    filename = os.listdir('./pictures/')[3]
    print("File found: " + filename + " - Processing...")
    test_image = Image(path='./pictures/' + filename)
    original_crds_edges = detect_frets_edges(test_image)
    for i in range(len(original_crds_edges)):
        if (i % 10) == 0 and i != 10:
            print(f"{i + 1}st fret coordinates in image are: {original_crds_edges[i]}")
        elif (i % 10) == 1 and i != 11:
            print(f"{i + 1}nd fret coordinates in image are: {original_crds_edges[i]}")
        elif (i % 10) == 2 and i != 12:
            print(f"{i + 1}rd fret coordinates in image are: {original_crds_edges[i]}")
        else:
            print(f"{i + 1}th fret coordinates in image are: {original_crds_edges[i]}")

    for i in range(len(original_crds_edges)):
        cv2.line(test_image.image, original_crds_edges[i][0], original_crds_edges[i][1], (0, 0, 255), 2)
    plt.imshow(cv2.cvtColor(test_image.image, cv2.COLOR_BGR2RGB))
    plt.show()
    cv2.waitKey(0)

