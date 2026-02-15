import requests
import os

PEXELS_API_KEY = "kg5CHjO34KNcUHqAlc9cfx6AJpEzQY4pv8H8kIqsKBrQRLansgsgHkKJ"

def download_images(topic):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    url = f"https://api.pexels.com/v1/search?query={topic}&per_page=5"

    response = requests.get(url, headers=headers)
    data = response.json()

    if not os.path.exists("images"):
        os.makedirs("images")

    for i, photo in enumerate(data["photos"]):
        image_url = photo["src"]["large"]
        img_data = requests.get(image_url).content

        with open(f"images/image_{i}.jpg", "wb") as f:
            f.write(img_data)

    print("Images downloaded successfully!")

if __name__ == "__main__":
    topic = input("Enter topic for images: ")
    download_images(topic)
