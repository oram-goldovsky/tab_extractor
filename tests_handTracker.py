import cv2
import os
from handTracker import handTracker
import mediapipe as mp
from matplotlib import pyplot as plt

# fingertips indices: thumb = 4, index = 8, middle = 12, ring = 16, pinky = 20

if __name__ == '__main__':
    plt.figure(1)
    filename = os.listdir('./pictures/')[0]
    path = './pictures/' + filename
    image = cv2.imread(path)

    hand_tracker = handTracker()
    hand = hand_tracker.handsFinder(image)
    positions = hand_tracker.positionFinder(image)


    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
    cv2.waitKey(0)





