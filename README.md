# Трекер цен


[![hexlet-check](https://github.com/igorshpindler-tech/vibecoding-claudecode-project-388/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/igorshpindler-tech/vibecoding-claudecode-project-388/actions)

Трекер на навыках Codex собирает цены по запросу, сравнивает их с предыдущим днём и отправляет в Telegram значимые изменения. Целевой товар и комплектация описаны в [KNOWLEDGE.md](KNOWLEDGE.md).

Учебный проект Хекслета: https://ru.hexlet.io/programs/vibecoding-claudecode


## Стек

- Codex с доступом к веб-страницам и GitHub.
- Python 3 для отправки сообщений; дополнительные библиотеки не требуются.

## Структура проекта

```text
.
├── .agents/skills/
│   ├── tracker/SKILL.md
│   └── extract-price/SKILL.md
├── .github/workflows/
├── AGENTS.md
├── KNOWLEDGE.md
├── README.md
├── send.py
├── .env.example
├── .env                 # локальные настройки, исключены из Git
└── YYYY-MM-DD.json      # локальные копии результатов
```

`AGENTS.md` задаёт правила работы агента, `KNOWLEDGE.md` хранит параметры проекта, а навыки описывают процедуры. Правила значимости изменений читаются из актуального [KNOWLEDGE.md репозитория данных](https://github.com/igorshpindler-tech/tracker-data/blob/main/KNOWLEDGE.md); локальная копия правил не ведётся.

Codex обнаруживает навыки проекта в `.agents/skills/`. При совпадении имён с общими навыками инструкции проекта требуют читать локальные файлы. Эта структура рассчитана на Codex; подключение к Claude Code нужно настраивать отдельно.

## Установка

```bash
git clone https://github.com/igorshpindler-tech/vibecoding-claudecode-project-388.git
cd vibecoding-claudecode-project-388
```

Откройте папку проекта в Codex. Для сбора нужен доступ к сайтам магазинов, для сохранения — право записи в `igorshpindler-tech/tracker-data`.

Скопируйте `.env.example` в `.env` и заполните настройки Telegram. Существующий `.env` сохраняйте. Агент при запуске мониторинга передаёт настройки скрипту через окружение; сам скрипт файл не загружает.

## Использование

### Мониторинг

В чате Codex из папки проекта отправьте запрос:

```text
Используй локальный навык .agents/skills/tracker/SKILL.md и проверь цены по проекту.
```

Агент прочитает параметры товара, проверит предложения через локальный `extract-price`, сохранит результаты и выполнит сравнение. При первом запуске без данных за предыдущий день сравнение недоступно. Автоматическое расписание настраивается отдельно.

Для проверки одной карточки укажите URL и попросите использовать `.agents/skills/extract-price/SKILL.md`.

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
