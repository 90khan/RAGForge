FROM python:3.11-slim

# -----------------------------------
# Environment
# -----------------------------------

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------------
# Working directory
# -----------------------------------

WORKDIR /app

# -----------------------------------
# Install dependencies
# -----------------------------------

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------------
# Copy source
# -----------------------------------

COPY . .

# -----------------------------------
# Create non-root user
# -----------------------------------

RUN useradd -m ragforge && \
    chown -R ragforge:ragforge /app

USER ragforge

# -----------------------------------
# Expose API
# -----------------------------------

EXPOSE 8000

# -----------------------------------
# Start API
# -----------------------------------

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]