import cv2
#import numpy
#гаус размытие
if __name__ == '__main__':
    cv2.namedWindow("result")

    cap = cv2.VideoCapture(0)

    while True:
        flag, img = cap.read()
        try:
            img = cv2.GaussianBlur(img, (5, 5), 2)
            cv2.imshow('result', img)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break