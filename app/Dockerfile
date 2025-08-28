# === Build stage ===
FROM python:3.10-slim AS builder

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc libffi-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Remove tests, docs, and .pyc files to slim down image
RUN find /usr/local/lib/python3.10/site-packages -type d \( -name "tests" -o -name "test" -o -name "__pycache__" \) -exec rm -rf {} + && \
    find /usr/local/lib/python3.10/site-packages -name "*.pyc" -delete

# === Runtime stage ===
FROM python:3.10-slim

# Install runtime dependencies only
RUN apt-get update && \
    apt-get install -y --no-install-recommends libffi8 libgomp1 libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user for security
RUN useradd -m appuser

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/

# Copy application files
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/
COPY models/churn_model.pkl ./models/churn_model.pkl
COPY models/scaler.pkl ./models/scaler.pkl

# Document intended port (Heroku sets $PORT env var)
EXPOSE 5000

# Switch to non-root user
USER appuser

# Start Gunicorn with shell to evaluate $PORT
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-5000} --timeout 300 --workers 2 app:app"]