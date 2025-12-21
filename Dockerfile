FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libsdl2-2.0-0 \
    libsdl2-ttf-2.0-0 \
    fontconfig fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY test.py .

RUN pip install pygame==2.5.2

CMD ["python", "test.py"]