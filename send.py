"""Send a Telegram message using credentials from environment variables."""

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def send_message(text):
    """Send plain text to TELEGRAM_CHAT_ID using TELEGRAM_BOT_TOKEN."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        raise ValueError("Задайте TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID.")
    if not text.strip() or len(text) > 4096:
        raise ValueError("Сообщение должно содержать от 1 до 4096 символов.")

    request = Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps({"chat_id": chat_id, "text": text}).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=30) as response:
            result = json.load(response)
    except HTTPError as error:
        # Do not print the request URL: it contains the bot token.
        raise RuntimeError(f"Telegram вернул HTTP {error.code}.") from None
    except (URLError, OSError):
        raise RuntimeError(
            "Ошибка соединения с Telegram. Проверьте сеть. "
            "При тайм-ауте сообщение могло быть доставлено."
        ) from None
    except (ValueError, UnicodeError):
        raise RuntimeError("Telegram вернул некорректный ответ.") from None

    if not isinstance(result, dict) or result.get("ok") is not True:
        raise RuntimeError("Telegram не подтвердил отправку сообщения.")
    return result["result"]


def main():
    parser = argparse.ArgumentParser(description="Отправка сообщения в Telegram.")
    parser.add_argument("message", help="Текст сообщения (в кавычках).")
    args = parser.parse_args()
    try:
        send_message(args.message)
    except (ValueError, RuntimeError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1
    print("Сообщение отправлено.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
