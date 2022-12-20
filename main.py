import os
from google.cloud import texttospeech
from PyPDF2 import PdfFileReader


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'DemoServiceAccount.json'


def synthesize_text(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Standard-C",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

    response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


def pdf_text():
    target_file = "sample.pdf"
    opened_file = open(target_file, 'rb')
    pdf = PdfFileReader(opened_file)
    num_pages = pdf.getNumPages()
    text = ' '

    for i in range(num_pages):
        page = pdf.getPage(1)
        text = text + ' ' + page.extractText()
        return text


synthesize_text(pdf_text())

