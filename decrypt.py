import cv2
def extract_data(image_path, password):
    img = cv2.imread(image_path)
    c = {i: chr(i) for i in range(256)}  # Mapping for all possible values
    message = ""
    n, m, z = 0, 0, 0
    h, w, _ = img.shape
    while True:
        # Get the character from the image
        char_value = img[n, m, z]
        message += c[char_value]
        # Move to the next pixel
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == w:
                m = 0
                n += 1
                if n == h:
                    # Reached the end of the image
                    break
        # Check if the end of the message (password) is reached
        if message.endswith(password):
            # Remove the password from the message
            decrypted_message = message[:-len(password)]
            print(f"Decrypted message: {decrypted_message}")
            return
    print("Incorrect password or no hidden message found.")
if __name__ == "__main__":
    image_path = "output.png"
    password = input("Enter passcode for decryption: ")
    extract_data(image_path, password)
