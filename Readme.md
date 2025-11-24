
# 🤖 SessionBuilderBot

A powerful, secure and modern Telegram bot that generates **Pyrogram** and **Telethon** session strings — for user or bot accounts — using an intuitive step-by-step UI.

---

## 🛠 Features

✔ Generate session strings for:

* `Pyrogram v1` (User)
* `Pyrogram v2` (User & Bot)
* `Telethon` (User & Bot)

✨ Plus:

* Inline keyboard-driven UI
* Handles timeout, cancel, restart commands
* Logs never expose sensitive content
* Fully Dockerized & deploy-ready for **Railway**, **Heroku**, and **VPS**

---

## 📊 Admin Utilities

If you're the owner (via `OWNER_ID`), you get:

* `/stats` – Show total registered users
* `/broadcast [message]` – Send global message
* `/users` – List users with join timestamps (as `.txt` if > 50)

---

## 🚀 Deployment

<p align="center">
 Heroku
  Railway 
  Local<a /></a>
</p>

---

### 💻 Local Setup

```bash
git clone https://github.com/CertifiedCoders/StringGenerator
cd StringGenerator
cp sample.env .env  # and edit values inside

pip install -r requirements.txt
python main.py
```

---

### 🐿 Docker (Fastest Way)

```bash
docker build -t sessionbuilder .
docker run --env-file .env sessionbuilder
```

---

### ☁️ Railway / Heroku (Cloud Platforms)

```bash
railway init
railway up
```

Or click the deploy buttons above. Make sure you set:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=your_telegram_user_id
```

---

## 🧹 Folder Structure

| Path               | Description                            |
| ------------------ | -------------------------------------- |
| `main.py`          | Bot entry point                        |
| `StringGen/`       | Core handlers, modules & plugin logic  |
| └ `generate.py`    | Session generation logic               |
| └ `callbacks.py`   | Callback button handling               |
| └ `admin.py`       | Admin-only stats, broadcast, user list |
| └ `save_user.py`   | Saves user join info to MongoDB        |
| └ `database.py`    | Mongo client config                    |
| `utils.py`         | Async question-response logic          |
| `sample.env`       | Env variable example file              |
| `Dockerfile`       | Docker-ready container spec            |
| `Procfile`         | Needed for Railway/Heroku dyno startup |
| `requirements.txt` | Required Python dependencies           |

---

