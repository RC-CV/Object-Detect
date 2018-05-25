# coding:utf8
import cv2
import houghCircle

def detect_video(video,ringPoint):
    camera = cv2.VideoCapture(video)
    history = 20    # 训练帧数

    # bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)  # 背景减除器，设置阴影检测
    # bs = cv2.bgsegm.createBackgroundSubtractorMOG(history=history) # 效果不行
    bs = cv2.createBackgroundSubtractorMOG2(history=history, detectShadows=True) #这个效果最好
    bs.setHistory(history)
    img_width, img_height = camera.get(3), camera.get(4)
    print(img_width , img_height)
    ball_x = 0
    ball_y = 0

    frames = 0
    points = []
    ring_x , ring_y , ring_r=ringPoint
    while True:
        res, frame = camera.read()
        frame = cv2.GaussianBlur(frame, (21, 21), 0)
        if not res:
            # 若读取失败则跳出循环
            break
        # cv2.imshow("first" , frame)
        fg_mask = bs.apply(frame)   # 获取 foreground mask
        # cv2.imshow("frame" , fg_mask)
        if frames < history:
            frames += 1
            continue

        # 对原始帧进行膨胀去噪
        # 二值化阈值处理，前景掩码含有前景的白色值以及阴影的灰色值，在阈值化图像中，将非纯白色（244~255）的所有像素都设为0，而不是255
        th = cv2.threshold(fg_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 6)), iterations=2)
        # 获取所有检测框
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(len(contours))
        if(len(contours) > 4):
            print("shock , no ball")
            continue

        for c in contours:
            # print(c)
            # 获取矩形框边界坐标
            x, y, w, h = cv2.boundingRect(c)
            print([x,y,w,h])
            # 计算矩形框的面积
            area = cv2.contourArea(c)
            print(area)
            # 如果是640，7mi则用200<area <2500(比赛不用7米，是6米)
            # 如果是1280，2m高，6m远 ,area用600~8000(放弃这种参数)
            # 如果是640的，2m高，6m远 ,area用600~8000
            # 如果是320的，2m高，6m远，area用120~8000
            if 120 < area < 8000 :
                # print([ball_x,ball_y])
                # 如果是640或1280的，则用y < (img_height*0.41) and (img_width*0.15) < x < (img_width*0.78)
                # 或者如果是640或1280的，则用y < (img_height*0.41) and (ring_x-ring_r-100) < x < (ring_x+ring_r+100)(建议)
                # 如果是320的，用y < (img_height*0.41) and (ring_x-ring_r-50) < x < (ring_x+ring_r+50)
                if ball_x== 0 and ball_y ==0 and y < (img_height*0.41) and (ring_x-ring_r-50) < x < (ring_x+ring_r+50):
                    ball_x = x
                    ball_y = y
                    print("First ball get",[ball_x ,ball_y])
                    points.append([x,y,w,h])
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    # 640的，用 ball_x !=0 and (ball_x - (img_width*0.15)) < x < (ball_x+(img_width*0.15)) and ( y < (ball_y+img_height*0.5))
                    # 320的，用 ball_x !=0 and (ball_x - (img_width*0.15)) < x < (ball_x+(img_width*0.15)) and ( y < (ball_y+img_height*0.35))
                    if ball_x !=0 and (ball_x - (img_width*0.15)) < x < (ball_x+(img_width*0.15)) and ( y < (ball_y+img_height*0.35)):
                        if  (y ) > (ring_y + ring_r) or (y + 10) > (ring_y + ring_r) or (y+h+5) > img_height:
                            # 小球结束,小球走到了环的下面
                            # 640，用(y ) > (ring_y + ring_r) or (y + 10) > (ring_y + ring_r)
                            # 320，用 (y ) > (ring_y + ring_r) or (y + 10) > (ring_y + ring_r) or (y+h+5) > img_height
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            print("ball is done!")
                            camera.release()
                            break
                        else:
                            ball_x = x
                            ball_y = y
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            print("Next ball",[ball_x ,ball_y])
                            points.append([x,y,w,h])
                            break

                    elif ball_x==0 and ball_y ==0  :
                        print("no ball")
                        # break
                    elif y < ball_y:
                        print("no ball")
                        break
                    else:
                        print("Scanner Moved!")
                        ball_y += (img_height*0.1)
                        break

        cv2.imshow("detection", frame)
        cv2.imshow("back", dilated)
        k = cv2.waitKey(110) & 0xff
        if k == 27:
            break
    if ball_x == 0 and ball_y == 0:
        print("Didn't throw the ball")
    camera.release()
    cv2.destroyAllWindows()
    return points
'''
if __name__ == '__main__':
    video = 'RightNotIn12.avi'
    detect_video(video)
'''
