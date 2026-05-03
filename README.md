# QR Code Generator

A simple Python script that converts any URL into a QR code image.

## Requirements

- Python 3.x
- qrcode library

Install the dependency:
```
pip install qrcode[pil]
```

## How to Run

```
python main.py
```

## How It Works

1. You enter a URL (e.g. `https://github.com`)
2. You enter a filename to save it as (e.g. `github`)
3. The script generates a QR code and saves it as a `.png` file in the same folder

The `.png` extension is added automatically if you forget to type it.