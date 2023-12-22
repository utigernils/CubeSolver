import ReadCube as rc
import SolveCube as sc
import MotorInterface as Motor
import MachineInterface as Machine
import eel

#settings
solvingSpeed = 100
automaticStart = False
ui = False #Beta

web_folder = 'web'

# Set the initial window size
initial_window_size = (1200, 800)

# Initialize Eel
eel.init(web_folder)

def Idle():
    Machine.SetLights(0)
def StartSolve():
    Machine.SetLights(1)
    cubestring = rc.ReadCube()
    Machine.SetLights(2)
    solvestring = sc.SolveCube(cubestring)
    Machine.SetLights(3)
    Motor.Solve(solvestring, solvingSpeed)
    Idle()



@eel.expose
def button_click():
    print("Button Clicked!")


eel.start('index.html', size=initial_window_size, port=8000, mode='chrome', root=web_folder)



