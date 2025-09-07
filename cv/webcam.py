import cv2
def run_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        # Flip the frame horizontally (mirror effect)
        mirrored_frame = cv2.flip(frame, 1)
        # Display the mirrored video
        cv2.imshow('Mirrored Webcam Feed', mirrored_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting webcam...")
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_webcam()
