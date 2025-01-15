# PurOpt - A Powerful HTTP Method Checker and Purger Tool

## Overview

PurOpt is an advanced HTTP method checker and cache purger tool designed for cybersecurity enthusiasts, penetration testers, and web administrators. It allows users to scan URLs for various HTTP methods, including OPTIONS and PURGE, helping identify vulnerabilities related to cache purging and server configurations. It provides valuable insights to ensure your server is secure and operates as expected.

![PurOpt Banner](https://github.com/b3tar00t/PurOpt/blob/main/img/banner.png)

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

### 1. Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/b3tar00t/PurOpt
cd PurOpt
```

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
python3 puropt.py
```
Upon running the tool, you will be prompted to choose between the following options:

Enter a Single URL: Provide a single URL to check.
Use a File of URLs: Provide a text file containing a list of URLs.
You'll also be prompted to specify a timeout and the number of threads to use, and you can choose whether to test for the **PURGE** method.

## Results Format

The results will be displayed in a neat format, showing the **OPTIONS** response and optionally the **PURGE** method status for each URL. 

Here’s an example of how the results may look:

![Example Results Image](https://github.com/b3tar00t/PurOpt/blob/main/img/output.png)

---

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) - see the [LICENSE](LICENSE) file for details.

---

## Author

**Creator:** b3tar00t

---

## Contributing

Feel free to fork the repository, open issues, or submit pull requests. Contributions are always welcome!

