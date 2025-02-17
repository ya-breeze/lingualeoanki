# Import Words From LinguaLeo to Anki 2

### Description

[scroll down for description in Russian (пролистайте вниз для описания на русском языке)][1]

This is an add-on for [Anki][2] - powerful, intelligent flashcards, that makes remembering things easy via space repetition.

The add-on downloads your dictionary words from [LinguaLeo][3] - another great resource to learn English, and transforms them into Anki cards. Both 'English to Russian' and 'Russian to English' cards are created and they include pronunciation sound, image, transcription, and context.

![screenshot][27]

[LinguaLeo][3] has a user-friendly interface for adding new words to learn and a good [browser extension][4] to quickly look up for translations and add words to the dictionary in one click. But once you added the words and learned them via several [trainings][5], you need Anki to stick them in your memory forever with as little time and effort as possible. 

### Notice on recent update of LinguaLeo 
The [update][30] of Lingualeo on April 30, 2019 brought several [issues][31]. Current version of add-on (2.1.3) is fully compatible with the update. If you find some problems with your words, translations or pictures, please check on [Lingualeo][3] first. For the add-on problems please [create an issue on Github][10] or mail me at 4yourquestions {at} gmail.com. Thank you! 

### New in version 2.1:
#### Added
- Updated to a new API because of LinguaLeo update on 30.04.2019.
- Added option (radiobutton) for downloading "New" words.

#### Changed
- Renamed "Studied" and "Unstudied" options to "Learned" and "Learning".
- List of user dictionaries shows number of learned words to download (if "Learned" option is selected).
- A list of words to download by status ("New", "Learning" or "Learned") is loading faster now. 
- For new users of add-on, Russian to English cards don't require typing a correct answer by default.
- Fixed connection issue on MacOS.
- Fixed media downloading for long sentences.
- Fixed import error when there is no translation for the word (or phrase).

#### Removed
- Protocol setting in config, since LinguaLeo doesn't work with http anymore. 

### New in version 2.0:
#### Added
- Full support of Anki 2.1.x and Anki 2.0 (tested on Anki 2.0.52).
- Ability to import not only all words, but words from one or several user dictionaries (word sets).
- Log in and log out buttons and ability to stay logged in (by storing cookies in the user\_files folder).
- Select words to import: "Studied", "Unstudied" or "Any".
- Option to update existing notes (see also "Changed" section).
- Configuration file to store user's login and (optionally) password as well as other settings: stay logged in, protocol (http or https), remember the password.
- Six.py module for writing Python 2 and 3 compatible code easier.
- Changelog to keep updates and changes in one place.

#### Changed
- Fixed issues with downloading duplicates.
- Check for duplicates first before starting to import words (don't check for duplicates only if "Update existing notes" option is selected).
- Default protocol changed to https.
- Prevent multiple runs of the add-on at the same time.
- When exiting allow Anki's main window to close add-on window if no words are downloading.

#### Removed
- Option "missed words": it is not necessary anymore, because, by default, the add-on only downloads media for the words that are not in the deck.

The full [log of changes][6] can be found in the repository.

### Installation

The easiest (and preferable) way to install the add-on is by using the Anki's built-in add-ons managing system. In this case, it will be easy to [update][28] the add-on and get the latest version with new features and bug fixes. To install the add-on go to:  
(in Anki 2.1.x) "Tools" \> "Add-ons" \> "Get add-ons..."  
(in Anki 2.0) "Tools" \> "Add-ons" \> "Browse & Install"  
and input add-on's code: 1411073333. Restart Anki.

If for some reason you wish to install the add-on manually, download the archive with the latest version from the [repository on GitHub][7] ([for Anki 2.1.x][24], [for Anki 2.0][25]), open Anki on your computer, go to:  
(in Anki 2.1.x) "Tools" \> "Add-ons" \> "View Files"  
(in Anki 2.0) "Tools" \> "Add-ons" \> "Open Add-ons Folder"  
and put the content of the archive there. If you use Anki 2.1.x create an additional folder named "lingualeoanki" inside "addons21" folder and put the content of the archive there. Restart Anki.   
See the following gif for the details on manual installation in Anki 2.0 (with Russian captures):
[how to manually install][8]

#### Update

To update the add-on in Anki 2.1.x go to "Tools" > "Add-ons". Select the add-on and click "Check for updates." Click "Yes" to update and **restart Anki**, for changes to take effect.
In Anki 2.0 you need to repeat [installation][29] procedure and it will automatically replace the files. 

If after the update the add-on doesn't work as expected try:
- restarting Anki;
- clicking Log Out and authorizing again.
If it is still not working - try to delete the add-on and install it again. 

### Compatibility

The add-on works with Anki 2.1.x and Anki 2.0 (tested on 2.0.52). It is recommended to install the latest version of Anki 2.1, because the future releases of the add-on may not support outdated Anki 2.0.52.

### Usage

To run the add-on go to the "Tools" menu and click "Import from LinguaLeo." Enter your login and password. If you'd like to stay logged in choose "Stay logged in" option, and you can also save the password (stored in the configuration file), and click "Log in" button.
If the authorization is successful, you can choose the words to import: "All" (no matter what status), "New", "Learning" or "Learned".
If you updated media for some notes that had been previously imported, choose "Update existing notes" option.  

To download all user words click "Import all words" button. If you want to choose user dictionaries (word sets) to download words from: click "Import from dictionaries" button and hold Ctrl (or Cmd) to choose several dictionaries. Then click "Import."  
And that's all. You don't need to create decks, models, templates or anything else. The add-on will make it all for you. As simple as that. 

Please, be patient, it can take up to 10 minutes (or even more) to download 1000 words depending on the size of images and sounds and the speed of your internet connection.  
When finished press the "Exit" button.


### Additional

To rate this add-on and leave feedback, go to [its page][9], log in to your AnkiWeb account in top right corner and click "Rate this." If you'd like to see a new feature or found a bug, please, don't leave a comment on the add-on's page, instead copy an error message and [create an issue on GitHub][10], or send me an email to 4yourquestions [at] gmail.com. 

#### Features expected to appear in next releases:

##### User Interface:
- "Loading..." message to show user that list of words or list of dictionaries is being downloaded.
- Add Russian localization since beginners are more comfortable with native language.
- Additional configuration window to set up: 
   - what style of "Russian to English" cards to create: with typing answer or without;
   - download timeout, number of retries and sleep seconds;
   - choose from-to dates for importing words;
   - option to highlight the word in context;
   - show number of words in progress bar. 
- Improve error messages by narrowing down the reason.

##### Import :
- Import more than one translation (allow user to choose how many translations to import).
- Add user dictionaries (wordsets) as tags.
- Save problem words in json format and ask to retry downloading problem words only.
- Update not only media, but also translation(s), context, tags.
- Improve duplicate search to automatically update notes when any information was changed.


### Authors

Version 1: [Alex Trutanov][12], [original project on bitbucket][13].  
Version 2: [Victor Khaustov][14], [project on GitHub][7] or [on bitbucket][26].

This project is licensed under the GPL License - see the [LICENSE][11] file for details. 


### Acknowledgments

[Kosta Korenkov][32] for [Chrome extension][33] that exports LinguaLeo dictionary and for the help with transitioning to a new API.   
[Ilya Isaev][15] for [inspiration][16] and his project [LeoPort][17].  
[Serge][18] for duplicate search feature, support words with apostrophes and function to retry downloading words if initially failed.  
[Nikolay Bikov][19] for [PostMan Collection][20], [alfred-lingualeo][21] add-on and for helping to test on MacOS.  
And to all users who gave valuable comments and feedback and helped to test on different platforms.

##### Russian
[scroll up for description in English][22]

### Описание

Дополнение для [Anki][2] - программы для облегчения запоминания слов, выражений и любой другой информации с помощью интервальных повторений.

Дополнение позволяет в один клик скачать ваши сохранённые слова из [LinguaLeo][3], другой замечательной образовательной платформы для изучения и практики английского языка, и создать для них карточки Anki. Карточки создаются как в варианте "русский - английский", так и "английский - русский" и включают в себя изображения, транскрипцию, аудио с произношением и предложение с контекстом из ЛингваЛео.  

![screenshot][27]

[ЛингваЛео][3] имеет удобный интерфейс для добавления новых слов и неплохое [расширение для браузера][4] для перевода незнакомых слов и мгновенного добавления в словарь вместе с контекстом. Но после того, как вы добавили слова и изучили их с помощью нескольких [тренировок][5], Анки поможет вам никогда не забыть эти слова с минимальной затратой времени и усилий.

### Внимание! Обновление Lingualeo 30.04.2019
В связи с [обновлением][30] сервиса Lingualeo от 30 апреля 2019 возможны временные [неполадки][31] в его работе. В актуальной версия дополнения (2.1.3) полностью восстановлена его работа. Если вы заметили, что ваши слова, их переводы и картинки отображаются неправильно, сначала проверьте всё ли в порядке с вашим словарём и наборами слов на сайте [Lingualeo][3]. Если же проблема в аддоне - [создайте issue на Github][10] либо напишите мне на 4yourquestions {собачка} gmail.com. Спасибо! 

### Новое в версии 2.1:
####  Добавлено
- Аддон переехал на новый API в связи с обновлением LinguaLeo от 30.04.2019.
- Добавлена опция "New" для загрузки новых слов (как в сервисе LinguaLeo).

#### Изменено
- Изменены названия опций "Studied" и "Unstudied" на "Learned" и "Learning" соответственно.
- При выборе опции "Learned" и нажатии "Import from Dictionaries" список словарей показывает кол-во изученных слов.
- Загрузка списка слов из категорий "New", "Learning" и "Learned" занимает меньше времени (особенно для больших словарей).
- Для новых пользователей дополнения, создаваемые карточки не требуют печатать правильный ответ на английском. 
- Исправлена ошибка соединения на MacOS, связанная с отсутствием сертификатов.
- Исправлена загрузка медиафайлов для длинных предложений.
- Исправлена ошибка при загрузке в случае, когда у слова (или предложения) нет перевода.

#### Удалено
- Настройка протокола соединения в конфигурационном файле, так как LinguaLeo больше не работает с http.

### Новое в версии 2.0:
#### Добавлено
- Полная поддержка Anki 2.1.x и Anki 2.0 (тестировалось на Anki 2.0.52).
- Возможность импортировать не только все слова, но выбирать пользовательские словари (наборы) для импорта.
- Кнопки "Войти" и "Выйти", а также опция оставаться в системе (сохраняя cookies в папке user\_files).
- Возможность выбрать, какие слова импортировать: 'Изученные', 'Неизученные' или 'Любые'.
- Опция "Обновить существующие карточки", чтобы обновить медиафайлы.
- Конфигурационный файл для хранения логина, пароля (если выбрана соответствующая опция), а также других пользовательских настроек: оставаться в системе, протокол (http либо https). 
- Библиотека Six.py для удобного написания совместимого кода для Python 2 и 3.
- Changelog для ведения лога изменений программы.

#### Изменено
- Исправлена загрузка дубликатов.
- Прежде чем загружать медиафайлы, дополнение проверяет, были ли эти слова загружены ранее (и не загружает медиафайлы для существующих слов, если опция "Обновить существующие карточки" неактивна).
- Https протокол используется по-умолчанию.
- Невозможно запустить более одной копии дополнения одновременно.
- При выходе из Anki и отсутствии активных загрузок окно дополнения будет закрыто автоматически.

#### Удалено
- Опция "missed words", так как по умолчанию дополнение создаёт карточки и загружает медиафайлы только для слов, которые не были импортированы ранее.

Полный [список изменений][23] хранится в репозитории.

### Установка

Наиболее простой (и рекомендуемый) способ установки: с помощью системы управления дополнениями Anki. В таком случае вы сможете с лёгкостью обновлять дополнение и получать новые верии с новыми функциями и исправленными ошибками. Для этого выберите пункт меню программы:  
(для Anki 2.1.x) "Инструменты" (Tools) \> "Дополнения" (Add-ons) \> "Скачать дополнения" (Get Add-ons...)  
(для Anki 2.0) "Инструменты" (Tools) \> "Дополнения" (Add-ons) \> "Обзор и установка" (Browse & Install)  
введите код 1411073333 и перезапустите Anki.  

Если вы по какой-то причине хотите установить дополнение вручную: скачайте архив с исходным кодом из [репозитория на GitHub][7] ([для Anki 2.1.x][24], [для Anki 2.0][25]), откройте Anki на вашем компьютере, выберите пункт меню:  
(для Anki 2.1.x) "Инструменты" (Tools) \> "Дополнения" (Add-ons) и кликните на кнопку "Просмотреть файлы" (View Files)  
(для Anki 2.0) "Инструменты" (Tools) \> "Дополнения" (Add-ons) \> "Открыть папку с дополнениями" (Open Add-ons Folder)  
и скопируйте туда содержимое архива. Если вы используете Anki 2.1.x, создайте папку с именем "lingualeoanki" в папку "addons21" и скопируйте туда содержимое архива. Перезапустите программу.   
Гифка с наглядным изображением процесса ручной установки для Anki 2.0: [как установить дополнение вручную][8]

### Обновление

Чтобы обновить дополнение в Anki 2.1.x перейдите в "Инструменты" (Tools) > "Дополнения" (Add-ons). Выберите название дополнения и кликните на "Проверить обновления" (Check for updates). Нажмите "Да" для обновления и **перезапустите Anki**, чтобы изменения вступили в силу.
В Anki 2.0 вам следует повторить процедуру установки.

Если после обновления дополнение не работает, попробуйте:
- перезапустить Anki;
- нажать Log Out и ещё раз авторизоваться.
Если вышеперечисленные действия не помогают - попробуйте удалить дополнение и загрузить снова.

### Совместимость

Дополнение работает с новыми версиями (Anki 2.1.x), а также с Анки 2.0 (тестировалось на 2.0.52).
Рекомендуется установить Anki 2.1, актуальную версию программы, так как новые версии дополнения могут не поддерживать устаревшую версию Anki 2.0. 

### Как это работает?

После установки, чтобы импортировать ваши слова из LinguaLeo в Anki, откройте меню "Инструменты" (Tools) и выберите пункт "Import from LinguaLeo." Введите ваш логин и пароль для сервиса LinguaLeo. Если вы хотите оставаться в системе, выберите пункт "Stay logged in," и если вы хотите, чтобы дополнение запомнило пароль, выберите "Save password" (в таком случае пароль будет храниться в конфигурационном файле), после этого нажмите "Log in."
Если авторизация прошла успешно, вы можете выбрать какие слова импортировать (по текущему статусу, так же как в веб интерфейсе): "All" (все, в независимости от текущего статуса), "New" (только новые), "Learning" (на изучении) либо "Learned" (только изученные).
Если в некоторых словах вы обновили изображение или звук и хотите, чтобы эти изменения попали в Anki, выберите пункт "Update existing notes."  

Для того, чтобы импортировать слова из главного словаря (все пользовательские слова), нажмите кнопку "Import all words." Для того, чтобы выбрать наборы слов (пользовательские словари) для импорта, нажмите "Import from dictionaries" и выберите один или несколько наборов (удерживая клавишу Ctrl либо Cmd) и нажмите "Import."
Никаких моделей, шаблонов, колод создавать не нужно, дополнение сделает всю работу за вас. Проще некуда.

Наберитесь терпения. Импорт 1000 слов может занять 10 минут и более в зависимости от веса аудио с произношением и картинок и скорости вашего интернета.  
По окончании работы с дополнением нажмите "Exit."

### Кроме того

Для того, чтобы оценить дополнение и оставить комментарий перейдите на [его страницу][9], войдите в аккаунт AnkiWeb в правом верхнем углу и кликните "Rate this." Но если вы хотите новую функцию или обнаружили ошибку, пожалуйста, не оставляйте сообщение о ней в комментарии, а скопируйте текст ошибки и [создайте issue на GitHub][10], либо напишите на email: 4yourquestions [собачка] gmail.com. 

#### Ожидается в следующих версиях:

##### Пользовательский интерфейс:
- Сообщение "Загружается...", чтобы уведомлять пользователя, что список слов или словарей загружается (актуально для больших списков либо медленного интернета).
- Русский язык интерфейса, так как начинающим комфортнее работать с дополнением на родном языке.
- Дополнительное окно конфигурации для установки настроек импорта, таких как: 
   - какого типа карточки создавать: с вводом ответа или без (для русско-английских карточек);
   - таймаут запроса, количество попыток и продолжительность ожидания перед повторным скачиванием;
   - выбор промежутка времени для импортирования слов;
   - опция подсветки слова в контексте;
   - показывать количество слов во время загрузки. 
- Уточнить сообщения об ошибках.

##### Загрузка слов:
- Импортировать более одного перевода для слова (добавить соответствующую опцию в окне конфигурации).
- Добавлять пользовательские словари как теги.
- Сохранять проблемные слова в json формате и предлагать пользователю попытаться снова скачать только проблемные слова.
- Обновлять не только картинки и звуки, но также перевод(ы), контекст, теги.
- Исправить функцию поиска дупликатов, чтобы автоматически обновлять карточки при любых изменениях (не только медиа).

### Авторы

Версия 1: [Александр Трутанов][12], [оригинальный проект на bitbucket][13].  
Версия 2: [Виктор Хаустов][14], ссылка на проект [на GitHub][7] или [на bitbucket][26].

Свободное копирование и использование. Лицензия [GPL][11]. 

### Благодарности

[Kosta Korenkov][32] за [расширение для Chrome][33] для экспорта словаря LinguaLeo, а также за помощь с переездом на новый API.   
[Илья Исаев][15] за [вдохновение][16] и проект [LeoPort][17].  
[Serge][18] за функцию поиска дубликатов, поддержку слов с апострофом и функцию повторного скачивания слов.  
[Николай Байков][19] за [PostMan Collection][20], дополнение [alfred-lingualeo][21] и за помощь с тестированием на MacOs.  
А также всем, кто пользовался приложением, оставлял ценные комментарии и помогал с тестированием на различных платформах.

[1]:	#russian
[2]:	https://apps.ankiweb.net/
[3]:	https://lingualeo.com/
[4]:	https://lingualeo.com/ru/browserapps
[5]:	https://lingualeo.com/ru/training
[6]:	https://github.com/vi3itor/lingualeoanki/blob/master/CHANGELOG.md
[7]:	https://github.com/vi3itor/lingualeoanki/
[8]:	https://media.giphy.com/media/3oFzm4JamA2wb86yTS/giphy.gif
[9]:	https://ankiweb.net/shared/info/1411073333
[10]:	https://github.com/vi3itor/lingualeoanki/issues/new
[11]:	https://github.com/vi3itor/lingualeoanki/blob/master/LICENSE
[12]:	https://vk.com/trutanov.alex
[13]:	https://bitbucket.org/alex-altay/lingualeoanki
[14]:	https://github.com/vi3itor/
[15]:	https://github.com/relaxart
[16]:	https://habrahabr.ru/post/276495/
[17]:	https://github.com/relaxart/LeoPort
[18]:	https://bitbucket.org/pioneer/
[19]:	https://github.com/bikenik
[20]:	https://github.com/bikenik/alfred-lingualeo/blob/master/Lingua-Leo.postman_collection.json
[21]:	https://github.com/bikenik/alfred-lingualeo
[22]:	#description
[23]:	https://github.com/vi3itor/lingualeoanki/blob/master/CHANGELOG.md#russian
[24]:   https://github.com/vi3itor/lingualeoanki/blob/master/version_archive/for_anki_2_1/for_2_1_lingualeoanki-2-1-3.zip
[25]:   https://github.com/vi3itor/lingualeoanki/blob/master/version_archive/for_anki_2_0/for_2_0_lingualeoanki-2-1-3.zip
[26]:   https://bitbucket.org/vkhaustov/lingualeoanki/
[27]:   https://i.imgur.com/qSwZn5bl.png
[28]:   #update
[29]:   #installation
[30]:   https://corp.lingualeo.com/ru/2019/04/30/news/
[31]:   https://corp.lingualeo.com/ru/2019/05/01/spasibo-druzya-rabota-nad-oshibkami/
[32]:   https://github.com/troggy
[33]:   http://troggy.github.io/anki-leo/
