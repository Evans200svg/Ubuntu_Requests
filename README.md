# 🖼️ Multi-URL Image Fetcher

A simple Python script that downloads images from one or more URLs, stores them in a `Fetched_Images` directory, and takes precautions against unsafe or duplicate downloads.

---

## 🚀 Features
- ✅ Download multiple images at once (comma-separated URLs)
- ✅ Creates a `Fetched_Images/` directory automatically
- ✅ Validates files using **HTTP headers**
  - Only downloads files with `Content-Type: image/*`
  - Skips files larger than **10MB** (`Content-Length` check)
- ✅ Prevents downloading **duplicate images** using SHA-256 hashing
- ✅ Extracts filename from URL, or generates a unique name if missing
- ✅ Saves images in **binary mode** to preserve quality
- ✅ Gracefully handles HTTP errors and network issues

---

## 📦 Requirements
- Python 3.7+
- [requests](https://pypi.org/project/requests/)

Install dependencies with:

```bash
pip install requests
```
## 📂 Usage

- Clone or download this repository.

Run the script:
```bash
python fetch_images.py
```

- Enter one or more image URLs (comma-separated), for example:

- Enter image URLs (comma-separated): 
["https://example.com/image1.jpg, https://example.com/image2.png"]


- Downloaded images will be saved inside the Fetched_Images/ directory.

## 🛡️ Security Precautions

- Content-Type check → Only images are saved.

- Content-Length limit → Prevents very large downloads (>10MB).

- Duplicate detection → Uses SHA-256 hashing to skip duplicate images.

- Custom User-Agent → Prevents blocking by some servers.

#### ⚠️ Note: Always be cautious when downloading files from unknown sources, as they may contain harmful or misleading content. This script only saves files classified as images, but further validation may be needed for production use.

## 📌 Example Output
- ✅ Image saved: Fetched_Images/image1.jpg
- ⚠️ Skipping https://example.com/not_image.txt: Not an image (Content-Type: text/plain)
- ⚠️ Skipping https://example.com/large.jpg: File too large (12000000 bytes)
- ⚠️ Skipping https://example.com/image1.jpg: Duplicate image detected

## 🔧 Future Improvements

- Add option to read URLs from a text file

- Support for ETag / Last-Modified caching

- Allow user to customize size limits and output directory

