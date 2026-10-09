"""Command-line interface for the document scanner."""
import argparse
from pathlib import Path
import cv2
from .detection import find_document_corners
from .transform import warp_document
from .enhancement import enhance_document


def build_parser():
    parser = argparse.ArgumentParser(
        description="Detect, perspective-correct, and enhance a photographed document."
    )
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument("--output", default="output", help="Output directory (default: output)")
    parser.add_argument("--mode", choices=("color", "gray", "bw"), default="color",
                        help="Output enhancement mode")
    parser.add_argument("--no-warp", action="store_true",
                        help="Skip perspective correction and enhance the full image")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    source = Path(args.image)
    output_dir = Path(args.output)
    if not source.is_file():
        print(f"Error: input file not found: {source}")
        return 2
    image = cv2.imread(str(source))
    if image is None:
        print("Error: could not decode the image. Try JPG or PNG.")
        return 2
    output_dir.mkdir(parents=True, exist_ok=True)
    corners = None if args.no_warp else find_document_corners(image)
    if corners is not None:
        result = warp_document(image, corners)
        print("Document boundary detected; perspective correction applied.")
    else:
        result = image
        print("No clear four-corner boundary found; processing the full image.")
    enhanced = enhance_document(result, args.mode)
    stem = source.stem
    scan_path = output_dir / f"{stem}_scan.png"
    enhanced_path = output_dir / f"{stem}_enhanced.png"
    if not cv2.imwrite(str(scan_path), result):
        print("Error: failed to save scan output.")
        return 3
    if not cv2.imwrite(str(enhanced_path), enhanced):
        print("Error: failed to save enhanced output.")
        return 3
    print(f"Saved perspective-corrected image: {scan_path}")
    print(f"Saved enhanced image ({args.mode}): {enhanced_path}")
    return 0
