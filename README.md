# Bert Sequence Classification Model
## Setup
> By using docker, you still need to install nvidia driver & some container toolkit 
1. Install requirements
    ```bash
    python setup.py
    ```
2. <span style="color:red">(optional)</span> Enable GPU acceleration (cuda toolkit & CuDNN).  
    ### Windows 
    1. Install cuda toolkit (winget)
        ```
        winget install -e --id Nvidia.CUDA
        ```
    2. Get the cuDNN on [Nvidia official website](https://developer.nvidia.com/cudnn)
    ### Debian based linux
    1. Install cuda toolkit
        ```
        wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
        sudo dpkg -i cuda-keyring_1.1-1_all.deb
        sudo apt update
        sudo apt -y install cuda
        ```
    2. Get the cuDNN on [Nvidia official website](https://developer.nvidia.com/cudnn)
    3. May need to reboot your system
    ### Docker [Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
    1. Install Nvidia Container toolkit
        ```bash
        curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
        && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
        && \
            sudo apt-get update
        ```
        ```bash
        sudo apt-get install -y nvidia-container-toolkit
        ```
    2. Configuring docker
        ```bash
        sudo nvidia-ctk runtime configure --runtime=docker
        ```
    3. Restart the Docker daemon
        ```bash
        sudo systemctl restart docker
        ```
    ### WSL
    - If you are using WSL for docker, please refer [this](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) to get done with your GPU driver.
## How to use
### windows
```powershell
python main.py
```
### linux
```bash
python3 main.py
```
### docker
```bash
docker build -t bert-model .
docker run -i bert-model --gpus all
```
> Dockerfile will create a volume to store the trained model.
- Specify docker volume
```bash
docker run -i bert-model --gpus all -v your/volume/path:/app/result
```
or 
```bash
docker run -i bert-model --gpus all -v .:/app
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