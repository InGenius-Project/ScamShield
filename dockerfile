FROM dachxy/python-cuda:all

COPY . /app
WORKDIR /app

# Create a volume to store result model
VOLUME /app/result
# RUN pip install torch transformers argparse
# RUN pip install accelerate -U

CMD ["python3", "main.py"]
