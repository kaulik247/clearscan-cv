"""Image enhancement operations for scanned documents."""
import cv2


def enhance_document(image, mode="color"):
    """Enhance readability using grayscale, denoising and optional thresholding."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if image.ndim == 3 else image.copy()
    gray = cv2.fastNlMeansDenoising(gray, None, h=8, templateWindowSize=7, searchWindowSize=21)
    if mode == "bw":
        return cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 31, 11
        )
    if mode == "gray":
        return gray
    return image
