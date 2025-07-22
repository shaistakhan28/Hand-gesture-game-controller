# Hand-gesture-game-controller
A computer vision-based project that uses hand gestures to control games or trigger specific actions. Built using Python, OpenCV, and MediaPipe, this system detects hand movements via a webcam and translates them into keyboard inputs using PyAutoGUI — enabling touchless, intuitive interaction with PC games or applications.
Can implement on the games like SubwaySurfers or TempleRun and similar games as well.        





# Features
🖐️ Real-time hand gesture detection

🎮 Simulate keyboard inputs to control any PC game

👆 Finger counting and custom gesture mapping

📷 Webcam-based input using OpenCV

🔄 Live flipped feed for intuitive user control

🧠 Modular and easy-to-modify code structure


# How It Works
1)OpenCV captures real-time video from your webcam.

2)MediaPipe identifies 21 hand landmarks (fingertips, joints, etc.).

3)A logic module counts raised fingers or recognizes patterns.

4)PyAutoGUI sends corresponding keyboard events (e.g., arrow keys, spacebar).

5)These actions control any game or app that supports keyboard input.

# Usage
# Gesture                    Action
✊ Fist       ------->       Down

☝ One       -------->        Right

✌ Two Fingers  -------->      Left

🖐 Five Fingers	 -------->      Up
