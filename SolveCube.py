import optimal.solver as sv
import GenerateMotorControls as gm

def runMotors(motor_controls):
    motor_controls_uart = []

    for control in motor_controls:
        splited = control.split(":")
        motor_controls_uart.append(gm.convertToUart(int(splited[0]), 5, 500, int(splited[1])))

    for command in motor_controls_uart:
        print(command)
def solve(cubestring):
    solve = sv.solve(cubestring)
    motor_controls = gm.convertToMotorCrtl(solve)
    runMotors(motor_controls)

