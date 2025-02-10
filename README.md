# Word Counter in Docker

## 📌 Overview
This is a simple Python console application that counts words in a sentence and saves the result in a file. It demonstrates **Docker containerization concepts**, including:

- Building and running containers
- Using Docker volumes for persistent data
- Managing containerized Python applications

## 🛠️ Setup Instructions
1. Clone the repository:
  ```bash
git clone https://github.com/Bmeera/docker-word-counter.git
cd docker-word-counter\
``` 
 
2. Build the Docker image:
 ```bash
docker build -t word-counter .
```
This creates a Docker image named word-counter.

3. Run the container interactively:
 ```bash
docker run -it --name mycounter word-counter
```
✅ You will be prompted to enter a sentence.
✅ The program will count the words and save the result in word_count.txt inside the container.

4. Check the Saved File

To check the file inside the container:
 ```bash
docker start mycounter
docker exec -it mycounter bash
cat word_count.txt
```
## 📂 Persistent Storage (Volume Mounting)

By default, the file is deleted when the container stops. To save the results permanently, use a Docker volume:
```bash
docker run -it --name mycounter -v ~/word_counter/data:/app/data word-counter
```
✅ Now, word_count.txt will be saved on your local machine at:
```bash
~/word_counter/data/word_count.txt
```
To verify, run:
```bash
cat ~/word_counter/data/word_count.txt
```
# 🐋 Docker Concepts Used

- Base Image: A base image is the foundation of a Docker container. Uses python:3.9-slim for a lightweight container.
- Containerization: App runs in an isolated Docker environment.
- Persistent Storage: Docker volumes save data permanently.
- Tagging & Versioning: Version 1.0 tagged as:

```bash
docker tag word-counter word-counter:1.0
```

# 📸 Screenshots

![screenshot2](https://github.com/user-attachments/assets/986729db-823e-4a74-bf33-58e65e834e09)


# ❌ How to Stop & Remove the Container

```bash
docker stop mycounter
docker rm mycounter
```
# 🛠️ Future Improvements
- Create a web-based version using Flask.

# 🤝 Contributing
Feel free to fork this repository and contribute improvements!
If you found this useful, ⭐ Star this repo!





