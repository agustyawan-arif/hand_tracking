import cv2
import mediapipe as mp
import time
import argparse

class HandTracker:
    def __init__(self, source):
        if source == "0":  # Camera source
            self.cap = cv2.VideoCapture(0)
        elif isinstance(source, str):  # Video file source
            self.cap = cv2.VideoCapture(source)
        else:
            raise ValueError("Invalid source. Use an integer for camera or a string for video file.")

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.pTime = 0
        self.cTime = 0

        # Define the width and height of the highlighted areas
        self.center_part = [226, 119, 375, 248]
        self.left_part = [87, 69, 172, 141]
        self.right_part = [439, 209, 510, 324]

    def process_frame(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        h, w, c = img.shape

        # Draw frame box
        cv2.rectangle(img, (0, 0), (w, h), (0, 255, 0), 2)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

                # Check if the hand is within the specified areas
                if self.is_in_area(cx, cy, self.center_part):
                    print("Hand is in the center area!")
                    cv2.rectangle(img, (self.center_part[0], self.center_part[1]), (self.center_part[2], self.center_part[3]), (0, 0, 255), 2)

                if self.is_in_area(cx, cy, self.left_part):
                    print("Hand is in the left area!")
                    cv2.rectangle(img, (self.left_part[0], self.left_part[1]), (self.left_part[2], self.left_part[3]), (0, 0, 255), 2)

                if self.is_in_area(cx, cy, self.right_part):
                    print("Hand is in the right area!")
                    cv2.rectangle(img, (self.right_part[0], self.right_part[1]), (self.right_part[2], self.right_part[3]), (0, 0, 255), 2)

    def is_in_area(self, x, y, area):
        return area[0] < x < area[2] and area[1] < y < area[3]

    def run(self):
        while True:
            success, img = self.cap.read()
            if not success:
                break

            self.process_frame(img)

            self.cTime = time.time()
            fps = 1 / (self.cTime - self.pTime)
            self.pTime = self.cTime

            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hand tracking with highlighted areas")
    parser.add_argument("--source", type=str, default="IMG_1114.mp4", help="Path to the video file or camera index (default: IMG_1114.mp4)")
    args = parser.parse_args()

    hand_tracker = HandTracker(args.source)
    hand_tracker.run()
