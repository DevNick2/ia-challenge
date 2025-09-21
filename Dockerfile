FROM python:3.12-slim-trixie

# deps do instalador do uv
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# instala o uv (binário vai para ~/.local/bin)
RUN curl -LsSf https://astral.sh/uv/0.8.19/install.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

# copie os manifests primeiro para aproveitar cache de camadas
COPY pyproject.toml uv.lock* ./

# instale deps (sem dev para imagem mais enxuta)
RUN uv sync --locked --no-dev

# agora copie o restante do projeto
COPY . /app

# entrypoint vazio é ok
ENTRYPOINT []

CMD ["uv", "run", "main.py"]