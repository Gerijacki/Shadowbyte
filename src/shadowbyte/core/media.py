"""
Media utilities module.
"""
import os

import qrcode
import yt_dlp

from shadowbyte.utils.display import print_error, print_info, print_success


def generate_qr_code(data: str, filename: str = "qrcode.png"):
    """Generates a QR code."""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print_success(f"QR Code saved to {filename}")
    except Exception as e:
        print_error(f"Error generating QR code: {e}")

def download_video(url: str, output_path: str = "."):
    """Downloads a video from YouTube using yt-dlp."""
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best',
    }

    print_info(f"Downloading video from {url}...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print_success("Download completed successfully.")
    except Exception as e:
        print_error(f"Download failed: {e}")
