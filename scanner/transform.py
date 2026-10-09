"""Perspective correction for quadrilateral regions."""
import cv2
import numpy as np
from .detection import order_points


def warp_document(image, corners):
    """Apply a perspective transform and return a top-down document image."""
    rect = order_points(corners)
    tl, tr, br, bl = rect
    width_a = np.linalg.norm(br - bl)
    width_b = np.linalg.norm(tr - tl)
    height_a = np.linalg.norm(tr - br)
    height_b = np.linalg.norm(tl - bl)
    out_w = max(1, int(max(width_a, width_b)))
    out_h = max(1, int(max(height_a, height_b)))
    destination = np.array([
        [0, 0], [out_w - 1, 0],
        [out_w - 1, out_h - 1], [0, out_h - 1]
    ], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(rect.astype(np.float32), destination)
    return cv2.warpPerspective(image, matrix, (out_w, out_h))
