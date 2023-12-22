def Turn(id, acc, speed, deg):
    output_string = "FA 0" + str(id) + " FD "

    processed_string = hex(speed)[2:].zfill(4)
    processed_string = " ".join(processed_string[i:i + 2] for i in range(0, len(processed_string), 2))

    output_string += processed_string

    output_string += " 0" + str(acc) + " 00 09 "

    deg_hex = hex(deg)[2:].zfill(4)
    deg_hex = " ".join(deg_hex[i:i + 2] for i in range(0, len(deg_hex), 2))

    output_string += deg_hex

    return output_string.upper()

def Solve(solvestring, speed):
    Turn(id, acc, speed, deg)
def SelfTest():
    #motor response test here !!
    print("Running: Motor Selftest")
def SelfCalibrate():
    #motor calibration here !!
    print("Running: Motor Selfcalibration")