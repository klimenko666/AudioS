# AudioS
### Накрутка музыки в ВКонтакте

1. Заходим в термукс или сmd на ПК и пишем следующие команды:
    ```shell script
    git clone https://github.com/klimenko666/AudioS
    cd AudioS
    pip install -r requirements.txt
    ```
2. Далее заходим в config.json и заполняем конфиг (
[Токен Kate Mobile](https://vkhost.github.io/))
4. Музыку которую хотим крутить закидываем в этот файл и называем audio.mp3
4. После чего пишем команду запуска:
    ```shell script
    python audio.py
    ```
5. Если будет ошибка, останавливаете скрипт ctrl+C и ждете несколько минут, потом можно обратно включать.
6. Задержка между музыками:
    ```shell script
    зависит от размера музыки(мин 75 КБ)
    ```

