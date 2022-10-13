import cv2
import numpy
import video

if __name__ == '__main__':
    # создаем окно с именем result
    cv2.namedWindow("result")

    # создаем объект cap для захвата кадров с камеры
    cap = video.create_capture(0)

    while True:
        # захватываем текущий кадр и кладем его в переменную img
        flag, img = cap.read()
        try:
            # меняем цветовую модель на HSV XYZ LAB RGB GRAY
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            img3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img4 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img5 = cv2.GaussianBlur(img, (5, 5), 2)
            img6 = cv2.GaussianBlur(img1, (5, 5), 2)
            img7 = cv2.GaussianBlur(img2, (5, 5), 2)
            img8 = cv2.GaussianBlur(img3, (5, 5), 2)
            img9 = cv2.GaussianBlur(img4, (5, 5), 2)
            # отображаем кадр в окне с именем result
            cv2.imshow('result', img)
            cv2.imshow('result1', img1)
            cv2.imshow('result2', img2)
            cv2.imshow('result3', img3)
            cv2.imshow('result4', img4)
            cv2.imshow('result5', img5)
            cv2.imshow('result6', img6)
            cv2.imshow('result7', img7)
            cv2.imshow('result8', img8)
            cv2.imshow('result9', img9)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()