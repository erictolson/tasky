FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd -ms /bin/bash taskyuser

# Copy source code first (still as root)
COPY . .

# Fix permissions for build dir and /app
RUN mkdir -p /app/build && chown -R taskyuser:taskyuser /app

# Switch to non-root user
USER taskyuser

# Install your CLI tool
RUN pip install .

# Start a bash shell by default
CMD ["/bin/bash"]
