# File Analyzer (CLI)

A simple Python CLI script that reads a text file and prints a small report:
- total characters (including spaces and line breaks)
- total lines

## How to run

1. Make sure you have Python 3 installed.
2. Put your `.txt` file in the same folder (or provide a path).
3. Run:

```bash
python file_analyzer.py
```

## Example

Try with the included `sample.txt`:

Input:
- `sample.txt`

Output (example):
- Your file was successfully analyzed!
- Your file has X characters and Y lines.

## Notes
- Character count includes spaces and line breaks.
- The program handles missing files with `FileNotFoundError`.
