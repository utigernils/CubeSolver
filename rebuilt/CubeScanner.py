import cv2
import base64
import numpy as np

filename = "CubeScanner.py"

camera1 = cv2.VideoCapture(1)
camera2 = cv2.VideoCapture(2)

def updateMasks(new_lower_red, new_upper_red, new_lower_blue, new_upper_blue, new_lower_orange, new_upper_orange, new_lower_green, new_upper_green, new_lower_yellow, new_upper_yellow):
    global lower_red
    global upper_red
    global lower_blue
    global upper_blue
    global lower_orange
    global upper_orange
    global lower_green
    global upper_green
    global lower_yellow
    global upper_yellow

    lower_red = new_lower_red
    upper_red = new_upper_red
    lower_blue = new_lower_blue
    upper_blue = new_upper_blue
    lower_orange = new_lower_orange
    upper_orange = new_upper_orange
    lower_green = new_lower_green
    upper_green = new_upper_green
    lower_yellow = new_lower_yellow
    upper_yellow = new_upper_yellow

    print(filename + ": lower_red-" + str(lower_red))
    print(filename + ": upper_red-" + str(upper_red))
    print(filename + ": lower_blue-" + str(lower_blue))
    print(filename + ": upper_blue-" + str(upper_blue))
    print(filename + ": lower_orange-" + str(lower_orange))
    print(filename + ": upper_orange-" + str(upper_orange))
    print(filename + ": lower_green-" + str(lower_green))
    print(filename + ": upper_green-" + str(upper_green))
    print(filename + ": lower_yellow-" + str(lower_yellow))
    print(filename + ": upper_yellow-" + str(upper_yellow))

def getCapturedFrame(camera):
    ret, frame = camera.read()
    return frame

def maskFrame(upper, lower, frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower, upper)
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)

    return masked_frame

def encodeFrame(frame):
     _, buffer = cv2.imencode('.jpg', frame)
     frame_encoded = base64.b64encode(buffer.tobytes()).decode('utf-8')

     return 'data:image/jpeg;base64,' + frame_encoded

def getMaskedFrame(upper, lower, camera):
    frame = getCapturedFrame(globals()[camera])
    frame = maskFrame(upper, lower, frame)
    return encodeFrame(frame)

def scan(camera):
    if False:
        frame = getCapturedFrame(globals()[camera])
        red_mask = maskFrame(upper_red, lower_red, frame)
        blue_mask = maskFrame(upper_blue, lower_blue, frame)
        orange_mask = maskFrame(upper_orange, lower_orange, frame)
        green_mask = maskFrame(upper_green, lower_green, frame)
        yellow_mask = maskFrame(upper_yellow, lower_yellow, frame)
        colors_under_circles = []
        circle_centers = [
            (100, 100), (250, 100), (400, 100),
            (100, 250), (250, 250), (400, 250),
            (100, 400), (250, 400), (400, 400)
        ]

        for circle_center in circle_centers:
            if np.any(red_mask[circle_center[1], circle_center[0]] != 0):
                colors_under_circles.append("F")
                color = (0, 0, 255)
            elif np.any(blue_mask[circle_center[1], circle_center[0]] != 0):
                colors_under_circles.append("L")
                color = (255, 0, 0)
            elif np.any(orange_mask[circle_center[1], circle_center[0]] != 0):
                colors_under_circles.append("B")
                color = (0, 165, 255)
            elif np.any(green_mask[circle_center[1], circle_center[0]] != 0):
                colors_under_circles.append("R")
                color = (0, 255, 0)
            elif np.any(yellow_mask[circle_center[1], circle_center[0]] != 0):
                colors_under_circles.append("U")
                color = (0, 255, 255)
            else:
                colors_under_circles.append("D")
                color = (255, 255, 255)

            cv2.circle(frame, circle_center, 10, color, -1)

            print(filename + ": " + camera + str(colors_under_circles))

    # auf True setzen für Debug
    if False:
        cv2.imshow("Circles on Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



    # auf True setzen für Debug
    if True:
        fakeReturn = []

        if camera == "camera1":
            fakeReturn.append("B")
            fakeReturn.append("R")
            fakeReturn.append("L")
            fakeReturn.append("L")
            fakeReturn.append("U")
            fakeReturn.append("F")
            fakeReturn.append("L")
            fakeReturn.append("D")
            fakeReturn.append("R")
            fakeReturn.append("B")
            fakeReturn.append("U")
            fakeReturn.append("U")
            fakeReturn.append("U")
            fakeReturn.append("R")
            fakeReturn.append("L")
            fakeReturn.append("D")
            fakeReturn.append("U")
            fakeReturn.append("F")
            fakeReturn.append("U")
            fakeReturn.append("R")
            fakeReturn.append("D")
            fakeReturn.append("D")
            fakeReturn.append("F")
            fakeReturn.append("B")
            fakeReturn.append("L")
            fakeReturn.append("L")
            fakeReturn.append("F")
        else:
            fakeReturn.append("D")
            fakeReturn.append("F")
            fakeReturn.append("L")
            fakeReturn.append("L")
            fakeReturn.append("D")
            fakeReturn.append("R")
            fakeReturn.append("R")
            fakeReturn.append("F")
            fakeReturn.append("R")
            fakeReturn.append("R")
            fakeReturn.append("U")
            fakeReturn.append("F")
            fakeReturn.append("B")
            fakeReturn.append("L")
            fakeReturn.append("F")
            fakeReturn.append("F")
            fakeReturn.append("B")
            fakeReturn.append("B")
            fakeReturn.append("B")
            fakeReturn.append("B")
            fakeReturn.append("U")
            fakeReturn.append("D")
            fakeReturn.append("B")
            fakeReturn.append("D")
            fakeReturn.append("U")
            fakeReturn.append("R")
            fakeReturn.append("D")

        return fakeReturn
    else:
        return colors_under_circles

