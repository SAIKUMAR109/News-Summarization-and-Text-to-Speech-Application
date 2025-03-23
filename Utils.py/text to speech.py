from transformers import pipeline, VitsModel, AutoTokenizer
import torch
import soundfile as sf

translation_pipeline = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")
tts_model = VitsModel.from_pretrained("facebook/mms-tts-hin")
tts_tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-hin")

def translate_to_hindi(text):
    """
    Translate text from English to Hindi.
    
    Args:
        text (str): Text to translate.
    
    Returns:
        str: Translated text in Hindi.
    """
    return translation_pipeline(text)[0]['translation_text']

def generate_speech(text, output_file="output.wav"):
    """
    Generate Hindi speech from text and save as an audio file.
    
    Args:
        text (str): Hindi text to convert to speech.
        output_file (str): Path to save the audio file (default: 'output.wav').
    
    Returns:
        str: Path to the generated audio file.
    """
    inputs = tts_tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        waveform = tts_model(**inputs).waveform
    waveform = waveform.squeeze().numpy()
    sf.write(output_file, waveform, tts_model.config.sampling_rate)
    return output_file
