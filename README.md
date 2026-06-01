# TeleVault

Open-source Telegram media archiver designed for large-scale channel backups.

TeleVault can download and organize hundreds of thousands of Telegram media files while automatically recovering from interruptions.

## Features

- Resume downloads after interruptions
- Automatic reconnection
- Organize media by year and month
- Separate photos, videos, and documents
- Built for large Telegram channels
- Open source

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Create a Telegram API application at:

https://my.telegram.org

Copy:

- API ID
- API Hash

Rename:

config.example.py

to:

config.py

and enter your credentials.

## Usage

```bash
python download.py
```

## Folder Structure

downloads/

├── photos/
├── videos/
└── documents/

## Why TeleVault?

Telegram contains massive collections of images, videos, and documents spread across channels and groups.

Downloading large archives manually is unreliable and interruptions can force users to start over.

TeleVault was built to provide a simple, resumable, and organized way to archive Telegram media at scale.

## Disclaimer

This project is intended for lawful archival and backup purposes only.

Users are responsible for complying with Telegram's Terms of Service and all applicable laws.

## Roadmap

### v0.1
- [x] Resume downloads
- [x] Automatic reconnect
- [x] Media categorization

### v0.2
- [ ] Progress bar
- [ ] Download statistics
- [ ] Multi-channel downloads

### v0.3
- [ ] GUI application
- [ ] Docker support
- [ ] Export reports
