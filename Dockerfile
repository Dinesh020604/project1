FROM python:3.9-alpine
WORKDIR /app
COPY print_text.py /app/
CMD ["python", "print_text.py"]
