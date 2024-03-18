import tkinter as tk
import speech_recognition as sr
import threading
import time
from translate import Translator
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Punjabi Speech to Text Generator!'

if __name__ == '__main__':
    app.run(debug=True)

# Punjabi Conversion Section
@app.route('/punjabi', methods=['GET'])
def punjabi_conversion():
    global stop_listening_punjabi
    stop_listening_punjabi = False
    start_conversion_punjabi()
    return jsonify({'message': 'Punjabi speech recognition route'})

# French Conversion Section
@app.route('/french', methods=['GET'])
def french_conversion():
    global stop_listening_french
    stop_listening_french = False
    start_conversion_french()
    return jsonify({'message': 'French speech recognition route'})

def start_conversion_punjabi():
    global stop_listening_punjabi
    stop_listening_punjabi = False
    start_button_punjabi.config(state=tk.DISABLED)  # Disable the button during speech recognition
    start_time = time.time()  # Record the start time of speech recognition

    def stop_conversion():
        global stop_listening_punjabi
        stop_listening_punjabi = True
        start_button_punjabi.config(state=tk.NORMAL)  # Re-enable the button when speech recognition stops

    # Creating a separate thread for speech recognition
    def recognize_speech_punjabi():
        global stop_listening_punjabi
        recognizer = sr.Recognizer()
        audio_stream = sr.Microphone()
        with audio_stream as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
            while not stop_listening_punjabi:
                try:
                    audio_data = recognizer.listen(source, timeout=0.5)  # Adjust timeout for faster response
                    text = recognizer.recognize_google(audio_data, language='pa-IN')  # Punjabi language code
                    translated_text_punjabi.delete(1.0, tk.END)
                    translated_text_punjabi.insert(tk.END, text)
                    word_count = len(text.split())
                    words_label_punjabi.config(text=f"Number of words: {word_count}")
                    translated_hindi = translate_text(text, 'pa', 'hi')
                    translated_gujarati = translate_text(text, 'pa', 'gu')
                    translated_german = translate_text(text, 'pa', 'de')
                    translated_sanskrit = translate_text(text, 'pa', 'sa')
                    translated_french = translate_text(text, 'pa', 'fr')
                    translated_hindi_label_punjabi.config(text=f"Hindi Translation: {translated_hindi}")
                    translated_gujarati_label_punjabi.config(text=f"Gujarati Translation: {translated_gujarati}")
                    translated_german_label_punjabi.config(text=f"German Translation: {translated_german}")
                    translated_sanskrit_label_punjabi.config(text=f"Sanskrit Translation: {translated_sanskrit}")
                    translated_french_label_punjabi.config(text=f"French Translation: {translated_french}")
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    translated_text_punjabi.delete(1.0, tk.END)
                    translated_text_punjabi.insert(tk.END, "Could not request results; {0}".format(e))
                duration = time.time() - start_time
                duration_label_punjabi.config(text=f"Duration: {duration:.2f} seconds")
                root.update()  # Update the GUI to reflect changes
                if stop_listening_punjabi:
                    break

        # Re-enable the button after speech recognition stops
        start_button_punjabi.config(state=tk.NORMAL)

    def translate_text(text, source_lang, target_lang):
        translator = Translator(to_lang=target_lang, from_lang=source_lang)
        translation = translator.translate(text)
        return translation

    stop_conversion_button_punjabi = tk.Button(root, text="Stop Speech", command=stop_conversion, bg="#d9534f", fg="white", font=("Helvetica", 12), padx=10)
    stop_conversion_button_punjabi.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Start the speech recognition process in a separate thread
    recognize_thread_punjabi = threading.Thread(target=recognize_speech_punjabi)
    recognize_thread_punjabi.start()

def start_conversion_french():
    global stop_listening_french
    stop_listening_french = False
    start_button_french.config(state=tk.DISABLED)  # Disable the button during speech recognition
    start_time = time.time()  # Record the start time of speech recognition

    def stop_conversion():
        global stop_listening_french
        stop_listening_french = True
        start_button_french.config(state=tk.NORMAL)  # Re-enable the button when speech recognition stops

    # Create a separate thread for speech recognition
    def recognize_speech_french():
        global stop_listening_french
        recognizer = sr.Recognizer()
        audio_stream = sr.Microphone()
        with audio_stream as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
            while not stop_listening_french:
                try:
                    audio_data = recognizer.listen(source, timeout=0.5)  # Adjust timeout for faster response
                    text = recognizer.recognize_google(audio_data, language='fr-FR')  # French language code
                    translated_text_french.delete(1.0, tk.END)
                    translated_text_french.insert(tk.END, text)
                    word_count = len(text.split())
                    words_label_french.config(text=f"Number of words: {word_count}")
                    translated_hindi = translate_text(text, 'fr', 'hi')
                    translated_gujarati = translate_text(text, 'fr', 'gu')
                    translated_german = translate_text(text, 'fr', 'de')
                    translated_sanskrit = translate_text(text, 'fr', 'sa')
                    translated_punjabi = translate_text(text, 'fr', 'pa')
                    translated_hindi_label_french.config(text=f"Hindi Translation: {translated_hindi}")
                    translated_gujarati_label_french.config(text=f"Gujarati Translation: {translated_gujarati}")
                    translated_german_label_french.config(text=f"German Translation: {translated_german}")
                    translated_sanskrit_label_french.config(text=f"Sanskrit Translation: {translated_sanskrit}")
                    translated_punjabi_label_french.config(text=f"Punjabi Translation: {translated_punjabi}")
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    translated_text_french.delete(1.0, tk.END)
                    translated_text_french.insert(tk.END, "Could not request results; {0}".format(e))
                duration = time.time() - start_time
                duration_label_french.config(text=f"Duration: {duration:.2f} seconds")
                root.update()  # Update the GUI to reflect changes
                if stop_listening_french:
                    break

        # Re-enable the button after speech recognition stops
        start_button_french.config(state=tk.NORMAL)

    def translate_text(text, source_lang, target_lang):
        translator = Translator(to_lang=target_lang, from_lang=source_lang)
        translation = translator.translate(text)
        return translation

    stop_conversion_button_french = tk.Button(root, text="Stop Speech", command=stop_conversion, bg="#d9534f", fg="white", font=("Helvetica", 12), padx=10)
    stop_conversion_button_french.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

    # Start the speech recognition process in a separate thread
    recognize_thread_french = threading.Thread(target=recognize_speech_french)
    recognize_thread_french.start()

# Create main window
root = tk.Tk()
root.title("Speech to Text Converter")
root.configure(bg="#f5f5f5")

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)

# Run the application
root.mainloop()
