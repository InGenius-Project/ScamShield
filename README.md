# Bert Sequence Classification Model
## Setup
> If you use docker, no need to setup.
1. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
2. <span style="color:red">(optional)</span> Enable GPU acceleration (cuda toolkit & CuDNN).  
    - Windows 
        1. Install cuda toolkit (winget)
        ```
        winget install -e --id Nvidia.CUDA
        ```
        2. Get the cuDNN on [Nvidia official website](https://developer.nvidia.com/cudnn)
    - Debain based linux
        1. Install cuda toolkit
        ```
        wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
        sudo dpkg -i cuda-keyring_1.1-1_all.deb
        sudo apt update
        sudo apt -y install cuda
        ```
        2. Get the cuDNN on [Nvidia official website](https://developer.nvidia.com/cudnn)
        3. May need to reboot your system
## How to use
- windows
    ```powershell
    python main.py
    ```
- linux
    ```bash
    python3 main.py
    ```
- docker
    ```bash
    docker build -t bert-model .
    docker run -i bert-model
    ```
    > Dockerfile will create a volume to store the trained model.
    - Specify docker volume
    ```bash
    docker run -i bert-model -v your/volume/path:/app/result
    ```
    or 
    ```bash
    docker run -i bert-model -v .:/app
    ```
    so you can change dataset and get result models more convenient.
## Optional Python Arguments
- `-d, --dataset` Specify dataset file to train the model. The data format should follow the below format. 
    ```json
    [
        [
            "Text HERE 1.", 1
        ],
        [
            "Text HERE 2.", 0
        ],
        [
            "Text HERE 3.", 2
        ],
    ]
    ```
    The number after text are labels
- `-o, --output` Specify the output path to save the trained model.