# Automatic Object Border/Outline Detection using Python

https://github.com/AdityaMetkar/Object-Border-Detection/assets/133694021/8678cc0d-c467-4e32-9cb9-706e9651ac27

## Procedure

1. Libraries used are  OpenCV | [Rembg](https://pypi.org/project/rembg/2.0.28/).
2. First we read the input image and select the region of interest (ROI) using `cv2.selectROI()`
   - This function returns us four values `x, y, w, h` that are the coordinates of the bounding box.
   - we use these coordinates to slice the image and get the desired part.
![image](https://github.com/AdityaMetkar/Object-Border-Detection/assets/133694021/69077640-4909-43df-859c-910720ec2a8a)
3. We then `GreyScale` this ROI Image and apply `Thresholding` to convert it into a Binary Channel.
4. On this Thresholded image, we apply contour detection using `cv2.findContours()`
   ![image](https://github.com/AdityaMetkar/Object-Border-Detection/assets/133694021/bc49e5df-6380-486c-91e1-fe2cacf8abab)

5. Finally we have the coordinates of the borders by using the above function.<br>
    - Now we draw these contours on the `Original ROI Image with no background removal`.
    - `Concatenate` it with the input image to read in the first step.

![image](https://github.com/AdityaMetkar/Object-Border-Detection/assets/133694021/7d906267-8c92-44d8-a6e0-c16148b2b861)

:clap: We have successfully detected the borders of the selected object.

### Side Information
- You can use `c` key to continue the program without re-running.
- You can use `q` key to quit the program.


