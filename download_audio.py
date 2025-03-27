import torch
from torch import nn
import torchaudio
import os
import requests
import shutil
import yt_dlp


SAMPLE_DIR = "assets"
os.makedirs(SAMPLE_DIR, exist_ok=True) #Will make the directory if it does not yet exist
sample_mike_breen = "https://youtu.be/MYS7pPHrIIQ?si=AdlmLkyZTl0vrxJ-"
sample_eric_collins = "https://youtu.be/YrigSv0Fovg?si=NDgTuRVO2H4xCb3_"
sample_ian_eagle = "https://youtu.be/9j36rXS91FA?si=6T7Y6mt1lk1SSiu8"
sample_brian_sieman = "https://youtu.be/yDsx_Y6PHzI?si=iKpsWFqjnPdz1XLG"
sample_mark_jones = "https://youtu.be/xGzVOhYzOmY?si=XMwt_b3bfZCahhud"


def download_audio(url, filename):
    """This function is used to download the audio from youtube and save it to the specified filename"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_audio(sample_mike_breen, os.path.join(SAMPLE_DIR, "mike_breen"))
download_audio(sample_eric_collins, os.path.join(SAMPLE_DIR, "eric_collins"))
download_audio(sample_ian_eagle, os.path.join(SAMPLE_DIR, "ian_eagle"))
download_audio(sample_brian_sieman, os.path.join(SAMPLE_DIR, "brian_sieman"))
download_audio(sample_mark_jones, os.path.join(SAMPLE_DIR, "mark_jones"))
