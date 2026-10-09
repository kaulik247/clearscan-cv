# ClearScan CV — Project Report

## 1. Cover Page
**Project:** ClearScan CV — Command-Line Document Scanner  
**Subject:** Computer Vision  
**Implementation:** Python, OpenCV, NumPy  
**Student:** [Enter your name and registration number]  
**Institution:** VITyarthi / VIT Bhopal  
**Date:** [Enter submission date]

## 2. Introduction
Digitizing paper documents with a phone camera can introduce perspective distortion, uneven lighting, and noise. ClearScan CV demonstrates how classical Computer Vision can reduce these issues without requiring a trained neural network or internet access.

## 3. Problem Statement
Given a photograph of a paper document, identify a likely quadrilateral paper boundary, transform it into a front-facing view, and produce a more readable output image.

## 4. Objectives
- Implement a reproducible image-processing pipeline.
- Detect a plausible document contour.
- Apply perspective correction using a homography.
- Compare color, grayscale, and adaptive-threshold outputs.
- Provide a command-line interface with input validation.

## 5. Functional Requirements
1. Load a local image and reject invalid inputs.
2. Detect a large four-corner contour.
3. Rectify the document with a perspective transform.
4. Enhance the result in color, grayscale, or black-and-white mode.
5. Save output images and report paths to the terminal.

## 6. Non-functional Requirements
- Usability: self-documenting CLI help.
- Reliability: clear handling of missing/unreadable input.
- Maintainability: separate modules for detection, geometry, enhancement, and CLI.
- Efficiency: reduce image width during contour search.
- Portability: standard Python packages, no cloud dependency.

## 7. System Architecture
```text
User / Terminal
      |
      v
CLI + Input Validation
      |
      v
Image Loader (OpenCV)
      |
      v
Pre-processing -> Edge Detection -> Contour Approximation
      |                                |
      |                         Four corners found?
      |                                |
      |                         Perspective Warp
      |                                |
      +----------------<---------------+
      |
      v
Enhancement (Color / Gray / Adaptive Threshold)
      |
      v
PNG Outputs + Terminal Status
```

## 8. Design Diagrams

### 8.1 Use Case
```text
Actor: Student/User
  -> Select image path
  -> Choose output folder and enhancement mode
  -> Run document scan
  -> Inspect saved scan and enhanced images
```

### 8.2 Workflow
```text
Start -> Validate path -> Read image -> Detect corners
      -> [Found?] Yes: perspective warp
      -> [Found?] No: use full image
      -> Enhance -> Save two outputs -> End
```

### 8.3 Sequence Diagram
```text
User -> CLI: image path + mode
CLI -> OpenCV: read image
CLI -> Detector: find_document_corners(image)
Detector --> CLI: corners or None
CLI -> Transformer: warp_document(image, corners) [if found]
CLI -> Enhancer: enhance_document(image, mode)
CLI -> Filesystem: save scan and enhanced PNGs
CLI --> User: output paths / error
```

### 8.4 Component Diagram
```text
main.py
  -> scanner.cli
      -> scanner.detection
      -> scanner.transform
      -> scanner.enhancement
tests/test_geometry.py -> scanner.detection.order_points
```

### 8.5 Storage Design
No database is required. The input is read from the local filesystem and two PNG outputs are written to the chosen output directory. This keeps the prototype simple and avoids collecting user data.

## 9. Design Decisions and Rationale
- **Canny edges:** highlights strong boundaries that may outline paper.
- **Contour approximation:** reduces a contour to a small polygon; quadrilaterals are candidates for document corners.
- **Area threshold:** ignores small objects unlikely to be the main page.
- **Homography / perspective transform:** maps four source corners to a rectangular destination.
- **Adaptive threshold:** supports black-and-white output when lighting varies across the page.
- **Fallback:** if a reliable quadrilateral is not detected, process the full image and notify the user instead of crashing.

## 10. Implementation Details
The implementation is divided into small files: `cli.py` manages arguments and errors, `detection.py` locates and orders corners, `transform.py` calculates the output dimensions and applies the perspective transform, and `enhancement.py` implements denoising and output modes. `main.py` is the command-line entry point.

## 11. Screenshots / Results
Insert genuine screenshots of:
1. Terminal command and successful output paths.
2. Original input image.
3. Generated `_scan.png` and `_enhanced.png` files.
4. Unit test output.

Do not claim performance metrics or successful test results until you have run the project.

## 12. Testing Approach
- Geometry test: verify that four unordered points are consistently ordered.
- Valid-input test: run against a readable JPG/PNG.
- Invalid-path test: supply a nonexistent filename and verify a non-zero exit code.
- Mode test: run once each with `--mode color`, `--mode gray`, and `--mode bw`.
- Boundary fallback test: use an image without a clear page boundary and check the warning and output.

## 13. Challenges Faced
Likely challenges include shadows, low contrast between paper and background, cluttered scenes, and contour detection selecting a non-document quadrilateral. The current implementation uses contour area and polygon shape as simple heuristics; these do not guarantee correct detection in every scene.

## 14. Learnings and Key Takeaways
This project connects pre-processing, edge detection, contour analysis, geometric point ordering, homography, and image enhancement into a complete command-line workflow. It also demonstrates why fallback paths and explicit error handling matter in practical image-processing applications.

## 15. Future Enhancements
- Interactive corner selection when automatic detection fails.
- Rotation correction and shadow removal.
- Batch processing for multiple files.
- OCR integration as a separate optional stage.
- A larger test set with measured detection success rate.

## 16. References
- OpenCV documentation: https://docs.opencv.org/
- NumPy documentation: https://numpy.org/doc/
- OpenCV-Python tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
