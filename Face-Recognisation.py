import cv2

# Load the Haar Cascade file
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Read the input image
image = cv2.imread('1.png')   # Make sure image is in same folder

# Check if image loaded properly
if image is None:
    print("Error: Image not found!")
    exit()

# Resize the image
img = cv2.resize(image, None, fx=0.3, fy=0.3)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5
)

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show the output
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
