sudo apt-get remove --purge '^nvidia-.*'
sudo apt-get autoremove
sudo apt-get autoclean
sudo apt --fix-broken install
sudo chmod 755 /путь/к/файлу
sudo chmod -R 755 /путь/к/директории


Удалите пакеты с пометкой rc:
```commandline
sudo dpkg --purge $(dpkg -l | awk '/^rc/ {print $2}')
```

Список райверов и рекомендации
```commandline
ubuntu-drivers devices
```
Автоматическая установка рекомендованных драйверов
```commandline
sudo ubuntu-drivers autoinstall
```


Введите команду для установки deb пакета
```
sudo dpkg -i имя_пакета.deb
```