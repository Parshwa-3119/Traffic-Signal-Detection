import cv2
import numpy as np
import pyttsx3
import threading

# Text-to-speech function (asynchronous)
def speak_async(text):
    tts_thread = threading.Thread(target=speak, args=(text,))
    tts_thread.start()

# Function to handle text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to detect the traffic light color and green arrow
def detect_traffic_light_color_and_arrow(roi):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define HSV ranges for red, yellow, and green colors
    red_lower1 = np.array([0, 100, 100], np.uint8)
    red_upper1 = np.array([10, 255, 255], np.uint8)
    red_lower2 = np.array([170, 100, 100], np.uint8)
    red_upper2 = np.array([180, 255, 255], np.uint8)

    yellow_lower = np.array([20, 100, 100], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)

    green_lower = np.array([35, 50, 50], np.uint8)
    green_upper = np.array([85, 255, 255], np.uint8)

    # Blur the region to reduce noise
    blurred = cv2.GaussianBlur(hsv, (5, 5), 0)

    # Create masks for each color
    red_mask1 = cv2.inRange(blurred, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(blurred, red_lower2, red_upper2)
    red_mask = cv2.add(red_mask1, red_mask2)
    yellow_mask = cv2.inRange(blurred, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(blurred, green_lower, green_upper)

    # Use morphological operations to clean the masks
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)

    # Minimum pixel threshold to avoid false detections
    pixel_threshold = 1500

    # Function to check if the mask has significant pixels
    def valid_detection(mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > pixel_threshold:
                return True, contours
        return False, None

    # Check if green light is detected and then check for arrow
    is_green, green_contours = valid_detection(green_mask)
    if is_green:
        # Convert the green mask to a binary image for contour detection
        for contour in green_contours:
            approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
            if len(approx) >= 5:  # Checking for an arrow-like shape
                # Get the bounding rectangle to analyze the arrow's direction
                x, y, w, h = cv2.boundingRect(approx)
                
                # Use the aspect ratio to differentiate between left and right arrows 
                if w > h:  # Arrow is pointing horizontally 
                    if approx[0][0][0] < approx[-1][0][0]:  # Arrow points to the right
                        return "Green Right Arrow"
                    else:  # Arrow points to the left
                        return "Green Left Arrow"
        return "Green"
    elif valid_detection(red_mask)[0]:
        return "Red"
    elif valid_detection(yellow_mask)[0]:
        return "Yellow"
    else:
        return "No Color"

# Function to process video and detect traffic light
def process_video():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    frame_skip = 5  # Skip frames to reduce lag
    frame_count = 0

    no_color_count = 0  # Counter for "No traffic light detected"
    max_no_color_repeat = 3  # Max times to repeat "No traffic light detected"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue  # Skip frames to reduce lag

        # Define region of interest (ROI) for traffic light detection
        roi_light = frame[100:300, 200:400]  # Adjust ROI based on your camera's position

        # Detect traffic light color and arrow
        light_color = detect_traffic_light_color_and_arrow(roi_light)

        # Map color to speech commands
        if light_color == "Red":
            speak_async("Stop")
            no_color_count = 0  # Reset no color count
        elif light_color == "Yellow":
            speak_async("Wait")
            no_color_count = 0
        elif light_color == "Green":
            speak_async("Go")
            no_color_count = 0
        elif light_color == "Green Right Arrow":
            speak_async("Right signal is green")
            no_color_count = 0
        elif light_color == "Green Left Arrow":
            speak_async("Left signal is green")
            no_color_count = 0
        elif light_color == "No Color":
            if no_color_count < max_no_color_repeat:
                speak_async("No traffic light detected")
                no_color_count += 1
        else:
            no_color_count = 0  # Reset if any color detected

        # Display the result on the screen
        cv2.putText(frame, f"Light: {light_color}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (200, 100), (400, 300), (255, 0, 0), 2)  # ROI rectangle for traffic light

        # Show the frame
        cv2.imshow("Traffic Light and Arrow Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the video processing in the main thread
process_video()
