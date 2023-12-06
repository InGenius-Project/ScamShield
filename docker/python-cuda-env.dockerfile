FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y

RUN apt install -y software-properties-common 
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.11 python3-pip wget git

RUN pip install torch --index-url https://download.pytorch.org/whl/cu121
RUN pip install -U accelerate
RUN pip install argparse

RUN mkdir /temp
RUN git clone https://github.com/huggingface/transformers.git /temp/transformers
RUN cd /temp/transformers && pip install -e .