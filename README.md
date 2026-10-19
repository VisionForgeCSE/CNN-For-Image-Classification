# EN3150 Assignment 03 – Resource-constrained CNN for edge image classification

Group _no._ · EN3150 Pattern Recognition

| Name | Index no. | Part |
|---|---|---|
| Sandali Jayawardhana | 220282K | Model A – standard CNN |
| Rashmika Yapa | 220734B | Model B – depthwise-separable CNN (≤ 100k parameters) |
| Dinara De Silva | 220098C | MobileNetV2 (pre-trained, fine-tuned) |
| Thumul Dasun | 220094K | EfficientNet-B0 (pre-trained, fine-tuned) |

## Dataset

[EuroSAT RGB](https://zenodo.org/records/7711810) (Helber et al., IEEE JSTARS 2019) – Sentinel-2 satellite images,
**10 land-use classes**, 27,000 images of **64×64 RGB** (the maximum resolution the brief allows, so no downscaling).

- Classes: AnnualCrop, Forest, HerbaceousVegetation, Highway, Industrial, Pasture, PermanentCrop, Residential,
  River, SeaLake – 2,000 to 3,000 images each (largest / smallest = 1.5)
- Stratified split with seed 42: **70 / 15 / 15** → train 18,900, validation 4,050, test 4,050
- No data augmentation
- `Dataset.ipynb` downloads the data and builds `data/eurosat/train|val|test/<class>/`. The image folders are not
  committed; the split is committed in `data/eurosat_split.csv`, so every model uses exactly the same images

## Repository layout

```
Dataset.ipynb               download EuroSAT, check, split 70/15/15       → data/eurosat/
ModelA.ipynb                Model A – standard CNN
ModelB.ipynb                Model B – depthwise-separable CNN
SOTA_MobileNetV2.ipynb      fine-tuned MobileNetV2
SOTA_EfficientNetB0.ipynb   fine-tuned EfficientNet-B0
Comparison.ipynb            tables and plots built from results/*.json only
data/eurosat_split.csv      which image is in train / val / test (data/eurosat/ is rebuilt locally)
results/                    one <id>.json + <id>.keras per model – format in results/README.md
figures/                    figures for the report
planning/                   proposed GitHub issues
```

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```

1. `Dataset.ipynb` – run once: downloads EuroSAT (~95 MB) and builds `data/eurosat/` from the committed split.
2. Any model notebook – each one is independent and reads `data/eurosat/` directly.
3. `Comparison.ipynb` – after the model notebooks have written their `results/*.json`.

A GPU (e.g. Google Colab) is recommended; on CPU the custom models still train in a few minutes.
