# frontend/Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

# Ensure streamlit is installed
RUN pip install streamlit

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
