# DNA -> RNA Transcription
#Assume input is noncoding strand
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcript = []
    for base in seq:
        if base in TRANSCRIPTION_MAPPING:
            transcript.append(TRANSCRIPTION_MAPPING[base])
        else:
            transcript.append('X') #indicates improper base

    return "".join(transcript)

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    transcript = []
    for base in seq[::-1]:
        if base in TRANSCRIPTION_MAPPING:
            transcript.append(TRANSCRIPTION_MAPPING[base])
        else:
            transcript.append('X') #indicates improper base

    return "".join(transcript)
