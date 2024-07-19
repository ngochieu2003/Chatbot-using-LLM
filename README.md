# Phenikaa Interdisciplinary Project - Structured Data App

## Getting started

Create your environment file using the file template in `environment.example` with the name `.env`.

First, setup the environment with poetry:

> **_Note:_** This step is not needed if you are using the dev-container.

```
poetry install
poetry shell
```

Then check the parameters that have been pre-configured in the `.env` file in this directory. (E.g. you might need to configure an `OPENAI_API_KEY` if you're using OpenAI as model provider).

Then, run the development server:

```
python main.py
```
