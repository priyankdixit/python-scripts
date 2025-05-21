🔧 Python Utility Scripts

A collection of practical Python scripts for automating everyday tasks including image editing, PDF merging, and YouTube video downloading.

📁 Contents

1. image_editor.py – Batch edit and enhance images using Pillow.
2. pdf_merger.py – Merge multiple PDFs into a single document.
3. yt_downloader.py – Download YouTube videos using yt-dlp (fallback for pytube).

🧰 Tech Stack

- Python 3.x
- Libraries Used:
  - Pillow for image editing
  - PyPDF2 for PDF merging
  - yt-dlp for YouTube downloads (alternative to pytube)

🔍 1. Image Editor

Script: photoEditor.py

Description:  
Processes all images in a folder by sharpening, rotating, converting to black & white, and increasing contrast. Saves the edited images in a separate folder.

Usage:
pip install pillow
python photoEditor.py


Folder Structure:
imageProcessor/
├── photoEditor.py
├── imgs/             # Input images
└── editedImgs/       # Output images (auto-created if not present)

📄 2. PDF Merger

Script: pdfMerger.py

Description:  
Automatically merges all .pdf files in the current directory into a single combined.pdf.

Usage:
pip install PyPDF2
python pdfMerger.py

📹 3. YouTube Video Downloader

Script: ytDownloader.py

Description:  
Downloads the highest-quality version of a YouTube video using yt-dlp. This is a more reliable fallback for pytube, which breaks when YouTube updates their backend.

Usage:
pip install yt-dlp
python ytDownloader.py


💡 Note on pytube

The original implementation using pytube is currently not functional due to a breaking change in YouTube’s internal structure. This repo uses yt-dlp instead, which is more reliable and actively maintained.
