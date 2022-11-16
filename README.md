# MagistrKurskBot
[![GitHub](https://img.shields.io/github/license/dan-sazonov/MagistrKurskBot)](https://github.com/dan-sazonov/MagistrKurskBot/blob/master/legal_info/LICENSE.md)&nbsp;&nbsp;
![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red)<br>

**Чат-бот для телеграм-канала [КРОМО "Магистр"](https://t.me/magistrKursk).**

## 📝 Техническое задание
- [X] Переписать текущий функционал на aiogram
- [X] Создать бота на новом ID, оформить UI
- [X] Задеплоить бота, поменять ссылки в соцсетях Магистра
- [X] Запилить [тайного санту](./Идеи/санта.md)
- [ ] Разработать спам-фильтр, прикрутить к коментам
- [ ] Создать чат канала, прикрутить спам-фильтр к нему
- [ ] Обсудить новый функционал бота, возможности развития
- [ ] Автоматизировать добавление кнопок лайков/дизлайков к постам
- [ ] Сделать новые стикеры
<br>  
<b>❗ Дэдлайн: 22.12.2021</b>

## Стэк
- Python3 + aiogram
- **БД:** PostgreSQL
- **Облако:** Heroku

Разработка идет на ветке `master`. Деплой на Heroku автоматический, из ветки `deploy`. Перед запуском на локалке необходимо поставить пакеты из `requirements.txt` и создать переменные окружения `BOT_TOKEN` и `DATABASE_URL` со значением токена бота и URI бд соответственно.

## 🤝 Хотите сотрудничать?
Если вы обнаружили ошибку в коде, или знаете более оптимальное решение, откройте
[ишью](https://github.com/dan-sazonov/MagistrKurskBot/issues). Вы можете взять ишью, и сказать мне, что работаете над ним. 
Если вы хотите предложить свое решение, сделайте [пулл-реквест](https://github.com/dan-sazonov/MagistrKurskBot/pulls). 

## 👨‍💻 Автор
Автор репозитория и кода - [@dan-sazonov](https://github.com/dan-sazonov). <br>
**Связаться со мной:**<br>
[:airplane: Telegram](https://t.me/dan_sazonov) <br>
[:e-mail: Email](mailto:p-294803@yandex.ru) <br>

## 📜 Лицензия
Весь код распространяется по лицензии [GPL-3.0 License](https://github.com/dan-sazonov/MagistrKurskBot/blob/master/legal_info/LICENSE.md).<br>
Подробнее смотри в файле.
