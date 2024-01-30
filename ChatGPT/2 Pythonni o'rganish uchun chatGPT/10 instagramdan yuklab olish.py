from instaloader import Instaloader, Profile
# oybekjon_nuriddinov
# ngen.uz
def instagram_video_yuklab_ol(username, saqlash_manzili):
    try:
        # Instaloader obyekti yaratish
        loader = Instaloader()

        # Foydalanuvchi profilini yuklab olish
        profile = Profile.from_username(loader.context, username)

        # Foydalanuvchi profilidagi barcha postlarni yuklab olish
        for post in profile.get_posts():
            if post.is_video:
                # Videoni yuklab olish
                loader.download_post(post, target=saqlash_manzili)
                print("Video muvaffaqiyatli yuklandi!")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    username = input("Instagram profilini kiriting: ")
    saqlash_manzili = input("Videoni saqlash manzilini kiriting: ")
    instagram_video_yuklab_ol(username, saqlash_manzili)
