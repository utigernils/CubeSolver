import cv2 as cv2
import numpy as np


cap = cv2.VideoCapture(0)
min_contour_area = 500

def ReadCube():
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_red = np.array([120, 0, 0])
    upper_red = np.array([255, 80, 80])
    lower_blue = np.array([30, 30, 70])
    upper_blue = np.array([80, 80, 200])

    mask_red = cv2.inRange(frame_rgb, lower_red, upper_red)
    mask_blue = cv2.inRange(frame_rgb, lower_blue, upper_blue)

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contours_red = []
    largest_contours_blue = []

    for contour in contours_red:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                largest_contours_red.append(approx)

    for contour in contours_blue:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                largest_contours_blue.append(approx)

    for contour in largest_contours_red:
        cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(frame, 'Red', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    for contour in largest_contours_blue:
        cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(frame, 'Blue', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.namedWindow('Colored Rectangles', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Colored Rectangles', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Colored Rectangles', frame)


def CheckCube():
    #fake return
    return False

def destroyReadCube():
    cap.release()
    cv2.destroyAllWindows()


