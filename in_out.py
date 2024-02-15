import cv2
import pygame
import numpy as np
from datetime import datetime


def in_out():
    video = cv2.VideoCapture(1)
    faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    pygame.init()
    window = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Face Detection App")
    img = pygame.image.load("bgimg1.png").convert()
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
             x1, y1 = x + w, y + h
             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
             cv2.line(frame, (x, y), (x + 30, y), (0, 0, 255), 6)  # Top Left
             cv2.line(frame, (x, y), (x, y + 30), (0, 0, 255), 6)

             cv2.line(frame, (x1, y), (x1 - 30, y), (0, 0, 255), 6)  # Top Right
             cv2.line(frame, (x1, y), (x1, y + 30), (0, 0, 255), 6)

             cv2.line(frame, (x, y1), (x + 30, y1), (0, 0, 255), 6)  # Bottom Left
             cv2.line(frame, (x, y1), (x, y1 - 30), (0, 0, 255), 6)

             cv2.line(frame, (x1, y1), (x1 - 30, y1), (0, 0, 255), 6)  # Bottom right
             cv2.line(frame, (x1, y1), (x1, y1 - 30), (0, 0, 255), 6)

        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)

        
        font = pygame.font.Font("BebasNeue-Regular.ttf", 50)
        text = font.render("Face Detection  : {} Face Detected".format(len(faces)), True, (255, 255, 255))


        window.blit(img, (0, 0))
        window.blit(imgRGB, (280, 95))
        pygame.draw.rect(window, (144, 238, 144), (280, 50, 640, 70), border_top_left_radius=10, border_top_right_radius=10)
        pygame.draw.rect(window, (144, 238, 144), (280, 550, 640, 70), border_bottom_left_radius=10,border_bottom_right_radius=10)
        window.blit(text, (320, 50))
        pygame.display.update()
















































    # cap = cv2.VideoCapture(0)
    #
    #
    # right, left = "", ""
    #
    # while True:
    #     _, frame1 = cap.read()
    #     frame1 = cv2.flip(frame1, 1)
    #     _, frame2 = cap.read()
    #     frame2 = cv2.flip(frame2, 1)
    #
    #     diff = cv2.absdiff(frame2, frame1)
    #
    #     diff = cv2.blur(diff, (5,5))
    #
    #     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #
    #     _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
    #
    #     contr, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     x = 300
    #     if len(contr) > 0:
    #         max_cnt = max(contr, key=cv2.contourArea)
    #         x,y,w,h = cv2.boundingRect(max_cnt)
    #         cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
    #         cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
    #
    #
    #     if right == "" and left == "":
    #         if x > 500:
    #             right = True
    #
    #         elif x < 200:
    #             left = True
    #
    #     elif right:
    #             if x < 200:
    #                 print("to left")
    #                 x = 300
    #                 right, left = "", ""
    #                 cv2.imwrite(f"visitors/in/{datetime.now().strftime('%-y-%-m-%-d-%H:%M:%S')}.jpg", frame1)
    #
    #     elif left:
    #             if x > 500:
    #                 print("to right")
    #                 x = 300
    #                 right, left = "", ""
    #                 cv2.imwrite(f"visitors/out/{datetime.now().strftime('%-y-%-m-%-d-%H:%M:%S')}.jpg", frame1)
    #
    #
    #
    #     cv2.imshow("", frame1)
    #
    #     k = cv2.waitKey(1)
    #
    #     if k == 27:
    #         cap.release()
    #         cv2.destroyAllWindows()
    #         break
    #
# this is change made 
# one more
