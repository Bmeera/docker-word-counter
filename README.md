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
 
3. Build the Docker image:

docker build -t word-counter .

3. Run the container interactively:

docker run -it --name mycounter word-counter


