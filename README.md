# TeleVault

A resumable Telegram media archiver built with Telethon.

## Features

## Roadmap

- [x] Resume downloads
- [x] Automatic reconnect
- [x] Media categorization
- [ ] Progress bar
- [ ] Download statistics
- [ ] GUI application
- [ ] Docker support
- [ ] Multi-channel downloads

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