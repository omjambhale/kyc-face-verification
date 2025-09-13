# KYC Face Verification

verify if a government ID photo matches your selfie.

## Demo
- Upload ID
- Upload Selfie
- Click "Verify"
- Result displayed instantly

## Features
- Drag-and-drop file upload
- Supports JPG, JPEG, PNG
- Side-by-side image preview
- Quick face verification
- Works offline with Streamlit

## Tech Stack
- Python
- Streamlit (Web UI)
- face_recognition / dlib (Face verification)
- OpenCV / Pillow (Image handling)

## Quickstart
```bash
git clone https://github.com/username/kyc-face-verification.git
cd kyc-face-verification
pip install -r requirements.txt
streamlit run app.py
