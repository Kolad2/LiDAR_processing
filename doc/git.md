Обновление модулей впервые
```
git submodule update --init --recursive
```
Обновление локального репозитория
```
git pull --recurse-submodules
```
Для клонирования репозитория и всех подмодулей
```
git clone --recurse-submodules https://github.com/Kolad2/War3TestMap.git
```
Для сброса состояния локального репозитория
```
git reset --hard origin #Полный сброс
```
или
```
git reset --soft origin #Без удаления файлов
```
Добавление подмодуля
```
git submodule add https://github.com/name/module path/to/module
```

```
git submodule status
```