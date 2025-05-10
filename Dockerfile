FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Create non-root user and switch to it
RUN useradd -ms /bin/bash taskyuser
USER taskyuser

# Copy source code and install dependencies
COPY --chown=taskyuser:taskyuser . .

RUN pip install .

# Start a bash shell by default
CMD ["/bin/bash"]
