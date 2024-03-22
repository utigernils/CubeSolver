import Main as app
import numpy as np

app.web_folder = '../web'
app.initial_window_size = (1200, 800)
app.thread_running = False

app.motor.serial_port = "COM5"
app.MachineCom = "COM2"
app.cube.activeCamera = "camera1"
app.CheckRate = "1"

app.machineBusy = False

app.selftestState = "Noch kein Selbsttest durchgeführt."
app.calibrationState = "Noch keine Kalibration durchgeführt."
app.machineState = "Status - Nicht verbunden"
app.solveState = "Noch keine Lösung durchgeführt."

app.standard_IdleColor = "rgb(20, 100, 255)"
app.standard_ScanColor = "rgb(255, 255, 255)"
app.standard_SolveColor = "rgb(255, 255, 50)"
app.standard_DoneColor = "rgb(20, 255, 20)"

app.standard_IdleAnimation = "glow"
app.standard_ScanAnimation = "static"
app.standard_SolveAnimation = "chase"
app.standard_DoneAnimation = "glow"

app.IdleColor = "rgb(20, 100, 255)"
app.ScanColor = "rgb(255, 255, 255)"
app.SolveColor = "rgb(255, 255, 50)"
app.DoneColor = "rgb(20, 255, 20)"

app.IdleAnimation = "glow"
app.ScanAnimation = "static"
app.SolveAnimation = "chase"
app.DoneAnimation = "glow"

app.CameraMask = "red"

app.standard_lower_red = np.array([0, 93, 50])
app.standard_upper_red = np.array([8, 209, 153])
app.standard_lower_blue = np.array([78, 99, 76])
app.standard_upper_blue = np.array([146, 176, 162])
app.standard_lower_orange = np.array([6, 99, 133])
app.standard_upper_orange = np.array([12, 194, 187])
app.standard_lower_green = np.array([32, 33, 33])
app.standard_upper_green = np.array([86, 175, 153])
app.standard_lower_yellow = np.array([17, 136, 137])
app.standard_upper_yellow = np.array([90, 216, 203])

app.lower_red = np.array([0, 93, 50])
app.upper_red = np.array([8, 209, 153])
app.lower_blue = np.array([78, 99, 76])
app.upper_blue = np.array([146, 176, 162])
app.lower_orange = np.array([6, 99, 133])
app.upper_orange = np.array([12, 194, 187])
app.lower_green = np.array([32, 33, 33])
app.upper_green = np.array([86, 175, 153])
app.lower_yellow = np.array([17, 136, 137])
app.upper_yellow = np.array([90, 216, 203])

app.cube.lower_red = np.array([0, 93, 50])
app.cube.upper_red = np.array([8, 209, 153])
app.cube.lower_blue = np.array([78, 99, 76])
app.cube.upper_blue = np.array([146, 176, 162])
app.cube.lower_orange = np.array([6, 99, 133])
app.cube.upper_orange = np.array([12, 194, 187])
app.cube.lower_green = np.array([32, 33, 33])
app.cube.upper_green = np.array([86, 175, 153])
app.cube.lower_yellow = np.array([17, 136, 137])
app.cube.upper_yellow = np.array([90, 216, 203])

app.Start()
