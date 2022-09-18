import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)

detector = HandDetector(detectionCon=0.8, maxHands=2)
finger_tips = [8, 12, 16, 20]
thumb = 4

while True:
    success, frame = cap.read()
    hands, img = detector.findHands(frame, flipType=True)
    left_finger_open = []
    right_finger_open = []

    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        handtype = hand['type']

        open_fingers = []
        if handtype == 'Left':
            if lmList[thumb][0] < lmList[thumb - 1][0]:
                open_fingers.append(1)
            else:
                open_fingers.append(0)
        else:
            if lmList[thumb][0] > lmList[thumb - 1][0]:
                open_fingers.append(1)
            else:
                open_fingers.append(0)

        for tip in finger_tips:
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
                if lmList2[thumb][0] < lmList2[thumb - 1][0]:
                    open_fingers2.append(1)
                else:
                    open_fingers2.append(0)
            else:
                if lmList2[thumb][0] > lmList2[thumb - 1][0]:
                    open_fingers2.append(1)
                else:
                    open_fingers2.append(0)

            for tip in finger_tips:
                if lmList2[tip][1] < lmList2[tip - 2][1]:
                    open_fingers2.append(1)
                else:
                    open_fingers2.append(0)

            total_fingers = open_fingers2.count(1) + open_fingers.count(1)

            cv2.putText(
                frame, f'fingers: {total_fingers}', (5, 50), cv2.FONT_HERSHEY_PLAIN, 4.0, (255, 0, 100), thickness=4
            )

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
