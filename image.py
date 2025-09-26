import os
import requests
from urllib.parse import urlparse
import uuid
import hashlib

def get_filename_from_url(url, content_type):
    """Extract filename from URL or generate a unique one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If no filename in URL, generate one
    if not filename:
        ext = get_extension_from_content_type(content_type)
        filename = f"image_{uuid.uuid4().hex}{ext}"
    
    return filename

def get_extension_from_content_type(content_type):
    """Return proper file extension based on Content-Type."""
    if content_type == "image/jpeg":
        return ".jpg"
    elif content_type == "image/png":
        return ".png"
    elif content_type == "image/gif":
        return ".gif"
    elif content_type == "image/webp":
        return ".webp"
    else:
        return ".bin"  # fallback if unknown

def calculate_hash(content):
    """Calculate SHA256 hash of file content to prevent duplicates."""
    return hashlib.sha256(content).hexdigest()

def fetch_images():
    # Prompt user for multiple URLs (comma-separated)
    urls = input("Enter image URLs (comma-separated): ").strip().split(",")

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Keep track of downloaded file hashes
    downloaded_hashes = set()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        try:
            # Fetch the image with safe headers
            response = requests.get(url, timeout=10, headers={"User-Agent": "ImageFetcher/1.0"})
            response.raise_for_status()

            # Check HTTP headers for precautions
            content_type = response.headers.get("Content-Type", "")
            content_length = response.headers.get("Content-Length")

            if not content_type.startswith("image/"):
                print(f"⚠️ Skipping {url}: Not an image (Content-Type: {content_type})")
                continue

            if content_length and int(content_length) > 10_000_000:  # limit to ~10MB
                print(f"⚠️ Skipping {url}: File too large ({content_length} bytes)")
                continue

            # Check for duplicates using hash
            file_hash = calculate_hash(response.content)
            if file_hash in downloaded_hashes:
                print(f"⚠️ Skipping {url}: Duplicate image detected")
                continue

            downloaded_hashes.add(file_hash)

            # Get a safe filename
            filename = get_filename_from_url(url, content_type)
            save_path = os.path.join(save_dir, filename)

            # Save image
            with open(save_path, "wb") as f:
                f.write(response.content)

            print(f"Image saved: {save_path}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}. Error: {e}")

if __name__ == "__main__":
    fetch_images()
