# ClearScan CV — Command-Line Document Scanner

## Overview
ClearScan CV is a small Computer Vision project that turns a photograph of a paper document into a perspective-corrected scan. It uses classical image-processing techniques: Gaussian blur, Canny edge detection, contour approximation, perspective transformation (homography), denoising, and adaptive thresholding.

## Features
- Detects a likely document boundary as a four-corner contour.
- Corrects perspective to create a top-down scan.
- Saves a scan image and a separately enhanced image.
- Supports color, grayscale, and black-and-white output modes.
- Handles missing/unreadable files and falls back to the full image when no clear boundary is found.
- Includes a small geometry unit test.

## Requirements
- Python 3.9 or newer
- pip
- OpenCV and NumPy

## Setup
Run these commands from the repository root.

### 1. Create a virtual environment (recommended)
Windows:
```bash
py -m venv .venv
.venv\\Scripts\\activate
```
macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Run
Place a JPG or PNG image in the project folder, then run:
```bash
python main.py sample.jpg --output output --mode bw
```
Modes: `color`, `gray`, `bw`. The program creates the output directory if needed and writes `sample_scan.png` and `sample_enhanced.png`.

For a full-image enhancement without perspective correction:
```bash
python main.py sample.jpg --output output --mode gray --no-warp
```

### 4. Test
```bash
python -m unittest discover -s tests -v
```

## Workflow
1. Read and validate the image.
2. Resize a working copy if the input is very wide.
3. Convert to grayscale, blur, detect edges, and find contours.
4. Approximate large contours to quadrilaterals.
5. Apply a perspective transform if a plausible boundary is found.
6. Denoise and optionally apply adaptive thresholding.
7. Save outputs and report their paths.

## Project structure
```text
cv_document_scanner/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── report.md
├── scanner/
│   ├── __init__.py
│   ├── cli.py
│   ├── detection.py
│   ├── enhancement.py
│   └── transform.py
└── tests/
    └── test_geometry.py
```

## Limitations
Boundary detection is heuristic and works best when the paper has visible contrast from the background. Busy backgrounds, shadows, curved pages, or multiple overlapping documents can reduce accuracy. The fallback processes the entire image instead of inventing a boundary.

## Academic note
Understand each module and run the program on your own sample images before submission. Describe the tests and results you actually observe; do not claim unperformed testing.
