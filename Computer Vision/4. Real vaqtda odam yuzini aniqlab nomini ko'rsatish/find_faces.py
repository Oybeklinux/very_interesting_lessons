import face_recognition
import cv2
import os
import glob
import numpy as np


class FindFaces:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Tezlashtirish maqsadida freymni kichiklashtirish
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):

        # Rasmlarni katalogdan yuklab oladi
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} rasm topildi".format(len(images_path)))

        # Rasm nomlari va kodlashtirilgan versiyasini saqlaydi
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Fayl nomi va kengaytmasini ajratib oladi
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Kodlashgan versiyaga o'giradi
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Fayl nomi va kodlashgan versiyasini saqlaydi
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Rasmlar yuklandi")

    def detect_known_faces(self, frame):
        # freymni kichiklashtirish
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Mazkur freymda hamma yuzni topadi
        # BGR rangdan (OpenCV formati) RGB rangga (face_recognition formati) o'giradi
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Rasm bazadagi rasmlar bilan mos kelishini aniqlaydi
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Noma'lum"

            # # known_face_encodings mos kelgani topilsa, birinchisini oladi
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Yoki uni o'rniga, ma'lum yuzni moma'lum yuzga nisbatan eng qisqa masofaga ega bo'lganini oladi
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        # freymni kattalashtirish - o'z holiga qaytarish
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
