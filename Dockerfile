FROM python:3.10.12-slim

COPY main.py main.py

ENTRYPOINT ["python", "main.py"]

