import serial

filename = "MotorInterface.py"
def sendHex(serial_port, hex_string):
    ser = serial.Serial(serial_port, baudrate=38400, timeout=1)

    hex_bytes = bytes.fromhex(hex_string)
    checksum = sum(hex_bytes) & 0xFF
    hex_bytes_with_checksum = hex_bytes + bytes([checksum])

    ser.write(hex_bytes_with_checksum)
    print(filename + f": Sent: {hex_bytes_with_checksum}")

    ser.close()

def calibrate(motor_addres):
    sendHex(serial_port, 'FA' + motor_addres + '8000')

def enable(motor_addres, state):
    if state:
        state = '01'
    else:
        state = '00'

    sendHex(serial_port, 'FA' + motor_addres + 'F3' + state)

def move(addr, dir, speed, acc, pulses):
    speed_byte4 = format(speed & 0xFF, '02X')
    speed_byte5 = format((speed >> 8) & 0xFF, '01X')
    acc_byte = format(acc, '02X')
    pulses_bytes = format(pulses, '08X')

    if dir == 1:
        dir = 8

    print(filename + f": dir_bit: {dir}")
    print(filename + f": speed_byte4: {speed_byte4}")
    print(filename + f": speed_byte5: {speed_byte5}")
    print(filename + f": acc_byte: {acc_byte}")
    print(filename + f": pulses_bytes: {pulses_bytes}")

    hex_string = f'FA{addr:02X}FD{dir}{speed_byte5}{speed_byte4}{acc_byte}{pulses_bytes}'

    print(filename + f": generated moveString: " + hex_string)
    sendHex(serial_port, hex_string)