import ReadCube as rc
import SolveCube as sc
import MotorInterface as Motor
import MachineInterface as Machine

#configuration
solvingSpeed = 10

while True:

    if rc.CheckCube():
        Machine.SetLights(1)
        cubestring = rc.ReadCube()
        Machine.SetLights(2)
        solvestring = sc.SolveCube(cubestring)
        Machine.SetLights(3)
        break
    else:
        cubestring = rc.ReadCube()

