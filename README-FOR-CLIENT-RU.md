# 🚀 Как установить и запустить Docker + Docker Compose

---

## 🔹 1. Установка Docker

### 📌 Linux (Ubuntu/Debian)

#### 1️⃣ Обновляем пакеты

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2️⃣ Устанавливаем зависимости

```bash
sudo apt install -y ca-certificates curl gnupg
```

#### 3️⃣ Добавляем официальный репозиторий Docker

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```

#### 4️⃣ Устанавливаем Docker и Docker Compose

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 5️⃣ Добавляем текущего пользователя в группу Docker (чтобы не писать sudo)

```bash
sudo usermod -aG docker $USER
newgrp docker
```

#### 6️⃣ Проверяем, что Docker установлен и работает

```bash
docker --version
docker compose version
```

---

### 📌 Windows

#### 1️⃣ Скачиваем и устанавливаем Docker Desktop

Перейдите по [ссылке](https://www.docker.com/products/docker-desktop/) для загрузки Docker Desktop.

#### 2️⃣ После установки перезагружаем ПК

#### 3️⃣ Открываем терминал и проверяем

```bash
docker --version
docker compose version
```

---

## 🔹 2. Запуск проекта в Docker Compose

#### 1️⃣ Перейдите в папку с проектом

```bash
cd /путь/к/проекту
```

#### 2️⃣ Запустите контейнеры

```bash
docker compose up -d
```

#### 3️⃣ Если нужно пересобрать контейнеры

```bash
docker compose up --build --force-recreate
```

#### 4️⃣ Остановить и удалить контейнеры

```bash
docker compose down
```