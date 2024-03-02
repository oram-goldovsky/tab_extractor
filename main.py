import os
from strings_and_frets_detector import detect_strings_edges, detect_frets_edges
from matplotlib import pyplot as plt
from image import Image
import cv2
from handTracker import handTracker


if __name__ == '__main__':
    plt.figure(1)
    tuning = ["E", "A", "D", "G", "B", "E6"]
    filename = os.listdir('./pictures/')[0]
    print("File found: " + filename + " - Processing...")
    test_image = Image(path='./pictures/' + filename)
    frets_edges = detect_frets_edges(test_image)
    strings_edges = detect_strings_edges(test_image)

    hand_tracker = handTracker()
    hand = hand_tracker.handsFinder(test_image.image)  # draw option works weird - consider changing
    positions = hand_tracker.positionFinder(test_image.image)

    # plt.subplot(211)
    # plt.imshow(cv2.cvtColor(hand, cv2.COLOR_BGR2RGB))
    # plt.subplot(212)
    plt.imshow(cv2.cvtColor(test_image.image, cv2.COLOR_BGR2RGB))
    plt.show()
    cv2.waitKey(0)

