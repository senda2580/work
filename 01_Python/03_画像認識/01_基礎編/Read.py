import cv2

# 画像を読み込む
img = cv2.imread('.\image\TEST.jpg')

# 画像を表示する
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()