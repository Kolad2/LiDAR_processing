sudo apt-get remove --purge '^nvidia-.*'
sudo apt-get autoremove
sudo apt-get autoclean

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
