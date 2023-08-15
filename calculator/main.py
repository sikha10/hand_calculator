import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from Functions import Functions
from CalculateFingers import CalculateFinger
import asyncio


func = Functions()
calculateFinger = CalculateFinger(detectionCon=0.8, maxHands=2, camera=2)

async def main():
    # jer jerobit yvelaze chqari varinti
    task = calculateFinger.CountFingers()

    task1 = func.CountOneNumber(calculateFinger.totalFingers)

    task2 = func.AppendNumbersAndPrintWholeNumber()

    task3 = func.Sum()

    task4 = func.Subtract()

    task5 = func.Multiply()

    task6 = func.Divide()

    task7 = func.Clear()
    
    await task
    await task1
    await task2
    await task3
    await task4
    await task5
    await task6
    await task7


if __name__=='__main__':
    while True:
        asyncio.run(main())
        cv2.imshow('frame', calculateFinger.frame)

        if cv2.waitKey(5) == ord('q'): 
            break

    calculateFinger.cap.release()
    cv2.destroyAllWindows()