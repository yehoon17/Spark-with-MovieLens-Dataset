# Use the official Apache Spark base image
FROM bitnami/spark:latest

# Copy the source code into the container
COPY . /opt/spark/work-dir

# Set the working directory
WORKDIR /opt/spark/work-dir

# Install any dependencies or libraries if needed
# For example, if you need additional Python packages, you can install them here using pip:
RUN pip install -r requirements.txt

# Run the main.py script when the container starts
CMD ["spark-submit", "--master", "local[*]", "src/main.py"]
