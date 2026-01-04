# Sadak-Sahayak--Road-helper-

![Screenshot of Sadak Sahayak.](image.png)

# Installation Intructions:
    pip install -r requirement.txt

# Challenges Faced
1. Linux-Based Cloud Deployment Compatibility
    1.1 Challenge: Encountered ImportError: libGL.so.1 upon deploying to Streamlit Cloud because the server environment lacked the necessary graphics drivers for OpenCV.
    1.2 Solution: Implemented a packages.txt file to install libGL1 at the system level and switched to the opencv-python-headless library to ensure compatibility with a server environment.