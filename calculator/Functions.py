import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

class Functions:
    def __init__(self) -> None:
        self.number = []
        self.numbers = []
        self.wholeNum = ""
        self.operatoredNumber = 0

    # count number that include how many fingers were up 
    async def CountOneNumber(self, fingersUp):
        if cv2.waitKey(1) == ord(" "):
            self.number.append(fingersUp)
            print(self.number)

        
    # we need some numbers so I add variable number in another list so we can have multipe numbers
    async def AppendNumbersAndPrintWholeNumber(self):
        if cv2.waitKey(2) == ord("n"):
            for num in self.number:
                self.wholeNum += str(num)
            self.numbers.append(int(self.wholeNum))

            print(self.numbers, self.wholeNum)
            self.number = []
            self.wholeNum = ""

    # Sum numbers that in list(numbers)
    async def Sum(self):
        if cv2.waitKey(2) == ord("+"):
            self.operatoredNumber = sum(self.numbers)
            print(self.operatoredNumber)
            self.numbers.clear()
            self.numbers.append(self.operatoredNumber)


    # Substract numbers that in list(numbers)
    async def Subtract(self):
        if cv2.waitKey(2) == ord("-"):
            for num in range (1, len(self.numbers)):
                self.numbers[0] -= self.numbers[num]
            self.operatoredNumber = self.numbers[0]
            print(self.operatoredNumber)
            self.numbers.clear()
            self.numbers.append(self.operatoredNumber)
    
    # Multiply numbers that in list(numbers)
    async def Multiply(self):
        if cv2.waitKey(2) == ord("*"):
            self.operatoredNumber = 1
            for num in self.numbers:
                self.operatoredNumber *= num
            
            print(self.operatoredNumber)
            self.numbers.clear()
            self.numbers.append(self.operatoredNumber)

    # Divide numbers that in list(numbers)
    async def Divide(self):
        if cv2.waitKey(2) == ord("/"):
            for num in range (1, len(self.numbers)):
                self.numbers[0] /= self.numbers[num]
            self.operatoredNumber = self.numbers[0]
            print(self.operatoredNumber)
            self.numbers.clear()
            self.numbers.append(self.operatoredNumber)

    # Delete numbers from number, numbers, wholeNum, operatoredNumber
    async def Clear(self):
        if cv2.waitKey(2) == ord("c"):
            self.number = []
            self.numbers = []
            self.wholeNum = ""
            self.operatoredNumber = 0
            print(self.number, self.numbers)
            
            
