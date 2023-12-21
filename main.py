import ReadCube as rc
import SolveCube as sc
import MotorInterface as Motor
import MachineInterface as Machine

#settings
solvingSpeed = 100
automaticStart = False

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

while True:
    if rc.CheckCube() & automaticStart:
        StartSolve()