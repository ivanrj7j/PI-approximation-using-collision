from Body import Body
from math import log
# importing all the module 


def calculateDeltaTime(body1:Body, body2:Body) -> float:
    """
    Calculates Delta Time based on the number distance between the objects for fastening up the process
    """
    # TODO: Find a mathematical function that greatly makes the small numbers smaller and high numbers look higher
    # current function(not finalized): 
    # deltaTime = log(body1.position-body2.position)
    return 0.0001

def updateValue(body1:Body, body2:Body, piDigits) -> None:
    """
    Adds 1 to the value of piDigits whenver the 
    """
    if body2.isCollidingWall() or body2.isColliding(body1):
        piDigits += 1
        print(f"[PI] {piDigits}", end='\r')
    return piDigits

def simulateFrame(body1:Body, body2:Body, deltaTime:float, piDigits:int):
    """
    Simulates a Frame for calculating the value of PI
    """
    body1.collisionHandle(body2)
    # handling the collision between bodies

    piDigits = updateValue(body1, body2, piDigits)
    # updating the value of pi

    body1.update(deltaTime)
    body2.update(deltaTime)
    # updating both the bodies

    return piDigits
    

def shouldKeepSimulating(body1:Body, body2:Body) -> bool:
    """
    Returns True if the digits are calculated
    """
    return not ( ( (body1.velocity > 0) and (body2.velocity > 0) and (body1.velocity > body2.velocity) ) or (body2.velocity == body1.velocity) )

def simulate(body1:Body, body2:Body) -> int:
    """
    Simulates Physics to calculate the value of PI
    """
    piDigits = 0
    # digits of pi

    print("Simulation Starging.")
    while shouldKeepSimulating(body1, body2):
        deltaTime = calculateDeltaTime(body1, body2)
        piDigits = simulateFrame(body1, body2, deltaTime, piDigits)
        # simulates bodies

    return piDigits


if __name__ == "__main__":

    totalDigits = 6
    # the number of digits to be calculated by the program

    body1 = Body(100**(totalDigits-1), 100, 300, -2)
    body2 = Body(1, 30, 30, 0)
    # initializing the bodies
    
    print("Final value", simulate(body1, body2))
    # simulating the program 