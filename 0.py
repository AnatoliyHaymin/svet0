import cv2 as cv
import numpy as np
#import video
import math

if __name__ == '__main__':
    cv.namedWindow("result")
    cap = cv.VideoCapture(0)


    hsv_min = np.array((0, 0, 200), np.uint8)
    hsv_max = np.array((132, 255, 255), np.uint8)

    hsv_min1 = np.array((200, 0, 0), np.uint8)
    hsv_max1 = np.array((255, 255, 72), np.uint8)

    hsv_min2 = np.array((0, 200, 0), np.uint8)
    hsv_max2 = np.array((120, 255, 120), np.uint8)

    color_purple = (30, 90, 255)
    color_red = (30, 90, 255)

    color_purple1 = (183, 100, 100)
    color_red1 = (246, 100, 100)

    color_purple2 = (0, 255, 0)
    color_red2 = (0, 255, 0)

    while True:
        flag, img = cap.read()
        img = cv.flip(img, 1)
        try:
            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
            thresh = cv.inRange(hsv, hsv_min, hsv_max)
            thresh1 = cv.inRange(hsv, hsv_min1, hsv_max1)
            thresh2 = cv.inRange(hsv, hsv_min2, hsv_max2)
            contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            contours1, hierarchy1 = cv.findContours(thresh1.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            contours2, hierarchy2 = cv.findContours(thresh2.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

            for cnt in contours0:
                rect = cv.minAreaRect(cnt)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]),int(rect[0][1]))
                area = int(rect[1][0]*rect[1][1])

                edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                usedEdge = edge1
                if cv.norm(edge2) > cv.norm(edge1):
                    usedEdge = edge2

                reference = (1, 0)

                if area > 500:
                    cv.drawContours(img,[box],0, color_purple, 2)
                    cv.circle(img, center, 5, color_red, 2)
                    cv.putText(img, "red-yellow", (center[0]+20, center[1]-20), cv.FONT_HERSHEY_SIMPLEX, 1, color_red, 2)
            cv.imshow('result', img)
            for cnt1 in contours1:
                rect = cv.minAreaRect(cnt1)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]),int(rect[0][1]))
                area = int(rect[1][0]*rect[1][1])

                edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                usedEdge = edge1
                if cv.norm(edge2) > cv.norm(edge1):
                    usedEdge = edge2

                reference = (1, 0)

                if area > 500:
                    cv.drawContours(img,[box],0, color_purple1, 2)
                    cv.circle(img, center, 5, color_red1, 2)
                    cv.putText(img, "blue", (center[0]+20, center[1]-20), cv.FONT_HERSHEY_SIMPLEX, 1, color_red1, 2)
            cv.imshow('result', img)
            for cnt2 in contours2:
                rect = cv.minAreaRect(cnt2)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]),int(rect[0][1]))
                area = int(rect[1][0]*rect[1][1])

                edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                usedEdge = edge1
                if cv.norm(edge2) > cv.norm(edge1):
                    usedEdge = edge2

                reference = (1, 0)

                if area > 500:
                    cv.drawContours(img,[box],0, color_purple2, 2)
                    cv.circle(img, center, 5, color_red2, 2)
                    cv.putText(img, "green", (center[0]+20, center[1]-20), cv.FONT_HERSHEY_SIMPLEX, 1, color_red2, 2)
            cv.imshow('result', img)
        except:
            cap.release()
            raise
        ch = cv.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv.destroyAllWindows()
