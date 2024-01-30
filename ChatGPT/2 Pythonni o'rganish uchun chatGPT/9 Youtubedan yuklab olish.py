from pytube import YouTube
# https://www.youtube.com/watch?v=e8-H2mifJmE&list=PLZ67NWgKA8g7b-o4w5bm3B4fngZ2ug959&index=58
def video_yuklab_ol(video_url, saqlash_manzili):
    try:
        # YouTube video obyektini yaratish
        video = YouTube(video_url)

        # Video haqida ma'lumotlar chiqarish
        print("Video nomi:", video.title)
        print("Video uzunligi:", video.length, "sekund")
        print("Video formati:", video.streams.get_highest_resolution().mime_type)

        # Videoni yuklab olish
        video.streams.get_highest_resolution().download(output_path=saqlash_manzili)
        print("Video muvaffaqiyatli yuklandi!")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    video_url = input("Yuklab olish uchun YouTube video havolasini kiriting: ")
    saqlash_manzili = input("Video faylini saqlash manzilini kiriting: ")
    video_yuklab_ol(video_url, saqlash_manzili)
