import cv2
import rembg

def draw_outline(roi_image, mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(roi_image, contours, -1, (0, 255, 0), 2)

    return img

def main():
    input_path = "YOUR IMAGE PATH"

    while True:

        image = cv2.imread(input_path)
        if image is None:
            print("Error reading the image. Make sure the path is correct.")
            break

        image=cv2.resize(image,(500,500))


        roi = cv2.selectROI(image)
        cv2.destroyAllWindows()

        x, y, w, h = roi
        roi_image = image[y:y+h, x:x+w]

        result_image = rembg.remove(roi_image)
        result_image = cv2.cvtColor(result_image, cv2.COLOR_BGRA2BGR)


        gray = cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        result=draw_outline(roi_image,mask)

        image[y:y+h, x:x+w] = result
        cv2.imshow("Output Image", image)

        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            cv2.destroyAllWindows()
            continue

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
