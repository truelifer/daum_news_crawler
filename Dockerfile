FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-dev \
    python3-pip \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    vim \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install scrapy SQLAlchemy mysqlclient

RUN mkdir -p /workspace/daum_news_crawler
RUN git clone -b release --single-branch https://github.com/truelifer/daum_news_crawler.git /workspace/daum_news_crawler
WORKDIR /workspace/daum_news_crawler/daum_news_crawler

CMD ["scrapy", "crawl", "daum_news_crawler"]