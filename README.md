# Customer Service Time Tracker

This project processes a video to track customers at a service counter and calculates the average service time. It uses computer vision techniques to detect and track customers in the video and provides insights into the service efficiency.

## Features
- Tracks the number of customers at a service counter.
- Calculates the time taken to serve each customer.
- Computes the average service time.
- Optimized for performance with frame sampling.

## Prerequisites
- Python 3.8 or higher
- OpenCV
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/customer-service-time-tracker.git
   cd customer-service-time-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your video file in the project directory.
2. Update the `video_path` variable in the script with the path to your video file.
3. Run the script:
   ```bash
   python service_time_analysis.py
   ```
4. The script will display the average service time in seconds.

## File Descriptions

- `service_time_analysis.py`: Main Python script for video processing and service time calculation.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: Documentation for the project.

## Example Output

```bash
Average service time: 16.27 seconds
```

## Notes
- The default average service time threshold is set to 16 seconds. Adjust this in the script if needed.
- Ensure the video has clear visibility of the service area for accurate tracking.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- OpenCV for computer vision processing
- NumPy for numerical computations
