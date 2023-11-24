# SecretSanta bot
[![GitHub](https://img.shields.io/github/license/dan-sazonov/sspb2)](https://github.com/dan-sazonov/sspb2/legal_info/LICENSE.md)&nbsp;&nbsp;
![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red)<br>

Это пропитанный ненавистью кусок вымученного кода, из проекта, который я запилил за одну ночь год назад. Все, что может быть ужасно - здесь ужасно. Попытка понять исходники или как-то доработать их, чревата необратимыми психическими травмами. **Ты предупрежден.**

- [Оригинал](https://github.com/dan-sazonov/MagistrKurskBot) этого мракобесия
- Однажды я перепишу все это, и будет универсальный [бот для Тайного Санты](https://github.com/dan-sazonov/secret-santa)

## Запуск
Это самая подробная инструкция, которую я только смог расписать. Сам бот был написан еще в 2021, и как-что там работает - я отказываюсь понимать. Чтобы что-то поменять, надо все переписывать с нуля. <br><br>
**Из ошибок:** число людей которые будут на встрече, или которые не будут - должно быть не меньше двух. Иначе, в жеребьевке они выпадут сами себе.<br><br>
**Условия работы:** я все проверил пошагово 24.11.2023 на Win10 MSEdge. Нет причин, чтобы оно не работало на других, но весь остальной софт надо ставить именно по ссылкам отсюда, как будет вести себя с другими версиями - не могу сказать

### 0. notabene
Командную строку, в которой будет запущен бот, все время его работы закрывать нельзя - упадет. Также нельзя выключать комп, на котором это все запущено. Нужно постоянное соединение с инетом.<br>
Если все-таки бот упал, повторяем заново шаг №7

### 1. Ставим гит
Экзешник [тут](https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe).<br>
Первый и предпоследний флаг не нужен, остальные должны стоять. На выборе редактора - выбрать nano. Это не обязательно, но если что, будет проще

### 2. Копируем репо
Открываем любую папку (желательно, на диске `C:`), нажимаем на свободном месте ПКМ и выбираем в выпавшей менюшке **Open git bash here**. Откроется консоль, в нее вставляем:
```
git clone https://github.com/dan-sazonov/sspb2.git
```
Нажимаем Enter. Если **"open git..."** не появилось, ошибка на шаге 1, переустанавливаем. Если посыпалось после ввода этой команды, скорее всего, нужны права админа

### 3. Ставим Python
Нужна версия 3.9.0. Если уже установлен, да еще и если другой версии, помолиться, чтобы не было конфликтов версий, и пропустить этот шаг.<br>
Экзешник [тут](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe).<br>
**По установке:** обязательно флажок **"Add python to PATH"** (сразу после открытия экзешика, внизу). После этого **Install now**. Если все ок, когда скачается, нажать **close**. Если будет что-то еще предлагать, игнорим.<br>
**Проверка:** открыть командную строку (через поиск винды, например) и ввести `python --version`. Если все ок, увидите `python 3.9.0`.<br>

### 4. Регаем бота
Это должен делать человек, который условно владелец бота, только у него будет доступ ко всему функционалу.<br>
- запускаем бот https://t.me/BotFather (нажимаем на кнопку Запустить)
- отправляем команду `/newbot`
- бот спрашивает про название, которое будет отображаться как имя бота, пишем
- дальше спрашивает про логин бота (что будет после @....). Название должно заканчиваться на "_bot"
- получаем сообщение, в котором указан токен бота. Никому не скидываем, иначе будет грустно. Лучше сохранить куда-то себе, чтобы случайно не потерять
- копируем логин бота (который мы писали на двумя шагами выше), и вставляем его в поиск телеги. Увидим только что созданного бота. Открываем диалог с ним и нажимаем на кнопку запустить. Бот ничего не ответит, так и задумано. Зачем так задумано - я не помню
- настраиваем оформление бота через BotFather: 
    ```
    /setdescription - change bot description
    /setabouttext - change bot about info
    /setuserpic - change bot profile photo
    ```
    здесь, думаю, все понятно

### 5. Накатываем БД
Вот тут предельно внимательно, одна ошибка - и ты ошибся
- качаем pga4 [отсюда](https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v6.21/windows/pgadmin4-6.21-x64.exe). Если не будет компонентов для vs, может спросить разрешение на установку, соглашаемся
- открываем **pg admin**, первый запуск может быть долгим. Его иконка должна была появиться в пуске, если нет - черз поиск
- задаем мастер-пароль и стараемся не забыть его
- нажимаем **"Add new server"**. На вкладке **"General"** в поле **"Name"** пишем `sspb2`, на вкладке **"Connection"** в поле **"Host address"** пишем `127.0.0.1`, в поле **"Password"** пишем `root`. Сохраняем.
- в менюшке слева должна появиться иконка слона, рядом с которым написано **sspb2**, а под ним желтый значок с надписью **"Databases (1)"**. Кликаем по нему пкм, выбираем **Create**, затем **Database...** и в поле **Database** пишем `sspb2`. Сохраняем.

### 6. Настраиваем бота
- Открываем папку, куда мы склонировали бота на шаге 2. Через текстовый редактор _(это капец как важно)_ открываем файл `config.py`
- Дальнейшая иснтрукция в нем. На этом этапе важно ничего не поломать, поэтому лучше открывать через редактор с подсветкой синтаксиса (vs code, notepad++, да хоть idle встроенный)
- Как закончили редактировать, сохранем и закрываем

### 7. Запускаем
- открываем командную строку, переходим в ней в директорию с ботом: адрес этой директории можно скопировать в проводнике, посмотрев свойства или в пути файла сверху. Вводим такую команду, путь меняем на свой:
    ```
    cd C:\Users\IEUser\Documents\sspb2
    ```
  если все ок, этот адрес будет написан слева перед `>`
- вводим команду
    ```
    python -m venv venv
    ```
    если вылетают ошибки, что-то не так на шаге №3
- вводим команду
    ```
    venv\Scripts\activate.bat
    ```
    если слева появилось `(venv)`, все ок
- вводим команду
    ```
    pip install -r requirements.txt
    ```
    если просит что-то обновить, не в коем случае не делаем этого
- момент истины - вводим:
    ```
    python main.py
    ```
    в консоли должны появится 3 записи лога, а админу бота придет сообщение, что бот запущен. Все, бот в режиме регистрации запущен. Теперь эту вкладку консоли закрывать нельзя)))
- а вот pgadmin уже можно закрыть, но лучше не надо, мало ли что

### 8. Проводим жеребьевку
- останавливаем бот - в окне командной строки нажимаем `Ctrl + C`
- удаляем файл `santa.py`
- переименовываем `_santa.py` в `santa.py`
- снова запускаем бот:
    ```
    python main.py
    ```
- открываем новую вкладку командной строки, повторяем шаги **7.1**; **7.3**
- вводим команду:
    ```
    python drawing.py
    ```

Каждые 30 секунд прога будет отправлять сообщения пользователям. После отправки будет падать **DeprecationWarning**, это хорошо, значит оно живое. Когда все сообщения будут отправлены, снова появится предложения ввода консоли (что-то типа `(venv) C:\Users\IEUser\Documents\sspb2 >`)<br>
После этого ЭТУ вкладку командной строки можно закрыть, другую не трогать!

### 9. Победа
После собрания, когда все подарки разданы, выключаем бота нажатием `Ctrl+C` в командной строке с основным процессом бота. Наконец-то закрываем ее

## 👨‍💻 Автор
Автор репозитория и кода - [@dan-sazonov](https://github.com/dan-sazonov). <br>
**Связаться со мной:**<br>
[:airplane: Telegram](https://t.me/dan_sazonov) <br>
[:e-mail: Email](mailto:p-294803@yandex.ru) <br>

## 📜 Лицензия
Весь код распространяется по лицензии [GPL-3.0 License](https://github.com/dan-sazonov/sspb2/legal_info/LICENSE.md).<br>
Подробнее смотри в файле.
