# EN3150 Assignment 03 – Resource-constrained CNN for edge image classification

Group _no._ · EN3150 Pattern Recognition

| Name | Index no. | Part |
|---|---|---|
| _name_ | _index_ | Model A – standard CNN |
| _name_ | _index_ | Model B – depthwise-separable CNN (≤ 100k parameters) |
| _name_ | _index_ | MobileNetV2 (pre-trained, fine-tuned) |
| _name_ | _index_ | EfficientNet-B0 (pre-trained, fine-tuned) |

## Dataset

[Jogitha/Animal_Image_Classification_Dataset](https://huggingface.co/datasets/Jogitha/Animal_Image_Classification_Dataset)
(Hugging Face) – 3 classes: **cats, dogs, snakes**, 1000 images each.

- Downscaled to **64×64 RGB** (EXIF rotation fixed, centre-cropped, Lanczos resize) to emulate a low-resource sensor
- Stratified split with seed 42: **70 / 15 / 15** → train 2100, validation 450, test 450 (700 / 150 / 150 per class)
- No data augmentation
- The split is committed in `animal/train`, `animal/val`, `animal/test` – every model uses exactly these images

## Repository layout

```
Dataset.ipynb               download, downscale to 64×64, split 70/15/15  → animal/
ModelA.ipynb                Model A – standard CNN
ModelB.ipynb                Model B – depthwise-separable CNN
SOTA_MobileNetV2.ipynb      fine-tuned MobileNetV2
SOTA_EfficientNetB0.ipynb   fine-tuned EfficientNet-B0
Comparison.ipynb            tables and plots built from results/*.json only
animal/                     64×64 dataset (train / val / test)
results/                    one <id>.json + <id>.keras per model – format in results/README.md
figures/                    figures for the report
planning/                   proposed GitHub issues
```

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```

1. `Dataset.ipynb` – only needed to regenerate `animal/` (it is already in the repository).
2. Any model notebook – each one is independent and reads `animal/` directly.
3. `Comparison.ipynb` – after the model notebooks have written their `results/*.json`.

A GPU (e.g. Google Colab) is recommended; on CPU the custom models still train in a few minutes.
