# coding:utf8
import cv2

def detect_video(video):
    camera = cv2.VideoCapture(video)
    history = 20    # 训练帧数

    # bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)  # 背景减除器，设置阴影检测
    # bs = cv2.bgsegm.createBackgroundSubtractorMOG(history=history) # 效果不行
    bs = cv2.createBackgroundSubtractorMOG2(history=history, detectShadows=True) #这个效果最好

    bs.setHistory(history)

    ball_x = 0
    ball_y = 0

    frames = 0
    points=[]

    while True:
        res, frame = camera.read()
        frame = cv2.GaussianBlur(frame, (21, 21), 0) #用高斯滤波检测更好点
        if not res:
            break

        fg_mask = bs.apply(frame)   # 获取 foreground mask

        if frames < history:
            frames += 1
            continue

        # 对原始帧进行膨胀去噪
        th = cv2.threshold(fg_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 3)), iterations=2)
        # 获取所有检测框
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # print(len(contours))
        if(len(contours) > 4):
            print("shock , no ball")
            continue
        for c in contours:
            # 获取矩形框边界坐标
            x, y, w, h = cv2.boundingRect(c)
            # print([x,y,w,h])
            # 计算矩形框的面积
            area = cv2.contourArea(c)
            # print(area)

            if 200 < area < 2500 :
                # print([ball_x,ball_y])
                if ball_x== 0 and ball_y ==0 and y < 200:
                    ball_x = x
                    ball_y = y
                    print("First ball get",[ball_x ,ball_y])
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    points.append([x,y,w,h])
                else:
                    if (ball_x -100 < x < ball_x+100) and ( y < ball_y+240):
                        ball_x = x
                        ball_y = y
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        print("Next ball",[ball_x ,ball_y])
                        points.append([x,y,w,h])
                    elif ball_x==0 and ball_y ==0  :
                        print("no ball")
                        break
                    else:
                        print("Scanner Moved!")
                        ball_y += 50
                        break

        cv2.imshow("detection", frame)
        cv2.imshow("back", dilated)
        if cv2.waitKey(110) & 0xff == 27:
            # 按Esc退出
            break

    camera.release()
    cv2.destroyAllWindows()
    return points

'''
if __name__ == '__main__':
    video = 'jin4.avi'
    points=detect_video(video)
    print(points)
'''
