FROM nikolaik/python-nodejs:python3.9-nodejs19
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
RUN pip install speedtest==0.0.1
RUN pip install speedtest-cli
CMD python ac.py
