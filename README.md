# GIF to ASCII Art Converter

![Version](https://img.shields.io/badge/version-1.0.7-green.svg)

Convert GIF animations into ASCII art frames directly in your terminal using Python. This project includes a WebSocket server that allows real-time conversion and transmission of GIF frames to ASCII art, providing a unique visual experience.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Introduction

This Python application was inspired by [parrot.live](https://github.com/hugomd/parrot.live). It converts GIF animations into ASCII art frames, leveraging the capabilities of PIL (Pillow) for image processing and websockets for real-time transmission. Each frame of the GIF is transformed into ASCII characters, providing a unique visual experience within your terminal.

This project is also deployed on Heroku, serving as an educational resource for me to learn how to deploy and manage WebSocket-based applications in a cloud environment. By exploring the deployment process and WebSocket integration, you can gain practical experience in scaling and maintaining real-time applications. The deployed files are included in this repository for educational purposes. However, the only file required to use this tool is the `client.py`
file.

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- **Python**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **IDE**: An Integrated Development Environment (IDE) like [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), or another code editor of your choice.

### Steps


1. **Clone the repository:**
   ```bash
   git clone https://github.com/fettucci/gif-to-ascii.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd gif-to-ascii
    ```

3. **Install dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage
 **Run the Client:**
```bash
python3 client.py <your_gif.gif>
```

![Demo GIF](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY21rbmZvZWl6dDZmY2VqMHdscTk2bGFwYnA5dXViajBqc3Z2amd5aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QP0B4E9av5zPIfmJyX/giphy.gif)

## Contact

For any inquiries or suggestions, feel free to reach out:

- Email: akiradev02@icloud.com
- LinkedIn: https://www.linkedin.com/in/odai-alqahwaji-2bbb50304
#
Project Link: [GIF to ASCII Converter](https://github.com/fettucci/gif-to-ascii)
