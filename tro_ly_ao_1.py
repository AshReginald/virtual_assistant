import os
import pyttsx3
import speech_recognition as sr
import datetime

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Chọn giọng tiếng Việt
    engine.say(text)
    engine.runAndWait()

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M"), now.strftime("%d/%m/%Y")

def get_user_input(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        speak(prompt)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="vi-VI")
            return text
        except sr.WaitTimeoutError:
            return "Không nhận được giọng nói."
        except sr.UnknownValueError:
            return "Không thể nhận dạng giọng nói."
        except:
            return "Lỗi xảy ra."

def text():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Xin hãy đặt tên cho tài liệu")
        speak("Xin hãy đặt tên cho tài liệu")
        speech_of_name = r.listen(source)
        try:
            text_name = r.recognize_google(speech_of_name, language="vi-VI")
            print(text_name)
        except:
            print("Xin lỗi! tôi không nhận được voice!")
        
        print("Nội dung tài liệu là? ")
        speak("Nội dung tài liệu là? ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="vi-VI")
            print("Bạn -->: {}".format(text))

            # Lưu đoạn text vào file .txt
            script_dir = os.path.dirname(__file__)  # Lấy đường dẫn thư mục của script
            file_path = os.path.join(script_dir, f"{text_name}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
            print(f"Đã lưu đoạn text vào file {text_name}.txt")

        except:
            print("Xin lỗi! tôi không nhận được voice!")

def greet_user():
    current_time, current_date = get_current_time()
    if 5 <= int(current_time[:2]) < 12:
        greet_message = "Chào buổi sáng! Chúc bạn một ngày tốt lành!"
    elif 12 <= int(current_time[:2]) < 19:
        greet_message = "Xin chào! Bạn sẵn sàng cho buổi chiều hôm nay chưa?"
    else:
        greet_message = "Chào buổi tối! Hy vọng bạn đã có một ngày tuyệt vời."
    print(greet_message)
    speak(greet_message)

def main():
    greet_user()
    
    while True:
        user_input = get_user_input("Hãy nói gì đó để tôi có thể giúp bạn ")
        
        if "tắt máy" in user_input:
            speak("Tạm biệt!")
            break
        elif "thời gian" in user_input:
            current_time, current_date = get_current_time()
            response = f"Bây giờ là {current_time}, hôm nay là ngày {current_date}."
            print(response)
            speak(response)
        elif "ghi lại" in user_input:
            text()
        else:
            response = "Bạn vừa nói: " + user_input
            print(response)
            speak(response)

if __name__ == "__main__":
    main()
