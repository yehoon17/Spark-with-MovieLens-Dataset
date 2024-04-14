# Spark with MovieLens Dataset

## Prerequisites

- Python 3.x
- Apache Spark
- Docker (optional)

## Setup

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/yehoon17/Spark-with-MovieLens-Dataset.git .
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download MovieLens dataset's `ratings.csv` in `data/` directory

## Usage

### Running Locally

To run the Spark application locally:

1. Ensure you have Apache Spark installed and configured properly on your machine.

2. Run the main.py script:
   ```
   python src/main.py
   ```

### Running with Docker

To run the Spark application with Docker:

1. Build the Docker image:
   ```
   docker build -t spark-app .
   ```

2. Run the Docker container:
   ```
   docker run --rm spark-app
   ```
