# PurOpt - A Powerful HTTP Method Checker and Purger Tool

## Overview

PurOpt is an advanced HTTP method checker and cache purger tool designed for cybersecurity enthusiasts, penetration testers, and web administrators. It allows users to scan URLs for various HTTP methods, including OPTIONS and PURGE, helping identify vulnerabilities related to cache purging and server configurations. It provides valuable insights to ensure your server is secure and operates as expected.

![PurOpt Banner](path_to_banner_image.jp)

## Features

- **OPTIONS Method Detection**: Identifies all allowed HTTP methods for each URL.
- **PURGE Method Check**: Optionally checks if the `PURGE` method is allowed, which can be a security vulnerability if misconfigured.
- **Customizable Timeout & Threading**: Fine-tune the timeout period and number of threads for faster scanning.
- **File & Single URL Support**: Scan URLs provided directly or read from a file containing multiple URLs.
- **Multi-threading Support**: Accelerates the scanning process by running multiple threads concurrently.
- **Easy-to-Read Results**: Displays results in a clean and professional format with color coding to highlight important findings.
- **Cross-platform**: Compatible with both Windows and Unix-based systems.
- **Customizable User Interaction**: User-friendly prompts with input validation for better experience.

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed on your machine. You also need to install the following dependencies:

```bash
pip install -r requirements.txt
```
## Requirements

- `requests`: For making HTTP requests.
- `colorama`: For colored terminal output.
- `threading`: For multi-threaded execution.
- `queue`: For thread-safe queues.

## Usage

### Run the Tool

Once the installation is complete, you can run **PurOpt** via the command line:

```bash
python puropt.py
