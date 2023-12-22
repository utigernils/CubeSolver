import cv2
import numpy as np
import base64

cap = cv2.VideoCapture(1)
min_contour_area = 400

Debug = False

lower_red = np.array([0, 93, 50])
upper_red = np.array([8, 209, 153])
lower_blue = np.array([78, 99, 76])
upper_blue = np.array([146, 176, 162])
lower_orange = np.array([6, 99, 133])
upper_orange = np.array([12, 194, 187])
lower_green = np.array([32, 33, 33])
upper_green = np.array([86, 175, 153])
lower_yellow = np.array([17, 136, 137])
upper_yellow = np.array([90, 216, 203])

upper_sat = 85

def iniDebug():
    Debug = True
    cv2.namedWindow('Red Mask')
    cv2.namedWindow('Blue Mask')
    cv2.namedWindow('Orange Mask')
    cv2.namedWindow('Green Mask')
    cv2.namedWindow('Yellow Mask')
    cv2.namedWindow('Color Mask')

    cv2.createTrackbar('Lower H', 'Red Mask', lower_red[0], 255, lambda x: None)
    cv2.createTrackbar('Upper H', 'Red Mask', upper_red[0], 255, lambda x: None)
    cv2.createTrackbar('Lower S', 'Red Mask', lower_red[1], 255, lambda x: None)
    cv2.createTrackbar('Upper S', 'Red Mask', upper_red[1], 255, lambda x: None)
    cv2.createTrackbar('Lower V', 'Red Mask', lower_red[2], 255, lambda x: None)
    cv2.createTrackbar('Upper V', 'Red Mask', upper_red[2], 255, lambda x: None)

    cv2.createTrackbar('Lower H', 'Blue Mask', lower_blue[0], 255, lambda x: None)
    cv2.createTrackbar('Upper H', 'Blue Mask', upper_blue[0], 255, lambda x: None)
    cv2.createTrackbar('Lower S', 'Blue Mask', lower_blue[1], 255, lambda x: None)
    cv2.createTrackbar('Upper S', 'Blue Mask', upper_blue[1], 255, lambda x: None)
    cv2.createTrackbar('Lower V', 'Blue Mask', lower_blue[2], 255, lambda x: None)
    cv2.createTrackbar('Upper V', 'Blue Mask', upper_blue[2], 255, lambda x: None)

    cv2.createTrackbar('Lower H', 'Orange Mask', lower_orange[0], 255, lambda x: None)
    cv2.createTrackbar('Upper H', 'Orange Mask', upper_orange[0], 255, lambda x: None)
    cv2.createTrackbar('Lower S', 'Orange Mask', lower_orange[1], 255, lambda x: None)
    cv2.createTrackbar('Upper S', 'Orange Mask', upper_orange[1], 255, lambda x: None)
    cv2.createTrackbar('Lower V', 'Orange Mask', lower_orange[2], 255, lambda x: None)
    cv2.createTrackbar('Upper V', 'Orange Mask', upper_orange[2], 255, lambda x: None)

    cv2.createTrackbar('Lower H', 'Green Mask', lower_green[0], 255, lambda x: None)
    cv2.createTrackbar('Upper H', 'Green Mask', upper_green[0], 255, lambda x: None)
    cv2.createTrackbar('Lower S', 'Green Mask', lower_green[1], 255, lambda x: None)
    cv2.createTrackbar('Upper S', 'Green Mask', upper_green[1], 255, lambda x: None)
    cv2.createTrackbar('Lower V', 'Green Mask', lower_green[2], 255, lambda x: None)
    cv2.createTrackbar('Upper V', 'Green Mask', upper_green[2], 255, lambda x: None)

    cv2.createTrackbar('Lower H', 'Yellow Mask', lower_yellow[0], 255, lambda x: None)
    cv2.createTrackbar('Upper H', 'Yellow Mask', upper_yellow[0], 255, lambda x: None)
    cv2.createTrackbar('Lower S', 'Yellow Mask', lower_yellow[1], 255, lambda x: None)
    cv2.createTrackbar('Upper S', 'Yellow Mask', upper_yellow[1], 255, lambda x: None)
    cv2.createTrackbar('Lower V', 'Yellow Mask', lower_yellow[2], 255, lambda x: None)
    cv2.createTrackbar('Upper V', 'Yellow Mask', upper_yellow[2], 255, lambda x: None)

    cv2.createTrackbar('Lower S', 'Color Mask', upper_sat, 255, lambda x: None)

def runDebug():
    lower_red[0] = cv2.getTrackbarPos('Lower H', 'Red Mask')
    upper_red[0] = cv2.getTrackbarPos('Upper H', 'Red Mask')
    lower_red[1] = cv2.getTrackbarPos('Lower S', 'Red Mask')
    upper_red[1] = cv2.getTrackbarPos('Upper S', 'Red Mask')
    lower_red[2] = cv2.getTrackbarPos('Lower V', 'Red Mask')
    upper_red[2] = cv2.getTrackbarPos('Upper V', 'Red Mask')

    lower_blue[0] = cv2.getTrackbarPos('Lower H', 'Blue Mask')
    upper_blue[0] = cv2.getTrackbarPos('Upper H', 'Blue Mask')
    lower_blue[1] = cv2.getTrackbarPos('Lower S', 'Blue Mask')
    upper_blue[1] = cv2.getTrackbarPos('Upper S', 'Blue Mask')
    lower_blue[2] = cv2.getTrackbarPos('Lower V', 'Blue Mask')
    upper_blue[2] = cv2.getTrackbarPos('Upper V', 'Blue Mask')

    lower_orange[0] = cv2.getTrackbarPos('Lower H', 'Orange Mask')
    upper_orange[0] = cv2.getTrackbarPos('Upper H', 'Orange Mask')
    lower_orange[1] = cv2.getTrackbarPos('Lower S', 'Orange Mask')
    upper_orange[1] = cv2.getTrackbarPos('Upper S', 'Orange Mask')
    lower_orange[2] = cv2.getTrackbarPos('Lower V', 'Orange Mask')
    upper_orange[2] = cv2.getTrackbarPos('Upper V', 'Orange Mask')

    lower_green[0] = cv2.getTrackbarPos('Lower H', 'Green Mask')
    upper_green[0] = cv2.getTrackbarPos('Upper H', 'Green Mask')
    lower_green[1] = cv2.getTrackbarPos('Lower S', 'Green Mask')
    upper_green[1] = cv2.getTrackbarPos('Upper S', 'Green Mask')
    lower_green[2] = cv2.getTrackbarPos('Lower V', 'Green Mask')
    upper_green[2] = cv2.getTrackbarPos('Upper V', 'Green Mask')

    lower_yellow[0] = cv2.getTrackbarPos('Lower H', 'Yellow Mask')
    upper_yellow[0] = cv2.getTrackbarPos('Upper H', 'Yellow Mask')
    lower_yellow[1] = cv2.getTrackbarPos('Lower S', 'Yellow Mask')
    upper_yellow[1] = cv2.getTrackbarPos('Upper S', 'Yellow Mask')
    lower_yellow[2] = cv2.getTrackbarPos('Lower V', 'Yellow Mask')
    upper_yellow[2] = cv2.getTrackbarPos('Upper V', 'Yellow Mask')

    upper_sat = cv2.getTrackbarPos('Lower S', 'Color Mask')

def ReadCube():
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    saturation_channel = hsv_image[:, :, 1]
    colorful_mask = saturation_channel > upper_sat
    frame_rgb = np.zeros_like(frame)
    frame_rgb[colorful_mask] = frame[colorful_mask]

    hsv_image = cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2HSV)

    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_orange = cv2.inRange(hsv_image, lower_orange, upper_orange)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_orange, _ = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contours_red = []
    largest_contours_blue = []
    largest_contours_orange = []
    largest_contours_green = []
    largest_contours_yellow = []

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

    for contour in contours_orange:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                largest_contours_orange.append(approx)

    for contour in contours_green:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                largest_contours_green.append(approx)

    for contour in contours_yellow:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                largest_contours_yellow.append(approx)

    for contour in largest_contours_red:
        area = cv2.contourArea(contour)
        if min_contour_area < area:
            cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(frame, 'Red', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    for contour in largest_contours_blue:
        area = cv2.contourArea(contour)
        if min_contour_area < area:
            cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(frame, 'Blue', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    for contour in largest_contours_orange:
        area = cv2.contourArea(contour)
        if min_contour_area < area:
            cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(frame, 'Orange', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 255), 2)

    for contour in largest_contours_green:
        area = cv2.contourArea(contour)
        if min_contour_area < area:
            cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(frame, 'Green', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    for contour in largest_contours_yellow:
        area = cv2.contourArea(contour)
        if min_contour_area < area:
            cv2.drawContours(frame, [contour], 0, (50, 255, 50), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(frame, 'Yellow', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    if Debug:
        runDebug()
        cv2.imshow('Red Mask', mask_red)
        cv2.imshow('Blue Mask', mask_blue)
        cv2.imshow('Orange Mask', mask_orange)
        cv2.imshow('Green Mask', mask_green)
        cv2.imshow('Yellow Mask', mask_yellow)
        cv2.imshow('Color Mask', frame_rgb)

    cv2.namedWindow('Colored Rectangles', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Colored Rectangles', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Colored Rectangles', frame)
    cap.release()
    cv2.destroyAllWindows()

    #fake return
    return "BLRBUDDLBUFULRUURBBDLDFBDLLLUFUDFRURRRLDLBFRFFFUBBRDFD"

def CheckCube():
    #fake return
    return True





