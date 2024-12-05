title: How to run Tencent's Hunyuan Video model using Python
slug: how-to-run-tencents-hunyuan-video-model-using-python
pub: 2024-11-05 20:07:00
authors: arj
tags: 
category: web


## Table of content
- What is HunYan Video model?
- How does it differ from competitors?
- Architectural novelties
- How to install
- How to run?
- Docker recipe


## What is HunYan Video model?

[HunYuan](https://github.com/tencent/HunyuanVideo) is a new video model that supposedly outperforms SORA, the SOTA of video models.

## How does it differ from competitors?

HunYan is OpenSource, has 13 billion parameters, the largest for an open model to date and ranks better than closed-source versions.

## Architectural novelties

To achieve the above, HunYan innovated in these areas:

1. *Unified Dual-to-Single-Stream Design*: The model processes video and text tokens independently at first and later merges them for deeper multimodal understanding. This improves how visual and semantic information are aligned.

2. *Multimodal Large Language Model (MLLM) as Text Encoder*: Instead of traditional encoders like CLIP or T5, HunyuanVideo uses MLLM with a decoder-only structure, enhancing text-video alignment, complex reasoning, and image detail capture.

3. *3D VAE Compression*: The use of CausalConv3D compresses high-resolution videos into a compact latent space efficiently, allowing training on full-resolution, high-frame-rate videos without excessive computational cost.

4. *Prompt Rewrite Mechanism*: It fine-tunes user prompts into model-optimized instructions for better comprehension (Normal mode) or higher visual quality (Master mode), improving generation accuracy and adaptability.

## How to install

First clone the repo

```
git clone https://github.com/tencent/HunyuanVideo
```

enter

```
cd HunyuanVideo
```

Prepare conda environment

```
conda env create -f environment.yml
```

Activate
```
conda activate HunyuanVideo
```

Install dependencies
```
python -m pip install -r requirements.txt
```

Install flash attention v2 for acceleration (requires CUDA 11.8 or above)
```
python -m pip install git+https://github.com/Dao-AILab/flash-attention.git@v2.5.9.post1
```

## How to run?

Run this inside the folder

```
python sample_video.py \
    --video-size 720 1280 \
    --video-length 129 \
    --infer-steps 30 \
    --prompt "a cat is running, realistic." \
    --flow-reverse \
    --seed 0 \
    --use-cpu-offload \
    --save-path ./results
```

## Docker recipe

For Cuda 12, you can run these instructions
```
wget https://aivideo.hunyuan.tencent.com/download/HunyuanVideo/hunyuan_video_cu12.tar
docker load -i hunyuan_video.tar
docker image ls
docker run -itd --gpus all --init --net=host --uts=host --ipc=host --name hunyuanvideo --security-opt=seccomp=unconfined --ulimit=stack=67108864 --ulimit=memlock=-1 --privileged  docker_image_tag
```
