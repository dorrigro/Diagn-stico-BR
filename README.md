# Diagnóstico App

## Overview
Diagnóstico App is a Python application designed to monitor system resources such as CPU, memory, and disk usage. It provides real-time alerts when resource usage exceeds predefined thresholds, helping users manage their system performance effectively.

## Features
- Monitors CPU usage and alerts when it exceeds 80%.
- Monitors memory usage and alerts when it exceeds 80%.
- Monitors disk usage and alerts when it exceeds 90%.
- Displays system information including OS, architecture, and computer name.

## Requirements
To run this application, you need to install the following dependencies:

- `psutil`
- `keyboard`

You can install these dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Application
To run the application, execute the following command in your terminal:

```
python src/Diagnóstico.py
```

Follow the on-screen instructions to monitor your system's resource usage.

## Building the Executable
To compile the script into a standalone executable, you can use `PyInstaller`. Make sure to have it installed:

```
pip install pyinstaller
```

Then, you can build the executable by running:

```
pyinstaller --onefile src/Diagnóstico.py
```

This will create a standalone executable in the `dist` directory.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.