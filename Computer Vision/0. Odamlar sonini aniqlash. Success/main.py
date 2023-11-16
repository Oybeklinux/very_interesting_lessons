import face_recognition

# Rasmni o'qib oladi
image = face_recognition.load_image_file("img_1.png")
# Tasvirdagi inson yuzlarining chegaralangan ramkalarini qaytaradi
face_locations = face_recognition.face_locations(image)
# yuzlar sonini aniqlaydi
print(f"Rasmda {len(face_locations)} ta odam bor ekan")