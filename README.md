# AI Video Generation Pipeline

## Overview

This project builds an automated AI video generation pipeline that converts a given topic into a YouTube-ready video using free tools.

One trigger → One video.

## Pipeline Flow

1. User inputs a topic
2. Script generated using Groq LLM API
3. Script converted to voiceover using Edge TTS
4. Relevant images fetched using Pexels API
5. MoviePy combines visuals + audio into final MP4

## Tech Stack

- Python
- Groq API (LLM)
- Edge TTS
- Pexels API
- MoviePy

## Setup

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python main.py

Enter a topic and the system automatically generates a video.

## Notes

- Uses only free-tier tools
- Fully automated
- End-to-end execution
