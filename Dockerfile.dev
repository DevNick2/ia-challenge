FROM python:3.12-slim-trixie

# deps do instalador do uv
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# instala o uv (binário vai para ~/.local/bin)
RUN curl -LsSf https://astral.sh/uv/0.8.19/install.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv sync --locked --no-dev

COPY . /app

ENTRYPOINT []

CMD ["uv", "run", "main.py"]