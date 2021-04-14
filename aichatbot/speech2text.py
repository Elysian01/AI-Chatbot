import speech_recognition as sr
import pyttsx3


def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["success"] = False
            response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)
    print("Start Speacking....\n")
    response = recognize_speech_from_mic(recognizer, microphone)

    if response["success"]:
        print(response["transcription"])
    else:
        print(response["error"])
