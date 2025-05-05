import face_recognition

def compare_faces(file1, file2, tolerance=0.6):
    try:
        # Load images from uploaded files
        image1 = face_recognition.load_image_file(file1)
        image2 = face_recognition.load_image_file(file2)

        # Get face encodings (like vector fingerprints of faces)
        encodings1 = face_recognition.face_encodings(image1)
        encodings2 = face_recognition.face_encodings(image2)

        # If face not detected in either image, return False
        if not encodings1 or not encodings2:
            return False

        # Compare the two face encodings
        result = face_recognition.compare_faces([encodings1[0]], encodings2[0], tolerance)

        return result[0]  # True if match, False if not

    except Exception as e:
        print(f"Error during face comparison: {e}")
        return False
