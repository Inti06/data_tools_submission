FROM python:3.9-slim

WORKDIR /data_tools_submission

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Inti06/data_tools_submission

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "uber_pickups.py", "--server.port=8501", "--server.address=0.0.0.0"]