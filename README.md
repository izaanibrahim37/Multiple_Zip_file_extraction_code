# ZIP File Extractor Tool

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

## About

This Python script automates the extraction of `.zip` files from a specified directory. For each ZIP file found, it creates a separate folder named after the ZIP file (excluding the extension) and extracts all contents into that folder.

**Example:**

- **Input:** `photos.zip` containing `a.jpg`, `b.jpg`, `c.jpg`  
- **Output:** `photos/` folder containing `a.jpg`, `b.jpg`, `c.jpg`

It handles edge cases like invalid ZIP files, special characters in filenames, and preserves the internal folder structure of the archives.

---

## Tech Stack

- **Language:** Python 3.6+
- **Core Libraries:**
  - `zipfile`: For working with ZIP files
  - `os`: For file and folder handling
  - `sys`: For processing command-line arguments
- **Platform:** Optimized for **Windows** (but works on macOS/Linux too)

---

## How to Use

### Prerequisites
- Python 3.6 or newer installed
- Basic understanding of command-line usage

### Installation
1. Save the script as `extract_zips.py`
2. *(Optional)* Add the script to a directory in your system PATH for easier execution

---

## Usage Methods

### Method 1: Double-Click Execution
1. Place `extract_zips.py` inside the folder containing your `.zip` files
2. Double-click the script
3. All ZIP files in the current folder will be extracted
4. Press `Enter` to close the terminal when done

---

### Method 2: Command-Line Execution

```bash
# Run in current directory
python extract_zips.py

# Run on a specific directory
python extract_zips.py "C:\path\to\your\zip_files"

---
```

### **Author**  
**Izaan Ibrahim Sayed**  
Email: izaanahmad37@gmail.com  
GitHub: [github.com/izaanahmad37](https://github.com/izaanibrahim37) 


