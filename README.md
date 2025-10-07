### App for works with Wordpress

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)

### Installation
Clone the repository
```bash
git clone https://github.com/stas-polos/chatbot.git
```

Change into the project directory
```bash
cd chatbot
```

### Configuration

Copy the appropriate file and rename it, removing the name ".dist"
```bash
cd .dist.env .env
```

Set configuration options to `.env`
* Settings for docker image
  * PYTHON_IMAGE_VERSION - version of python image (default: 3.12.6-slim-bullseye)
  * LLM_MODEL_IMAGE - version of target LLM model (default: ai/smollm2:360M-Q4_K_M)
* Settings of application
  * PORT - Application port (default: 8050)
* Settings for logging
  * LOG_LEVEL - level of logging

### Usage
The project includes Dockerfiles and docker-compose configuration for running your spiders in containers. 
For build docker container for local development using docker-compose, need run command:
```bash
docker compose -f compose.yaml up -d --build
```
For get list running compose projects, run command:
```bash
docker-compose ls
```
For get list running process in docker container, run command:
```bash
docker-compose top streamlit-ui
```

Connect to docker container
```bash
docker compose exec streamlit-ui bash
```
