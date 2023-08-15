import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

class CalculateFinger(HandDetector):

    def __init__(self, detectionCon,  maxHands, camera) -> None:
        super().__init__(detectionCon, maxHands)
        self.camera = camera
        self.detector = HandDetector(detectionCon=detectionCon, maxHands=maxHands)
        self.cap = cv2.VideoCapture(camera)
        self.fingerTips = [8, 12, 16, 20]
        self.thumb = 4
        self.leftFingerOpen = []
        self.rightFingerOpen = []
        self.totalFingers = 0

    async def CountFingers(self):
        success, self.frame = self.cap.read()
        hands, img = self.detector.findHands(self.frame, flipType=True)

        if hands:
            hand = hands[0]
            lmList = hand['lmList']
            handtype = hand['type']
            
            open_fingers = []
            if handtype == 'Left':
                if lmList[self.thumb][0] < lmList[self.thumb - 1][0]:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)
            else:
                if lmList[self.thumb][0] > lmList[self.thumb - 1][0]:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)

            for tip in self.fingerTips:
                if lmList[tip][1] < lmList[tip - 2][1]:
                    open_fingers.append(1)
                else:
                    open_fingers.append(0)

            if len(hands) == 2:
                hand2 = hands[1]
                lmList2 = hand2['lmList']
                handtype2 = hand2['type']

                open_fingers2 = []
                if handtype2 == 'Left':
                    if lmList2[self.thumb][0] < lmList2[self.thumb - 1][0]:
                        open_fingers2.append(1)
                    else:
                        open_fingers2.append(0)
                else:
                    if lmList2[self.thumb][0] > lmList2[self.thumb - 1][0]:
                        open_fingers2.append(1)
                    else:
                        open_fingers2.append(0)

                for tip in self.fingerTips:
                    if lmList2[tip][1] < lmList2[tip - 2][1]:
                        open_fingers2.append(1)
                    else:
                        open_fingers2.append(0)

                self.totalFingers = open_fingers2.count(1) + open_fingers.count(1)

                cv2.putText(
                    self.frame, f'fingers: {self.totalFingers}', (5, 50), cv2.FONT_HERSHEY_PLAIN, 4.0, (255, 0, 100), thickness=4
                )

