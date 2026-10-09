"""Document boundary detection using classical computer vision."""
import cv2
import numpy as np


def order_points(points):
    """Return four points in top-left, top-right, bottom-right, bottom-left order."""
    pts = np.asarray(points, dtype=np.float32).reshape(4, 2)
    sums = pts.sum(axis=1)
    diffs = np.diff(pts, axis=1).reshape(-1)
    return np.array([
        pts[np.argmin(sums)],
        pts[np.argmin(diffs)],
        pts[np.argmax(sums)],
        pts[np.argmax(diffs)],
    ], dtype=np.float32)


def find_document_corners(image, max_width=1000):
    """Find the largest plausible four-corner contour; return None if not found."""
    if image is None or image.size == 0:
        raise ValueError("Input image is empty.")
    height, width = image.shape[:2]
    scale = min(1.0, max_width / float(width))
    resized = cv2.resize(image, (int(width * scale), int(height * scale))) if scale < 1 else image.copy()
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    edges = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for contour in contours[:30]:
        perimeter = cv2.arcLength(contour, True)
        polygon = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(polygon) == 4 and cv2.contourArea(polygon) > 0.08 * resized.shape[0] * resized.shape[1]:
            corners = order_points(polygon.reshape(4, 2))
            return corners / scale
    return None
