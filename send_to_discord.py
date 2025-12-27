import requests
import os

WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
GIF_URL = 'https://raw.githubusercontent.com/Ap4kk/limbo-daily-gif/main/current.gif'

data = {
    "content": f"Сегодняшний ключ Limbo!\n{GIF_URL}"
}

requests.post(WEBHOOK_URL, json=data)
