# PDF Page Extractor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple and efficient tool to extract specific pages from PDF documents while preserving OCR text layers. Features a user-friendly GUI and can be run as a standalone Windows executable.

## Features

- Extract custom page ranges from PDF files
- Preserves searchable OCR text in extracted PDFs
- Simple GUI interface with file browsing
- Standalone Windows executable (no Python installation required)
- Lightweight and fast

## Installation

### Option 1: Download Executable (Recommended for Windows Users)

1. Download `pdf_splitter.exe` from the [Releases](https://github.com/muaz1236/pdf-page-extractor/releases) page.
2. Run the executable directly - no installation needed!

### Option 2: From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/muaz1236/pdf-page-extractor.git
   cd pdf-page-extractor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python pdf_splitter.py
   ```

4. (Optional) Build your own executable:
   ```bash
   pip install pyinstaller
   pyinstaller --onefile pdf_splitter.py
   ```

## Usage

### GUI Mode (Default)

1. Launch the application (double-click `pdf_splitter.exe` or run `python pdf_splitter.py`)
2. Click "Browse" to select your input PDF file
3. Click "Browse" to choose output location and filename
4. Enter start and end page numbers (1-based)
5. Click "Extract Pages"

### Command-Line Mode (Advanced)

```bash
python pdf_splitter.py <input_pdf> <output_pdf> <start_page> <end_page>
```

Example:
```bash
python pdf_splitter.py document.pdf extracted.pdf 230 240
```

## Requirements

- Python 3.6+ (for source code)
- pypdf library
- Tkinter (usually included with Python)

## Building

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile pdf_splitter.py
```

The executable will be in the `dist/` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues, please open an issue on GitHub.
