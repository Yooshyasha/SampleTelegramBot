# 🚀 How to Install and Run Docker + Docker Compose

---

## 🔹 1. Installing Docker

### 📌 Linux (Ubuntu/Debian)

#### 1️⃣ Update packages

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2️⃣ Install dependencies

```bash
sudo apt install -y ca-certificates curl gnupg
```

#### 3️⃣ Add the official Docker repository

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```

#### 4️⃣ Install Docker and Docker Compose

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 5️⃣ Add the current user to the Docker group (to avoid using sudo)

```bash
sudo usermod -aG docker $USER
newgrp docker
```

#### 6️⃣ Verify that Docker is installed and running

```bash
docker --version
docker compose version
```

---

### 📌 Windows

#### 1️⃣ Download and Install Docker Desktop

Go to [this link](https://www.docker.com/products/docker-desktop/) to download Docker Desktop.

#### 2️⃣ After installation, reboot your PC

#### 3️⃣ Open the terminal and verify

```bash
docker --version
docker compose version
```

---

## 🔹 2. Running the Project with Docker Compose

#### 1️⃣ Navigate to the project folder

```bash
cd /path/to/project
```

#### 2️⃣ Start the containers

```bash
docker compose up -d
```

#### 3️⃣ If you need to rebuild the containers
```bash
docker compose up --build --force-recreate
```

#### 4️⃣ Stop and remove containers

```bash
docker compose down
```