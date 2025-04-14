# Use official Python base image for building stage
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app
ENV HOME=/app
#add  /app/.local/bin to PATH
#ENV PATH="/app/.local/bin:$PATH"

# Copy requirements and install dependencies and clean up unecessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

#remove unnecessary compiled python files

#RUN find . -name '*.pyc' -type f -delete
#Final stage
#FROM python:3.11-slim

# Set working directory
WORKDIR /app

#Copy dependencies from builder stage
#COPY --from=builder /app/.local /app/.local
RUN mkdir -p /app/model
COPY api/index.py /app
COPY api/model/svm_model.dill /app/model

# clean up unnecessary files
RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

# Ensure local Python packages are available
ENV PATH="/app/.local/bin:$PATH"


# Expose port (Flask default is 5000)
EXPOSE 5000

# Set entry point
CMD ["python", "index.py"]