import cv2
import face_recognition

# rasmni o'qib oladi
img1 = cv2.imread("prezident.png")
# OpenCV odatda BGR formatida saqlaydi, shuning uchun uni
# RGB formatga o'girish kerak
rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# yuzni aniqlab oladi
img1_encoding = face_recognition.face_encodings(rgb_img1)[0]

# huddi yuqoridagi jarayon boshqa rasm uchun bajariladi
img2 = cv2.imread("people1.png")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_encoding = face_recognition.face_encodings(rgb_img2)[0]

# 1-rasmdagi yuz/yuzlar ikkinchi rasmdagi yuz/yuzlarga o'xshashligini ehtimollik
# bilan aniqlaydi
result = face_recognition.compare_faces([img1_encoding], img2_encoding)
if result[0]:
    print("Birinchi rasmdagi odam ikkinchi rasmda bor")
else:
    print("Birinchi rasmdagi odam ikkinchi rasmda yo'q")

# oynada ko'rsatish
cv2.imshow("Men", img1)
cv2.imshow("Ular", img2)
# biror tugmani bosilishini kutish
cv2.waitKey(0)
