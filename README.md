# Трекер цен с Claude


[![hexlet-check](https://github.com/igorshpindler-tech/vibecoding-claudecode-project-388/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/igorshpindler-tech/vibecoding-claudecode-project-388/actions)

Соберите на Claude-скиллах трекер цен: он сам следит за товарами и присылает в Telegram только значимые изменения.

Учебный проект Хекслета: https://ru.hexlet.io/programs/vibecoding-claudecode


## Стек

- Разное

## Установка

<!-- Опишите установку: клонирование, зависимости, переменные окружения -->

```bash
git clone https://github.com/igorshpindler-tech/vibecoding-claudecode-project-388.git
cd vibecoding-claudecode-project-388
```

## Использование

### Отправка сообщения в Telegram

Нужен Python 3. Дополнительные библиотеки не требуются.
Создайте бота через [BotFather](https://t.me/BotFather), получите токен
и отправьте боту `/start` в Telegram. Укажите ID нужного чата.

Пример запуска в PowerShell:

```powershell
$env:TELEGRAM_BOT_TOKEN = "<токен бота>"
$env:TELEGRAM_CHAT_ID = "<ID чата>"
python send.py "Цена на Daewoo DAST 3421Li изменилась!"
```

В Linux/macOS:

```bash
export TELEGRAM_BOT_TOKEN="<токен бота>"
export TELEGRAM_CHAT_ID="<ID чата>"
python3 send.py "Цена на Daewoo DAST 3421Li изменилась!"
```

Скрипт читает переменные окружения процесса; файл `.env` автоматически не загружается.
Токен не сохраняйте в коде или GitHub. При успехе скрипт завершится с кодом 0,
при ошибке — с кодом 1 (ошибки аргументов — 2).
Один запуск отправляет одно текстовое сообщение длиной до 4096 символов
через [Telegram Bot API](https://core.telegram.org/bots/api#sendmessage).

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
