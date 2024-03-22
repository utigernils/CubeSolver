import eel
import re
import time
import datetime
import threading

import CubeScanner as cube
import SolveCalculator as solve
import MotorInterface as motor

filename = "Main.py"

#Machine actions
def solveCube():
    eel.UserInfo("Würfel wird gelesen und berechnet. Bitte Seite nicht verlassen!")

    colorArray1 = ''.join(cube.scan("camera1"))
    colorArray2 = ''.join(cube.scan("camera2"))

    cubestring = colorArray1 + colorArray2
    #solvestring = sc.SolveCube(cubestring)

    solvestring = 'U3 R2 B2 U2 B3 D3 L1 D1 L2 U2 D2 R3 U1 D1 R3 D1 B3 U1 (18f*)'

    print(filename + ": generatet solve: " + solvestring)

    solve = solvestring.split(" (")[0].split()

    for instruction in solve:
        print(instruction)

        motorAdress = re.split(r'\d+', instruction)[0]
        motorMove = instruction.split(motorAdress)[1]

        match motorAdress:
            case 'D':
                motorAdress = 1
            case 'L':
                motorAdress = 2
            case 'B':
                motorAdress = 3
            case 'R':
                motorAdress = 4
            case 'F':
                motorAdress = 5
            case 'U':
                motorAdress = 6

        match int(motorMove):
            case 1:
                motor.move(motorAdress, 1, 3000, 254, 800)
            case 2:
                motor.move(motorAdress, 1, 3000, 254, 1600)
            case 3:
                motor.move(motorAdress, 0, 3000, 254, 800)

        time.sleep(0.2)

    print('Solve DONE!')

def motorTest():
    try:
        motor.enable('00', True)
        time.sleep(1)

        shortWait = 0.15
        longWait = 0.5
        count = 0
        while count < 5:
            motor.move(1, 1, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(2, 1, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(3, 1, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(4, 1, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(5, 1, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(6, 1, 3000, 254, 1600)
            time.sleep(longWait)
            motor.move(1, 0, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(2, 0, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(3, 0, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(4, 0, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(5, 0, 3000, 254, 1600)
            time.sleep(shortWait)
            motor.move(6, 0, 3000, 254, 1600)
            time.sleep(longWait)
            motor.move(0, 0, 3000, 254, 800)
            time.sleep(shortWait)
            motor.move(0, 1, 3000, 254, 800)
            time.sleep(shortWait)
            motor.move(0, 0, 3000, 254, 800)
            time.sleep(shortWait)
            motor.move(0, 1, 3000, 254, 800)
            time.sleep(shortWait)
            motor.move(0, 0, 3000, 254, 800)
            time.sleep(shortWait)
            motor.move(0, 1, 3000, 254, 800)
            time.sleep(longWait)
            count += 1

            time.sleep(1)
            motor.enable('00', False)
    except:
        print("MotorInterface: Invalid com Port")
        eel.UserInfo("MotorInterface Error: Wrong com Port")

def motorCalibration():
    motor.calibrate('00')

#Thread routines
def dashboardThread():
    while thread_running:
        print(filename + ": getting Machine state")
        eel.UpdateText('selftest-state', selftestState)
        eel.UpdateText('calibration-state', calibrationState)
        time.sleep(float(CheckRate))

def cameraThread():
    while thread_running:
        variable_Upper = "upper_" + CameraMask
        variable_Lower = "lower_" + CameraMask
        time.sleep(0.04)
        eel.refresh_img(cube.getMaskedFrame(globals()[variable_Upper], globals()[variable_Lower], cube.activeCamera))

#Threading functions
def startThread(function):
    global thread_running
    thread_running = True
    thread = threading.Thread(target=function)
    thread.start()

def stopThread():
    global thread_running
    thread_running = False

#Ui backbone
def updateCameraSliders():
    eel.set_camera_Mask_select(CameraMask)

    global lower_red, upper_red, lower_blue, upper_blue, lower_orange, upper_orange, lower_green, upper_green,lower_yellow, upper_yellow

    variable_Upper = "upper_" + CameraMask
    variable_Lower = "lower_" + CameraMask

    eel.set_camera_UpperHue_slider(int(globals()[variable_Upper][0]))
    eel.set_camera_UpperSaturation_slider(int(globals()[variable_Upper][1]))
    eel.set_camera_UpperBrightness_slider(int(globals()[variable_Upper][2]))

    eel.set_camera_LowerHue_slider(int(globals()[variable_Lower][0]))
    eel.set_camera_LowerSaturation_slider(int(globals()[variable_Lower][1]))
    eel.set_camera_LowerBrightness_slider(int(globals()[variable_Lower][2]))

@eel.expose
def home_loaded():
    print(filename + ": 'home' loaded.")

    stopThread()
    time.sleep(1)
    startThread(dashboardThread)

@eel.expose
def home_AutostartOn_btn():
    print(filename + ": 'home_AutostartOn' pressed.")

@eel.expose
def home_AutostartOff_btn():
    print(filename + ": 'home_AutostartOff' pressed.")

@eel.expose
def home_Solve_btn():
    print(filename + ": 'home_Solve' pressed.")
    solveCube()

@eel.expose
def home_SelfTest_btn():
    global selftestState
    print(filename + ": 'home_SelfTest' pressed.")

    selftestState = "Selbsttest läuft..."

    motorTest()

    selftestState = 'Letzter Selbsttest: ' + datetime.datetime.now().strftime('%H:%M')

@eel.expose
def home_Calibration_btn():
    global calibrationState
    print(filename + ": 'home_Calibration' pressed.")

    calibrationState = "Kalibration läuft..."

    motorCalibration()
    time.sleep(5)

    calibrationState = 'Letzte Kalibration: ' + datetime.datetime.now().strftime('%H:%M')

#Camera
@eel.expose
def camera_loaded():
    print(filename + ": 'camera' loaded.")
    updateCameraSliders()
    stopThread()
    time.sleep(1)
    startThread(cameraThread)

@eel.expose
def camera_Reset_btn():
    print(filename + ": 'camera_Reset' pressed.")

    variable_Upper = "upper_" + CameraMask
    variable_Lower = "lower_" + CameraMask

    standard_Upper = "standard_upper_" + CameraMask
    standard_Lower = "standard_lower_" + CameraMask

    globals()[variable_Upper][0] = int(globals()[standard_Upper][0])
    globals()[variable_Upper][1] = int(globals()[standard_Upper][1])
    globals()[variable_Upper][2] = int(globals()[standard_Upper][2])

    globals()[variable_Lower][0] = int(globals()[standard_Lower][0])
    globals()[variable_Lower][1] = int(globals()[standard_Lower][1])
    globals()[variable_Lower][2] = int(globals()[standard_Lower][2])

    updateCameraSliders()

    print(filename + ": reseted '" + variable_Upper + "' and '" + variable_Lower + "'." )

@eel.expose
def camera_Set_btn():
    print(filename + ": 'camera_Set' pressed.")
    cube.updateMasks(lower_red, upper_red, lower_blue, upper_blue, lower_orange, upper_orange, lower_green, upper_green, lower_yellow, upper_yellow)

@eel.expose
def camera_SwitchCamera_btn():
    print(filename + ": 'camera_SwitchCamera' pressed.")
    if cube.activeCamera == "camera1":
        cube.activeCamera = "camera2"
        print(filename + ": switched to Camera2")
    else:
        cube.activeCamera = "camera1"
        print(filename + ": switched to Camera1")

@eel.expose
def camera_Mask_select(value):
    global CameraMask
    CameraMask = value
    updateCameraSliders()
    print(filename + ": 'camera_Mask' selected '" + value + "'.")

@eel.expose
def camera_UpperHue_slider(value):
    variable_Upper = "upper_" + CameraMask

    globals()[variable_Upper][0] = int(value)
    print(filename + ": 'camera_UpperHue' set to '" + value + "'.")

@eel.expose
def camera_LowerHue_slider(value):
    variable_Lower = "lower_" + CameraMask

    globals()[variable_Lower][0] = int(value)
    print(filename + ": 'camera_LowerHue' set to '" + value + "'.")

@eel.expose
def camera_UpperSaturation_slider(value):
    variable_Upper = "upper_" + CameraMask

    globals()[variable_Upper][1] = int(value)
    print(filename + ": 'camera_UpperSaturation' set to '" + value + "'.")

@eel.expose
def camera_LowerSaturation_slider(value):
    variable_Lower = "lower_" + CameraMask

    globals()[variable_Lower][1] = int(value)
    print(filename + ": 'camera_LowerSaturation' set to '" + value + "'.")

@eel.expose
def camera_UpperBrightness_slider(value):
    variable_Upper = "upper_" + CameraMask

    globals()[variable_Upper][2] = int(value)
    print(filename + ": 'camera_UpperBrightness' set to '" + value + "'.")

@eel.expose
def camera_LowerBrightness_slider(value):
    variable_Lower = "lower_" + CameraMask

    globals()[variable_Lower][2] = int(value)
    print(filename + ": 'camera_LowerBrightness' set to '" + value + "'.")

#Light's
@eel.expose
def lights_loaded():
    eel.set_lights_AnimationIdle_select(IdleAnimation)
    eel.set_lights_AnimationScanning_select(ScanAnimation)
    eel.set_lights_AnimationSolving_select(SolveAnimation)
    eel.set_lights_AnimationDone_select(DoneAnimation)

    eel.set_lights_ColorIdle_color(IdleColor)
    eel.set_lights_ColorScanning_color(ScanColor)
    eel.set_lights_ColorSolving_color(SolveColor)
    eel.set_lights_ColorDone_color(DoneColor)
    print(filename + ": 'lights' loaded.")

@eel.expose
def lights_ResetIdle_btn():
    global IdleColor
    global IdleAnimation
    global standard_IdleColor
    global standard_IdleAnimation
    IdleColor = standard_IdleColor
    IdleAnimation = standard_IdleAnimation
    lights_loaded()
    print(filename + ": 'lights_ResetIdle' pressed.")

@eel.expose
def lights_SetIdle_btn():
    print(filename + ": 'lights_SetIdle' pressed.")

@eel.expose
def lights_ResetScanning_btn():
    global ScanColor
    global ScanAnimation
    global standard_ScanColor
    global standard_ScanAnimation
    ScanColor = standard_ScanColor
    ScanAnimation = standard_ScanAnimation
    lights_loaded()
    print(filename + ": 'lights_ResetScanning' pressed.")

@eel.expose
def lights_SetScanning_btn():
    print(filename + ": 'lights_SetScanning' pressed.")

@eel.expose
def lights_ResetSolving_btn():
    global SolveColor
    global SolveAnimation
    global standard_SolveColor
    global standard_SolveAnimation
    SolveColor = standard_SolveColor
    SolveAnimation = standard_SolveAnimation
    lights_loaded()
    print(filename + ": 'lights_ResetSolving' pressed.")

@eel.expose
def lights_SetSolving_btn():
    print(filename + ": 'lights_SetSolving' pressed.")

@eel.expose
def lights_ResetDone_btn():
    global DoneColor
    global DoneAnimation
    global standard_DoneColor
    global standard_DoneAnimation
    DoneColor = standard_DoneColor
    DoneAnimation = standard_DoneAnimation
    lights_loaded()
    print(filename + ": 'lights_ResetDone' pressed.")

@eel.expose
def lights_SetDone_btn():
    print(filename + ": 'lights_SetDone' pressed.")

@eel.expose
def lights_AnimationIdle_select(value):
    global IdleAnimation
    IdleAnimation = value
    print(filename + ": 'lights_AnimationIdle' selected '" + value + "'.")

@eel.expose
def lights_AnimationScanning_select(value):
    global ScanAnimation
    ScanAnimation = value
    print(filename + ": 'lights_AnimationScanning' selected '" + value + "'.")

@eel.expose
def lights_AnimationSolving_select(value):
    global SolveAnimation
    SolveAnimation = value
    print(filename + ": 'lights_AnimationSolving' selected '" + value + "'.")

@eel.expose
def lights_AnimationDone_select(value):
    global DoneAnimation
    DoneAnimation = value
    print(filename + ": 'lights_AnimationDone' selected '" + value + "'.")

@eel.expose
def lights_ColorIdle_color(value):
    global IdleColor
    IdleColor = value
    print(filename + ": 'lights_ColorIdle' set Color '" + value + "'.")

@eel.expose
def lights_ColorScanning_color(value):
    global ScanColor
    ScanColor = value
    print(filename + ": 'lights_ColorScanning' set Color '" + value + "'.")

@eel.expose
def lights_ColorSolve_color(value):
    global SolveColor
    SolveColor = value
    print(filename + ": 'lights_ColorSolve' set Color '" + value + "'.")

@eel.expose
def lights_ColorDone_color(value):
    global DoneColor
    DoneColor = value
    print(filename + ": 'lights_ColorDone' set Color '" + value + "'.")

#Settings
@eel.expose
def settings_loaded():
    eel.set_settings_MotorCom_select(MotorCom)
    eel.set_settings_MachineCom_select(MachineCom)
    eel.set_settings_CheckRate_select(CheckRate)
    print(filename + ": 'settings' loaded.")

@eel.expose
def settings_MotorCom_select(value):
    global MotorCom
    MotorCom = value
    motor.serial_port = value
    print(filename + ": 'settings_MotorCom' selected '" + value + "'.")

@eel.expose
def settings_MachineCom_select(value):
    global MachineCom
    MachineCom = value
    print(filename + ": 'settings_MachineCom' selected '" + value + "'.")

@eel.expose
def settings_CheckRate_select(value):
    global CheckRate
    CheckRate = value
    print(filename + ": 'settings_CheckRate' selected '" + value + "'.")

@eel.expose
def settings_Save_btn():
    print(filename + ": 'settings_Save' pressed.")

def Start():
    eel.init(web_folder)
    eel.start('index.html', size=initial_window_size, port=8000, mode='chrome', root=web_folder)
    print(filename + ": 'eel' started.")




