import optimal.solver as sv

cubestring = 'LBURUDDFBRBFURUBLBFLURFFDLLLUUDDDBDRUBRBLFDRFRUFRBLDFL'

def convertToMotorCrtl(input_string):
    motor_mapping = {'F': '1', 'R': '2', 'B': '3', 'L': '4', 'U': '5', 'D': '6'}
    result = []

    tokens = input_string.split()

    for token in tokens:
        if len(token) < 2:
            continue

        direction = token[0]
        if direction not in motor_mapping:
            continue

        steps = int(token[1])

        motor = motor_mapping[direction]

        result.append(f"{motor}:{steps * 90}")

    return result

def convertToUart(id, acc, speed, deg):
    output_string = "FA 0" + str(id) + " FD "

    processed_string = hex(speed)[2:].zfill(4)
    processed_string = " ".join(processed_string[i:i + 2] for i in range(0, len(processed_string), 2))

    output_string += processed_string

    output_string += " 0" + str(acc) + " 00 09 "

    deg_hex = hex(deg)[2:].zfill(4)
    deg_hex = " ".join(deg_hex[i:i + 2] for i in range(0, len(deg_hex), 2))

    output_string += deg_hex

    return output_string.upper()

solvedString = sv.solve(cubestring)
motor_controls = convertToMotorCrtl(solvedString)

motor_controls_uart = []

for control in motor_controls:
    splited = control.split(":")
    motor_controls_uart.append(convertToUart(int(splited[0]), 5, 500, int(splited[1])))

print("\nInput Cube:")
print("\t" + cubestring)

print("\nSolving steps:")
print("\t" + solvedString)

print("\nMotor controls (lesbar):")
for control in motor_controls:
    print("\t" + control)

print("\nMotor controls (Uart):")
for control in motor_controls_uart:
    print("\t" + control)