import g4f, asyncio
import sys

from g4f.Provider import ProviderUtils

_providers = [
    # g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    # g4f.Provider.Yqcloud,
]

text = """Quyidagi universitetlarni telefon raqami kerak:
Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti;
Toshkent shahridagi Amiti universiteti;
Toshkent shahridagi Inha Universiteti;
Toshkent viloyati Chirchiq davlat pedagogika instituti;
Mirzo Ulug‘bek nomidagi O‘zbekiston Milliy universiteti
Islom Karimov nomidagi Toshkent davlat texnika universiteti;
Toshkent davlat Iqtisodiyot universiteti;
Toshkent davlat agrar universiteti;
M.V.Lomonosov nomidagi Moskva davlat universitetining Toshkent shahridagi filiali;
Toshkent davlat pedagogika universiteti;
O‘zbekistonʼxalqaroʼIslom akademiyasi;
Toshkent shahridagi Turin Politexnika universiteti;
Toshkent shahridagi Vebster universitetining ta’lim dasturlarini amalga oshirish markazi;
Toshkent Kimyo xalqaro universiteti
O‘zbekiston davlat jahon tillari universiteti
Toshkent davlat transport universiteti;
Toshkent davlat sharqshunoslik universiteti;
Toshkent arxitektura-qurilish instituti;
Toshkent Moliya Instituti;
Toshkent kimyo-texnologiya instituti;
Toshkent irrigatsiya va qishloq xo‘jaligini mexanizatsiyalash muhandislari instituti”ʼmilliy tadqiqot universiteti;
Jahon iqtisodiyoti va diplomatiya universiteti; 
Toshkent Davlat Yuridik Universiteti; 
Singapur menejmentni rivojlantirish instituti."""

text = """Menga quyidagi o'zbek tilidagi matnni ingliz tiliga tarjima qilib ber:
Bizning kompaniyaning nomi NextGen Academy"""

text = "Menga ayiq haqida hazil yarat"
poet = "Menga quyidagi haqida sher yozib ber: NextGen Academy Python instituti, Javascript instituti, Cisco Networking Academy, Fortinet kabi xalqaro ishlab chiqaruvchilarning hamkori hisoblanadi. Ushbu hamkorlik talabalarga xalqaro dasturlarda sifatli ta'lim olish imkonini beradi, shuningdek, xalqaro sertifikat olish imkoniyatini beradi."

text = "Menga ruslar haqida latifa gapirib ber"


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": text}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())
