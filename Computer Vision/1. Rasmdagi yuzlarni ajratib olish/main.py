import face_recognition
from PIL import Image

# rasmlarni o'qib oladi
image = face_recognition.load_image_file("img_3.png")
# yuzlarni ajratib oladi
face_locations = face_recognition.face_locations(image)
i = 1
# har bir yuzni alohida saqlaydi
for face_location in face_locations:
    # ramka koordinatalari
    top, right, bottom, left = face_location
    print(f'Koordinata: {top} {right} {bottom} {left}')
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f'{i}.jpg')
    i += 1
# aniqlangan yuzlar sonini chiqaradi
print(f"Rasmda {len(face_locations)} ta odam bor ekan")