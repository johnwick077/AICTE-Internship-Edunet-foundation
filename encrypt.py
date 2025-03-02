import cv2
import os
def embed_data(image_path, msg, password):
    img = cv2.imread(image_path)
    d = {chr(i): i for i in range(256)}  # Mapping for all possible characters
    msg += password # Append the password to the message
    h, w, _ = img.shape
    total_values = h * w * 3
    if len(msg) > total_values:
        raise ValueError("Message is too long to fit in the image.")
    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        # Move to the next pixel
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == w:
                m = 0
                n += 1
    cv2.imwrite("output.png", img)
    os.system("start output.png")  # Use 'start' to open the image on Windows
    print("Message embedded successfully.")
if __name__ == "__main__":
    image_path = "input.png"  # Replace with your image file
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    embed_data(image_path, msg, password)
