import cv2
import face_recognition

# Load your image
your_image = face_recognition.load_image_file("path/to/your/image.jpg")
your_face_encoding = face_recognition.face_encodings(your_image)[0]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Check if the face matches the registered face
        match = face_recognition.compare_faces([your_face_encoding], face_encoding)

        if match[0]:
            print("You are Verified")
            cv2.destroyAllWindows()  # Close the window
            video_capture.release()  # Release webcam
            exit()  # Exit the program

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the loop by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
