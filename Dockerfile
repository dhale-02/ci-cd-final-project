FROM python:3.9-slim

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY service/ ./service/

# Expose port
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=service:app
ENV PORT=8080

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
