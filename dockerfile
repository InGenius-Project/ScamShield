FROM dachxy/python-cuda:all

COPY . /app
WORKDIR /app

# Create a volume to store result model
VOLUME /app/result

CMD ["python3", "main.py"]
