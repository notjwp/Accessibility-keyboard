import cv2

def run_webcam():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Camera initialized at {int(actual_width)}x{int(actual_height)} @ {int(actual_fps)} FPS")
    print("Press 'q' to quit.")

    display_width = 640
    display_height = 360

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        mirrored_frame = cv2.flip(frame, 1)
        display_frame = cv2.resize(mirrored_frame, (display_width, display_height))
        cv2.imshow('Mirrored Webcam Feed (Smaller Window)', display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting webcam...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_webcam()
