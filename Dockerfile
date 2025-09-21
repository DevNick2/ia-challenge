# =========================
# Stage 1: build deps layer
# =========================
FROM python:3.12-slim-trixie AS deps

# Evita .pyc e força stdout sem buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Instala deps básicos e remove cache do apt
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl ca-certificates build-essential \
 && rm -rf /var/lib/apt/lists/*

# Instala uv
RUN curl -LsSf https://astral.sh/uv/0.8.19/install.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

# Copia apenas arquivos de deps para aproveitar cache
COPY pyproject.toml uv.lock* ./

# Cria a venv do projeto e instala SÓ prod deps
# Dica: UV_LINK_MODE=copy evita symlink quebrado em alguns runtimes
ENV UV_LINK_MODE=copy
RUN uv sync --locked --no-dev

# =========================
# Stage 2: runtime
# =========================
FROM python:3.12-slim-trixie AS runtime

# Variáveis de execução
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/app" \
    PATH="/root/.local/bin/:$PATH" \
    UV_LINK_MODE=copy

# Cria usuário sem privilégios
RUN useradd -m -u 10001 appuser

WORKDIR /app

# Copia o ambiente Python (venv/.uv) e binários do uv do stage anterior
COPY --from=deps /root/.local /root/.local
COPY --from=deps /app/.venv /app/.venv
# Se seu projeto usa cache do uv em .uv, copie também:
# COPY --from=deps /app/.uv /app/.uv

COPY . /app

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 3000

ENTRYPOINT []

CMD ["uv", "run", "main.py"]
