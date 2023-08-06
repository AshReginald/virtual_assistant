import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Mời bạn nói: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="vi-VI")
        print("Bạn -->: {}".format(text))

        # Lưu đoạn text vào file .txt
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print("Đã lưu đoạn text vào file output.txt")

    except:
        print("Xin lỗi! tôi không nhận được voice!")
