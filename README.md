# ПИНГ-ПОНГ (1 ИГРОК) 

Десктопная реализация классической игры Pong для одного игрока против компьютера. Написана на Python с использованием библиотеки Pygame.

Проект упакован в Docker-образ с GUI-поддержкой для запуска на Windows, macOS и Linux без установки дополнительных зависимостей.

---

## СТРУКТУРА РЕПОЗИТОРИЯ

ping-pong/

├── .gitignore

├── Dockerfile

├── README.md

└── requirements.txt

---

## ТРЕБОВАНИЯ

- Установленный Docker
- Поддержка GUI из контейнера:
  - **Windows/macOS:** Docker Desktop с GUI-режимом
  - **Linux:** доступ к X11-серверу

---

## СБОРКА И ЗАПУСК

### 1. Сборка образа

```bash
docker build -t ping-pong .
```
### 2. Запуск
```bash
docker run --rm -it \
  --name ping-pong-app \
  -e DISPLAY=host.docker.internal:0 \
  ping-pong
```
```bash
xhost +local:root

docker run --rm -it \
  --name ping-pong-app \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  ping-pong
```
Использование env (опционально)
```bash
docker run --rm -it --env-file .env ping-pong
```

