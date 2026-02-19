FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    iputils-ping \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir .

# Entry point
ENTRYPOINT ["shadowbyte"]
CMD ["--help"]
