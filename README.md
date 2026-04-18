# shodan-webui

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Minimal Flask web UI for [Shodan](https://www.shodan.io/) searches. Stores results in a local SQLite DB.

> ⚠️ **Personal tool / learning project.** Not production-grade.

## 🚀 Quick Start

```bash
git clone https://github.com/m4rv4x/shodan-webui.git
cd shodan-webui

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env and set SHODAN_API_KEY

python app.py
```

Open http://localhost:5000

## 🔑 Configuration

| Variable | Description |
|----------|-------------|
| `SHODAN_API_KEY` | Your Shodan API key (https://account.shodan.io) |

## 📄 License

[MIT](LICENSE) © [marvax](https://github.com/m4rv4x)
