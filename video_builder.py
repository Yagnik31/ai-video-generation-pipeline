import os
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

# -----------------------
# Load audio file
# -----------------------
audio = AudioFileClip("voice.mp3")

# -----------------------
# Get all images
# -----------------------
image_folder = "images"

images = [
    os.path.join(image_folder, img)
    for img in os.listdir(image_folder)
    if img.endswith((".jpg", ".png", ".jpeg"))
]

# Sort images properly
images.sort()

# Safety check
if len(images) == 0:
    raise Exception("No images found in 'images' folder!")

# -----------------------
# Calculate duration per image
# -----------------------
duration_per_image = audio.duration / len(images)

clips = []

# -----------------------
# Create image clips
# -----------------------
for img in images:
    clip = ImageClip(img).with_duration(duration_per_image)
    clips.append(clip)

# -----------------------
# Combine all clips
# -----------------------
video = concatenate_videoclips(clips, method="compose")

# -----------------------
# Add audio
# -----------------------
video = video.with_audio(audio)

# -----------------------
# Export final video
# -----------------------
video.write_videofile("final_video.mp4", fps=24)

print("✅ Video created successfully: final_video.mp4")
