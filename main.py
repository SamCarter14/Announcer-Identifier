import torch
from torch import nn
import torchaudio
import os
import requests
import shutil
import yt_dlp

SAMPLE_DIR = "assets"
sample_path_breen = os.path.join(SAMPLE_DIR, "mike_breen.wav")
sample_path_collins = os.path.join(SAMPLE_DIR, "eric_collins.wav")
print(os.path.exists(sample_path_breen))  # Should print True if file exists
print(os.path.exists(sample_path_collins))
print(sample_path_breen)
metadata_breen = torchaudio.info(sample_path_breen)
metadata_collins = torchaudio.info(sample_path_collins)

print(metadata_breen)
print(metadata_collins)