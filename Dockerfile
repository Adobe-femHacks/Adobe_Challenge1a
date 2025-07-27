FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY pdfs/ /app/pdfs/
COPY *.py /app/
COPY output/ /app/output/

# Create output directory if it doesn't exist
RUN mkdir -p /app/output

# Set environment variables
ENV PYTHONPATH=/app

# Command to run the extractor
ENTRYPOINT ["python", "main.py"]
