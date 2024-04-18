# Spark with MovieLens Dataset

## Prerequisites

- Python 3.x
- Apache Spark
- Docker (optional)

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yehoon17/Spark-with-MovieLens-Dataset.git .
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download MovieLens dataset's `ratings.csv` in `data/` directory

## Usage

### Running Locally

To run the Spark application locally:

1. Ensure you have Apache Spark installed and configured properly on your machine.

2. Run the main.py script:
   ```bash
   python src/main.py
   ```

   or to time it
   ```bash
   python src/main.py -t
   ```

   > Execution time of analyze_top_movies: 7.080772876739502 seconds
   > Execution time of analyze_top_movies: 6.9813642501831055 seconds
   > Execution time of analyze_top_movies: 6.7091310024261475 seconds
   

### Running with Docker

To run the Spark application with Docker:

1. Build the Docker image:
   ```bash
   docker build -t spark-app .
   ```

2. Run the Docker container:
   ```bash
   docker run --rm spark-app
   ```
