# Project Statement — ClearScan CV

## Problem statement
Photographs of paper documents can be tilted, skewed, noisy, or difficult to read. Manually correcting each image is time-consuming. This project explores a lightweight Computer Vision pipeline that detects a likely paper boundary, rectifies perspective, and produces an enhanced image.

## Scope
The prototype processes one local image at a time from the command line. It uses classical OpenCV operations and does not require cloud services, a trained model, or network access. It is a document-image enhancement tool, not an OCR system.

## Target users
- Students digitizing notes and handouts
- People preparing readable copies of receipts or forms
- Developers learning classical Computer Vision pipelines

## High-level features
1. Image loading and input validation
2. Four-corner document-boundary detection
3. Perspective correction using a homography
4. Color, grayscale, or adaptive-threshold enhancement
5. Output saving and command-line status messages

## Inputs and outputs
Input: one JPG/PNG image and command-line options.
Output: a perspective-corrected PNG and an enhanced PNG, plus status/error messages.

## Non-functional requirements
- Usability: options and help are exposed through a CLI.
- Reliability: invalid paths and unreadable images are handled with clear errors.
- Maintainability: detection, transformation, enhancement, and CLI logic are separated.
- Resource efficiency: the image used for contour search is resized when wide, while transformation uses original-resolution coordinates.
- Portability: uses Python, OpenCV, and NumPy on common desktop operating systems.
