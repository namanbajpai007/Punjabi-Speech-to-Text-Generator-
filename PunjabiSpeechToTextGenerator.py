import tkinter as tk
import speech_recognition as sr
import threading
import time
from translate import Translator

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

# Punjabi Conversion Section
start_button_punjabi = tk.Button(root, text="Start Punjabi Speech", command=start_conversion_punjabi, bg="#5cb85c", fg="white", font=("Helvetica", 12), padx=10)
start_button_punjabi.grid(row=0, column=0, padx=5, pady=5)

translated_text_punjabi = tk.Text(root, height=10, width=50, bg="white", fg="#333", font=("Helvetica", 14), wrap="word")
translated_text_punjabi.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

words_label_punjabi = tk.Label(root, text="Number of words: 0", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
words_label_punjabi.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

duration_label_punjabi = tk.Label(root, text="Duration: 0.00 seconds", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
duration_label_punjabi.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

translated_hindi_label_punjabi = tk.Label(root, text="Hindi Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_hindi_label_punjabi.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

translated_gujarati_label_punjabi = tk.Label(root, text="Gujarati Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_gujarati_label_punjabi.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

translated_german_label_punjabi = tk.Label(root, text="German Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_german_label_punjabi.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

translated_sanskrit_label_punjabi = tk.Label(root, text="Sanskrit Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_sanskrit_label_punjabi.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

translated_french_label_punjabi = tk.Label(root, text="French Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_french_label_punjabi.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# French Conversion Section
start_button_french = tk.Button(root, text="Start French Speech", command=start_conversion_french, bg="#5cb85c", fg="white", font=("Helvetica", 12), padx=10)
start_button_french.grid(row=0, column=2, padx=5, pady=5)

translated_text_french = tk.Text(root, height=10, width=50, bg="white", fg="#333", font=("Helvetica", 14), wrap="word")
translated_text_french.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

words_label_french = tk.Label(root, text="Number of words: 0", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
words_label_french.grid(row=3, column=2, columnspan=2, padx=10, pady=5)

duration_label_french = tk.Label(root, text="Duration: 0.00 seconds", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
duration_label_french.grid(row=4, column=2, columnspan=2, padx=10, pady=5)

translated_hindi_label_french = tk.Label(root, text="Hindi Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_hindi_label_french.grid(row=5, column=2, columnspan=2, padx=10, pady=5)

translated_gujarati_label_french = tk.Label(root, text="Gujarati Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_gujarati_label_french.grid(row=6, column=2, columnspan=2, padx=10, pady=5)

translated_german_label_french = tk.Label(root, text="German Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_german_label_french.grid(row=7, column=2, columnspan=2, padx=10, pady=5)

translated_sanskrit_label_french = tk.Label(root, text="Sanskrit Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_sanskrit_label_french.grid(row=8, column=2, columnspan=2, padx=10, pady=5)

translated_punjabi_label_french = tk.Label(root, text="Punjabi Translation: ", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
translated_punjabi_label_french.grid(row=9, column=2, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
