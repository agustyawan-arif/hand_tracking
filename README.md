# Hand Tracking with Highlighted Areas

This Python script uses the Mediapipe library to perform hand tracking on a video feed or a video file. The script highlights specific areas on the screen and prints a message when the hand is detected within these areas.

## Dependencies

- Python 3.9.13
- OpenCV (`cv2`)
- Mediapipe
- argparse

## Installation

1. Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install required packages:

   ```bash
   pip install opencv-python mediapipe
   ```

## Usage

Run the script with the following command:

```bash
python e_sop.py --source "IMG_1114.mp4"
```

### Options

- `--source`: Specify the source of the video feed. Use an integer for a camera source (e.g., `0`) or a string for a video file path (e.g., `"IMG_1114.mp4"`).

## Highlighted Areas

The script defines three highlighted areas on the screen:
1. Center Area: `[226, 119, 375, 248]`
2. Left Area: `[87, 69, 172, 141]`
3. Right Area: `[439, 209, 510, 324]`

When a hand is detected within these areas, the script prints a corresponding message and outlines the area in red.

## Keyboard Commands

- Press 'q' to exit the script.

## Credits

This script is based on the Mediapipe library for hand tracking.
