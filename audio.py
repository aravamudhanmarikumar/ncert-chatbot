import pyttsx3

engine = pyttsx3.init()

def generate_audio_from_text(text):
    print(text)

    output_file = "output_audio.mp3"

    engine.save_to_file(text, output_file)
    engine.runAndWait()

    return output_file