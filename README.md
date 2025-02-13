# Word Counter in Docker

## 📌 Overview
This is a Python console application that counts words in a sentence and saves the result in a file. It demonstrates **Docker containerization concepts**, including:

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

3. Run the container interactively and with volume mounting:
 ```bash
docker run -it --name mycounter -v ~/word_counter/data:/app/data word-counter
```
✅ You will be prompted to enter a sentence.

✅ The program will count the words in the sentence, display it, and save the result in word_count.txt.

4. Check the Saved File

To check the file inside the container:
 ```bash
docker start mycounter
docker exec -it mycounter bash
cat /app/data/word_count.txt
```

To check the file outside the container

First, exit the container

```bash
exit
```
Then, run:

```bash
cat ~/word_counter/data/word_count.txt
```

# ▶️ Usage
1. Input a sentence
2. Press the enter key
3. The word count of the sentence is displayed and saved to word_count.txt

Example:
1. Input a sentence: I am an amazing Software Engineer
2. Press the enter key
3. The word count is: 6
4. The word count of the sentence is displayed and saved to word_count.txt
   
# 🐋 Docker Concepts Used
The following Docker concepts are used:

- Base Image: A base image is the foundation of a Docker container. Uses python:3.9-slim for a lightweight container.
- Containerization: App runs in an isolated Docker environment.
- Persistent Storage: Docker volumes save data permanently.
- Tagging & Versioning: Version 1.0 tagged as:

```bash
docker tag word-counter word-counter:1.0
```

# 📸 Screenshots

Screenshot 1

![screenshot1](https://github.com/user-attachments/assets/f3dfcdb9-d33e-4425-b11d-b5d74b460ddb)

Screenshot 2

![screenshot2](https://github.com/user-attachments/assets/ceec931f-7617-4224-90ac-2386d5422352)

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





