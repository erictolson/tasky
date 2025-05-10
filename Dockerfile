FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd -ms /bin/bash taskyuser

# Copy source and fix permissions
COPY . .
RUN mkdir -p /app/build && chown -R taskyuser:taskyuser /app

# Switch to non-root user
USER taskyuser

# Add user's local bin to PATH so pip-installed CLI tools are available
ENV PATH="/home/taskyuser/.local/bin:$PATH"

# Install the CLI tool
RUN pip install .

# Default to bash shell
CMD ["/bin/bash"]
