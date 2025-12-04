FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install build deps and runtime deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . /app

# Expose port
EXPOSE 5000

# Use gunicorn to serve the Flask app
CMD ["gunicorn", "weather_flask_app:app", "--bind", "0.0.0.0:5000", "--workers", "3"]
