import cv2
import mediapipe as mp
import pyautogui


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def count_raised_fingers(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    count = 0

   
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        count += 1

   
    for i in range(1, 5):
        if hand_landmarks.landmark[tips_ids[i]].y < hand_landmarks.landmark[tips_ids[i] - 2].y:
            count += 1

    return count

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            finger_count = count_raised_fingers(handLms)

            if finger_count == 5:
                cv2.putText(frame, "jump (5 fingers)", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                pyautogui.keyDown("up")
                
            elif finger_count == 0:
                cv2.putText(frame, "Roll (0 fingers)", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                pyautogui.keyDown("down")
                
            elif finger_count == 1:
                cv2.putText(frame, "Lean Left (1 finger)", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                pyautogui.keyDown("left")
                
            elif finger_count == 2:
                cv2.putText(frame, "Lean Right (2 fingers)", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                pyautogui.keyDown("right")
                
            else:
               
                cv2.putText(frame, "Neutral", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyUp("left")
                pyautogui.keyUp("right")
    else:
        pyautogui.keyUp("up")
        pyautogui.keyUp("down")
        pyautogui.keyUp("left")
        pyautogui.keyUp("right")

    cv2.imshow("Finger Count Controller", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
