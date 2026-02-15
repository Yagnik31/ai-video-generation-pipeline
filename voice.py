import asyncio
import edge_tts

async def generate_voice():
    # Read script from file
    with open("script.txt", "r", encoding="utf-8") as f:
        script = f.read()

    # Choose voice
    voice = "en-US-AriaNeural"

    communicate = edge_tts.Communicate(script, voice)
    await communicate.save("voice.mp3")

    print("Voice generated successfully: voice.mp3")

asyncio.run(generate_voice())
