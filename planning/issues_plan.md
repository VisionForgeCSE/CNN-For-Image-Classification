# Proposed issues – EN3150 Assignment 03

Every model issue touches exactly one model and depends only on shared issues (G*) or issues of the same model. Comparison issues (C*) read saved `results/*.json` only.

Pattern: title `[TN] …` = part N of the brief; labels `task-N` + workstream `wsN-…`; one branch `feat/<issue>-<slug>` and one PR per issue.

| ID | Owner | Labels | Status | Title | Branch |
|---|---|---|---|---|---|
| G1 | Shared | task-0, ws0-shared | open | [T0] Setup: requirements.txt (TensorFlow) and README | `feat/<#>-setup-requirements-readme` |
| D1 | Sandali0726 | task-1, ws0-shared | closed (done) | [T1] Dataset generation: choose, download, downscale to 64×64 and split 70/15/15 | `feat/<#>-dataset-generation` |
| D2 | Sandali0726 | task-1, ws0-shared | open | [T1] Dataset: update dataset information in the course sheet | `feat/<#>-dataset-sheet` |
| D3 | Sandali0726 | task-1, ws0-shared, report | open | [T1] Dataset: report section and figures | `feat/<#>-dataset-report` |
| G2 | Shared | task-0, ws0-shared | open | [T0] Results format convention for all models | `feat/<#>-results-format` |
| A1 | Model A owner | task-2, ws1-model-a | open | [T2] Model A: build the standard CNN architecture | `feat/<#>-model-a-build` |
| A2 | Model A owner | task-2, ws1-model-a | open | [T2] Model A: parameter / MAC table and design justification | `feat/<#>-model-a-params-macs` |
| A3 | Model A owner | task-3, ws1-model-a | open | [T3] Model A: optimizer and learning-rate comparison (Adam vs SGD vs SGD+Momentum) | `feat/<#>-model-a-optimizers` |
| A4 | Model A owner | task-4, ws1-model-a | open | [T4] Model A: final training (>= 20 epochs) and loss curves | `feat/<#>-model-a-train` |
| A5 | Model A owner | task-4, ws1-model-a | open | [T4] Model A: test-set evaluation (accuracy, confusion matrix, precision, recall) | `feat/<#>-model-a-evaluate` |
| A6 | Model A owner | task-4, ws1-model-a | open | [T4] Model A: model size on disk and results file | `feat/<#>-model-a-results` |
| A7 | Model A owner | task-4, ws1-model-a, report | open | [T4] Model A: report section | `feat/<#>-model-a-report` |
| B1 | Model B owner | task-2, ws2-model-b | open | [T2] Model B: build the lightweight depthwise-separable CNN architecture | `feat/<#>-model-b-build` |
| B2 | Model B owner | task-2, ws2-model-b | open | [T2] Model B: parameter / MAC table and design justification | `feat/<#>-model-b-params-macs` |
| B3 | Model B owner | task-3, ws2-model-b | open | [T3] Model B: optimizer and learning-rate comparison (Adam vs SGD vs SGD+Momentum) | `feat/<#>-model-b-optimizers` |
| B4 | Model B owner | task-4, ws2-model-b | open | [T4] Model B: final training (>= 20 epochs) and loss curves | `feat/<#>-model-b-train` |
| B5 | Model B owner | task-4, ws2-model-b | open | [T4] Model B: test-set evaluation (accuracy, confusion matrix, precision, recall) | `feat/<#>-model-b-evaluate` |
| B6 | Model B owner | task-4, ws2-model-b | open | [T4] Model B: model size on disk and results file | `feat/<#>-model-b-results` |
| B7 | Model B owner | task-4, ws2-model-b, report | open | [T4] Model B: report section | `feat/<#>-model-b-report` |
| M1 | MobileNetV2 owner | task-5, ws3-mobilenetv2 | open | [T5] MobileNetV2: load ImageNet-pretrained model with a 3-class head | `feat/<#>-mobilenetv2-build` |
| M2 | MobileNetV2 owner | task-5, ws3-mobilenetv2 | open | [T5] MobileNetV2: fine-tune and plot loss curves | `feat/<#>-mobilenetv2-finetune` |
| M3 | MobileNetV2 owner | task-5, ws3-mobilenetv2 | open | [T5] MobileNetV2: test-set evaluation, parameter count, size (MB) and results file | `feat/<#>-mobilenetv2-evaluate` |
| M4 | MobileNetV2 owner | task-5, ws3-mobilenetv2, report | open | [T5] MobileNetV2: report section | `feat/<#>-mobilenetv2-report` |
| E1 | EfficientNet-B0 owner | task-5, ws4-efficientnet | open | [T5] EfficientNet-B0: load ImageNet-pretrained model with a 3-class head | `feat/<#>-efficientnet-build` |
| E2 | EfficientNet-B0 owner | task-5, ws4-efficientnet | open | [T5] EfficientNet-B0: fine-tune and plot loss curves | `feat/<#>-efficientnet-finetune` |
| E3 | EfficientNet-B0 owner | task-5, ws4-efficientnet | open | [T5] EfficientNet-B0: test-set evaluation, parameter count, size (MB) and results file | `feat/<#>-efficientnet-evaluate` |
| E4 | EfficientNet-B0 owner | task-5, ws4-efficientnet, report | open | [T5] EfficientNet-B0: report section | `feat/<#>-efficientnet-report` |
| C1 | Comparison (one person) | task-4, ws5-comparison | open | [T4] Comparison: Model A vs Model B table and trade-off discussion | `feat/<#>-compare-a-vs-b` |
| C2 | Comparison (one person) | task-6, ws5-comparison | open | [T6] Final comparison: Model B vs MobileNetV2 vs EfficientNet-B0 | `feat/<#>-final-comparison` |
| R1 | Whole group | task-7, ws0-shared, report | open | [T7] Report assembly and submission | `feat/<#>-report-submission` |

---

## G1 – [T0] Setup: requirements.txt (TensorFlow) and README

**Labels:** task-0, ws0-shared

The current `requirements.txt` lists PyTorch, but all notebooks use TensorFlow/Keras.

### Tasks
- [ ] `requirements.txt`: tensorflow, numpy, pandas, matplotlib, scikit-learn, pillow, huggingface_hub, jupyter
- [ ] `.gitignore`: `.ipynb_checkpoints/`, large model files if needed
- [ ] README: project title, group members, dataset link, which notebook belongs to which model, run order (Dataset.ipynb first)

### Done when
`pip install -r requirements.txt` on a fresh environment lets every notebook run.

---
**Branch:** `feat/<this issue number>-setup-requirements-readme` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## D1 – [T1] Dataset generation: choose, download, downscale to 64×64 and split 70/15/15

**Labels:** task-1, ws0-shared · **Assignee:** Sandali0726 · **Create as closed**

Assignment task 1 (Data Preparation). Every model uses the output of this issue.

**File:** `Dataset.ipynb` · **Output:** `animal/train|val|test/<class>/`

### Tasks
- [x] **Choose the dataset** – [Jogitha/Animal_Image_Classification_Dataset](https://huggingface.co/datasets/Jogitha/Animal_Image_Classification_Dataset) (Hugging Face): cats, dogs, snakes, 1000 images each; suitable for low-resolution classification and **not CIFAR-10**
- [x] **Download** `cats_dogs_snakes.zip` with `HfFileSystem`; keep `.jpg/.jpeg`, skip `__MACOSX`; label = folder name; print images per class
- [x] **Downscale to 64×64** (assignment maximum): fix EXIF rotation, convert to RGB, centre-crop to square, resize with Lanczos (`ImageOps.fit`), save as PNG
- [x] **Before / after figure** – one original vs 64×64 image per class → `animal/before_after.png`
- [x] **Stratified split 70 / 15 / 15** with seed 42 (`train_test_split` twice) → train 2100 (700 per class), val 450 (150), test 450 (150)
- [x] Commit the `animal/train|val|test` folders so every member uses exactly the same images

### Done when
`animal/` contains 700 / 150 / 150 64×64 images per class and every model notebook reads from it.

**Status:** done before the issues were created (PRs #44, #45, #46).

---
**Branch:** `feat/<this issue number>-dataset-generation` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## D2 – [T1] Dataset: update dataset information in the course sheet

**Labels:** task-1, ws0-shared · **Assignee:** Sandali0726

Assignment task 1 – "update information about your dataset in this sheet".

### Tasks
- [ ] Fill in dataset name, link, number of classes, number of images, image size (64×64) and the split

### Done when
Group row in the sheet is complete.

### Depends on
[D1]

---
**Branch:** `feat/<this issue number>-dataset-sheet` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## D3 – [T1] Dataset: report section and figures

**Labels:** task-1, ws0-shared, report · **Assignee:** Sandali0726

**File:** `Dataset.ipynb`

### Tasks
- [ ] Grid of sample 64×64 images per class → `figures/samples.png`
- [ ] Bar chart of images per class in each split → `figures/class_distribution.png`
- [ ] Report paragraph: source, classes, original size, why 64×64 (edge sensor), preprocessing steps and split ([D1]); include `before_after.png`

### Done when
Section is added to the shared report document.

### Depends on
[D1]

---
**Branch:** `feat/<this issue number>-dataset-report` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## G2 – [T0] Results format convention for all models

**Labels:** task-0, ws0-shared

Agree once on how every model saves its numbers, so comparisons are built from files and no one needs another member's code.

**File:** `results/README.md`

### Tasks
- [ ] Each model writes `results/<id>.json` with id one of `model_a`, `model_b`, `sota_mobilenetv2`, `sota_efficientnetb0`
- [ ] Keys: `model`, `trainable_params`, `total_params`, `macs`, `size_kb`, `size_mb`, `epochs`, `time_per_epoch_s`, `optimizer`, `learning_rate`, `test_accuracy`, `precision_macro`, `recall_macro`, `f1_macro`, `confusion_matrix`, `history` (`loss`, `val_loss`, `accuracy`, `val_accuracy`)
- [ ] Figure names: `figures/<id>_curves.png`, `figures/<id>_confusion.png`
- [ ] Small example JSON in `results/README.md`

### Done when
`results/README.md` is merged.

---
**Branch:** `feat/<this issue number>-results-format` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A1 – [T2] Model A: build the standard CNN architecture

**Labels:** task-2, ws1-model-a

Assignment task 2 (Custom Architecture Design).

**File:** `ModelA.ipynb`

### Tasks
- [ ] Interleave standard `Conv2D` (3×3, ReLU) and `MaxPooling2D` (2×2) layers, e.g. 4 blocks with 32 / 64 / 128 / 256 filters
- [ ] Classifier head: GlobalAveragePooling (or Flatten) → Dense → Dropout → Dense(3, softmax)
- [ ] Load the data from `animal/` with `image_dataset_from_directory` (image_size 64×64, seed 42) and scale pixels to 0–1
- [ ] `build_model_a()` function so the model can be rebuilt with fresh weights
- [ ] `model.summary()` output in the notebook

Use the shared split in `animal/train`, `animal/val`, `animal/test` (64×64 RGB PNG, 700/150/150 images per class). Do not re-split or resize. No data augmentation (group decision).

### Done when
Model builds for input (64, 64, 3) and outputs 3 class probabilities; parameter count printed.

### Depends on
[D1]

---
**Branch:** `feat/<this issue number>-model-a-build` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A2 – [T2] Model A: parameter / MAC table and design justification

**Labels:** task-2, ws1-model-a

Assignment task 2 – "explicitly detail the network parameters … calculate the total trainable parameters … hardware-aware justification for activation functions".

**File:** `ModelA.ipynb`

### Tasks
- [ ] Table per layer: kernel size, filters / units, output shape, trainable parameters (calculated by formula, not only `model.summary()`)
- [ ] Multiply-accumulate operations (MACs) per layer and in total
- [ ] Check: hand-calculated total == `model.count_params()`
- [ ] Justify kernel sizes, filter counts and dense units
- [ ] Hardware-aware activation justification: ReLU is a single comparison (max(0, x)), no exponentials like sigmoid/tanh, cheap on microcontrollers / int8 hardware; softmax only once at the output

### Done when
Table and justification are in the notebook as markdown and ready to copy into the report.

### Depends on
[A1]

---
**Branch:** `feat/<this issue number>-model-a-params-macs` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A3 – [T3] Model A: optimizer and learning-rate comparison (Adam vs SGD vs SGD+Momentum)

**Labels:** task-3, ws1-model-a

Assignment task 3 (Optimizer Selection & Tuning) for Model A.

**File:** `ModelA.ipynb`

### Tasks
- [ ] Every run starts from a freshly built model with the same seed (fair comparison)
- [ ] Runs: chosen optimizer (e.g. Adam) vs **plain SGD** vs **SGD with momentum** (e.g. 0.9); same epochs for all
- [ ] Try at least 3 learning rates for the chosen optimizer and say why the final one was chosen
- [ ] Plot validation loss / accuracy of all runs → `figures/model_a_optimizers.png`
- [ ] Table: best val accuracy, epoch of best val accuracy, final val loss → `results/model_a_optimizers.csv`
- [ ] Explain the effect of the momentum parameter on convergence speed and stability (compare SGD vs SGD+Momentum curves)

Select on the **validation** set only – the test set is not used here.

### Done when
Figure, CSV and a short written explanation exist; the chosen optimizer + learning rate is stated.

### Depends on
[A1]

---
**Branch:** `feat/<this issue number>-model-a-optimizers` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A4 – [T4] Model A: final training (>= 20 epochs) and loss curves

**Labels:** task-4, ws1-model-a

Assignment task 4 – "train for at least 20 epochs and plot the training/validation loss curves".

**File:** `ModelA.ipynb`

### Tasks
- [ ] Train Model A with the optimizer / learning rate chosen in [A3] for at least 20 epochs
- [ ] Record the time of every epoch (Keras callback); report the mean excluding epoch 1
- [ ] Plot training vs validation **loss** (and accuracy) → `figures/model_a_curves.png`
- [ ] Comment on over/under-fitting seen in the curves
- [ ] Save the trained model → `results/model_a.keras`

### Done when
Curves figure and saved model exist; time per epoch is printed.

### Depends on
[A3]

---
**Branch:** `feat/<this issue number>-model-a-train` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A5 – [T4] Model A: test-set evaluation (accuracy, confusion matrix, precision, recall)

**Labels:** task-4, ws1-model-a

Assignment task 4 – evaluation part. The test set is used **only once**, here.

**File:** `ModelA.ipynb`

### Tasks
- [ ] Test accuracy
- [ ] Per-class and macro precision, recall (and F1) with `classification_report`
- [ ] Confusion matrix (counts and row-normalised) → `figures/model_a_confusion.png`
- [ ] Short discussion: which classes are confused (e.g. cats ↔ dogs) and why

### Done when
All metrics printed and the confusion-matrix figure saved.

### Depends on
[A4]

---
**Branch:** `feat/<this issue number>-model-a-evaluate` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A6 – [T4] Model A: model size on disk and results file

**Labels:** task-4, ws1-model-a

Values needed for the Model A vs Model B comparison table.

**File:** `ModelA.ipynb`

### Tasks
- [ ] Size on disk in KB of a clean copy without optimizer state (also report float32 = params×4 B and int8 = params×1 B estimates)
- [ ] Write `results/model_a.json` in the shared format of [G2]

Save results in the format defined in [G2]: `results/model_a.json`, `figures/model_a_curves.png`, `figures/model_a_confusion.png`.

### Done when
`results/model_a.json` contains params, MACs, size, time per epoch, test accuracy, precision, recall and the confusion matrix.

### Depends on
[A5] [G2]

---
**Branch:** `feat/<this issue number>-model-a-results` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## A7 – [T4] Model A: report section

**Labels:** task-4, ws1-model-a, report

Write the Model A part of the report.

### Tasks
- [ ] Architecture diagram / table and parameter calculation ([A2])
- [ ] Optimizer + learning-rate choice, SGD vs SGD+Momentum, effect of momentum ([A3])
- [ ] Loss curves and interpretation ([A4])
- [ ] Test metrics and confusion matrix with discussion ([A5])

### Done when
Section is added to the shared report document.

### Depends on
[A6]

---
**Branch:** `feat/<this issue number>-model-a-report` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B1 – [T2] Model B: build the lightweight depthwise-separable CNN architecture

**Labels:** task-2, ws2-model-b

Assignment task 2 (Custom Architecture Design).

**File:** `ModelB.ipynb`

### Tasks
- [ ] Replace the standard convolutions with **depthwise-separable** convolutions (`SeparableConv2D`, or `DepthwiseConv2D` + 1×1 `Conv2D`)
- [ ] Interleave with max-pooling; small classifier head ending in Dense(3, softmax)
- [ ] **Total trainable parameters must not exceed 100,000** – add an `assert model.count_params() <= 100_000`
- [ ] Load the data from `animal/` with `image_dataset_from_directory` (image_size 64×64, seed 42) and scale pixels to 0–1
- [ ] `build_model_b()` function so the model can be rebuilt with fresh weights
- [ ] `model.summary()` output in the notebook

Use the shared split in `animal/train`, `animal/val`, `animal/test` (64×64 RGB PNG, 700/150/150 images per class). Do not re-split or resize. No data augmentation (group decision).

### Done when
Model builds for input (64, 64, 3), outputs 3 class probabilities and has <= 100,000 trainable parameters.

### Depends on
[D1]

---
**Branch:** `feat/<this issue number>-model-b-build` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B2 – [T2] Model B: parameter / MAC table and design justification

**Labels:** task-2, ws2-model-b

Assignment task 2 – "explicitly detail the network parameters … calculate the total trainable parameters … hardware-aware justification for activation functions".

**File:** `ModelB.ipynb`

### Tasks
- [ ] Table per layer: kernel size, filters / units, output shape, trainable parameters (calculated by formula, not only `model.summary()`)
- [ ] Multiply-accumulate operations (MACs) per layer and in total
- [ ] Check: hand-calculated total == `model.count_params()`
- [ ] Justify kernel sizes, filter counts and dense units
- [ ] Hardware-aware activation justification: ReLU is a single comparison (max(0, x)), no exponentials like sigmoid/tanh, cheap on microcontrollers / int8 hardware; softmax only once at the output
- [ ] Show why depthwise-separable convs reduce MACs: k·k·C_in + C_in·C_out instead of k·k·C_in·C_out per output pixel

### Done when
Table and justification are in the notebook as markdown and ready to copy into the report.

### Depends on
[B1]

---
**Branch:** `feat/<this issue number>-model-b-params-macs` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B3 – [T3] Model B: optimizer and learning-rate comparison (Adam vs SGD vs SGD+Momentum)

**Labels:** task-3, ws2-model-b

Assignment task 3 (Optimizer Selection & Tuning) for Model B.

**File:** `ModelB.ipynb`

### Tasks
- [ ] Every run starts from a freshly built model with the same seed (fair comparison)
- [ ] Runs: chosen optimizer (e.g. Adam) vs **plain SGD** vs **SGD with momentum** (e.g. 0.9); same epochs for all
- [ ] Try at least 3 learning rates for the chosen optimizer and say why the final one was chosen
- [ ] Plot validation loss / accuracy of all runs → `figures/model_b_optimizers.png`
- [ ] Table: best val accuracy, epoch of best val accuracy, final val loss → `results/model_b_optimizers.csv`
- [ ] Explain the effect of the momentum parameter on convergence speed and stability (compare SGD vs SGD+Momentum curves)

Select on the **validation** set only – the test set is not used here.

### Done when
Figure, CSV and a short written explanation exist; the chosen optimizer + learning rate is stated.

### Depends on
[B1]

---
**Branch:** `feat/<this issue number>-model-b-optimizers` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B4 – [T4] Model B: final training (>= 20 epochs) and loss curves

**Labels:** task-4, ws2-model-b

Assignment task 4 – "train for at least 20 epochs and plot the training/validation loss curves".

**File:** `ModelB.ipynb`

### Tasks
- [ ] Train Model B with the optimizer / learning rate chosen in [B3] for at least 20 epochs
- [ ] Record the time of every epoch (Keras callback); report the mean excluding epoch 1
- [ ] Plot training vs validation **loss** (and accuracy) → `figures/model_b_curves.png`
- [ ] Comment on over/under-fitting seen in the curves
- [ ] Save the trained model → `results/model_b.keras`

### Done when
Curves figure and saved model exist; time per epoch is printed.

### Depends on
[B3]

---
**Branch:** `feat/<this issue number>-model-b-train` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B5 – [T4] Model B: test-set evaluation (accuracy, confusion matrix, precision, recall)

**Labels:** task-4, ws2-model-b

Assignment task 4 – evaluation part. The test set is used **only once**, here.

**File:** `ModelB.ipynb`

### Tasks
- [ ] Test accuracy
- [ ] Per-class and macro precision, recall (and F1) with `classification_report`
- [ ] Confusion matrix (counts and row-normalised) → `figures/model_b_confusion.png`
- [ ] Short discussion: which classes are confused (e.g. cats ↔ dogs) and why

### Done when
All metrics printed and the confusion-matrix figure saved.

### Depends on
[B4]

---
**Branch:** `feat/<this issue number>-model-b-evaluate` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B6 – [T4] Model B: model size on disk and results file

**Labels:** task-4, ws2-model-b

Values needed for the Model A vs Model B comparison table.

**File:** `ModelB.ipynb`

### Tasks
- [ ] Size on disk in KB of a clean copy without optimizer state (also report float32 = params×4 B and int8 = params×1 B estimates)
- [ ] Write `results/model_b.json` in the shared format of [G2]

Save results in the format defined in [G2]: `results/model_b.json`, `figures/model_b_curves.png`, `figures/model_b_confusion.png`.

### Done when
`results/model_b.json` contains params, MACs, size, time per epoch, test accuracy, precision, recall and the confusion matrix.

### Depends on
[B5] [G2]

---
**Branch:** `feat/<this issue number>-model-b-results` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## B7 – [T4] Model B: report section

**Labels:** task-4, ws2-model-b, report

Write the Model B part of the report.

### Tasks
- [ ] Architecture diagram / table and parameter calculation ([B2])
- [ ] Optimizer + learning-rate choice, SGD vs SGD+Momentum, effect of momentum ([B3])
- [ ] Loss curves and interpretation ([B4])
- [ ] Test metrics and confusion matrix with discussion ([B5])

### Done when
Section is added to the shared report document.

### Depends on
[B6]

---
**Branch:** `feat/<this issue number>-model-b-report` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## M1 – [T5] MobileNetV2: load ImageNet-pretrained model with a 3-class head

**Labels:** task-5, ws3-mobilenetv2

Assignment task 5 (SOTA fine-tuning).

**File:** `SOTA_MobileNetV2.ipynb`

### Tasks
- [ ] `tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet", input_shape=(64, 64, 3))`
- [ ] Add head: GlobalAveragePooling → Dropout → Dense(3, softmax)
- [ ] Correct preprocessing: `tf.keras.applications.mobilenet_v2.preprocess_input` (expects 0–255 pixels, maps to [-1, 1]); Keras will warn that 64×64 is not a standard size and load the 224 weights – this is expected
- [ ] Print total and trainable parameter counts

Use the shared split in `animal/train`, `animal/val`, `animal/test` (64×64 RGB PNG, 700/150/150 images per class). Do not re-split or resize. No data augmentation (group decision).

### Done when
Model builds and predicts shape (batch, 3) on one batch from `animal/train`.

### Depends on
[D1]

---
**Branch:** `feat/<this issue number>-mobilenetv2-build` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## M2 – [T5] MobileNetV2: fine-tune and plot loss curves

**Labels:** task-5, ws3-mobilenetv2

**File:** `SOTA_MobileNetV2.ipynb`

### Tasks
- [ ] Stage 1: freeze the backbone, train only the head (a few epochs)
- [ ] Stage 2: unfreeze (all or top layers), fine-tune with a low learning rate (e.g. 1e-4 / 1e-5); keep BatchNorm layers in inference mode
- [ ] Use the same train / val split as the custom models; early stopping on validation loss
- [ ] Record time per epoch; plot training vs validation loss → `figures/sota_m_curves.png`
- [ ] Save the model → `results/sota_m.keras`

### Done when
Curves and saved model exist.

### Depends on
[M1]

---
**Branch:** `feat/<this issue number>-mobilenetv2-finetune` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## M3 – [T5] MobileNetV2: test-set evaluation, parameter count, size (MB) and results file

**Labels:** task-5, ws3-mobilenetv2

Assignment task 5 – "record their performance metrics, specifically noting the total parameter count and model size (MB)".

**File:** `SOTA_MobileNetV2.ipynb`

### Tasks
- [ ] Test accuracy, precision, recall, F1, confusion matrix → `figures/sota_m_confusion.png`
- [ ] Total and trainable parameters; size on disk in **MB**; MACs at 64×64 (e.g. `tf.profiler` FLOPs / 2) if possible
- [ ] Write `results/sota_m.json` in the shared format of [G2]

### Done when
`results/sota_m.json` exists with all fields.

### Depends on
[M2] [G2]

---
**Branch:** `feat/<this issue number>-mobilenetv2-evaluate` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## M4 – [T5] MobileNetV2: report section

**Labels:** task-5, ws3-mobilenetv2, report

### Tasks
- [ ] Why MobileNetV2 is suitable for edge devices (key building blocks)
- [ ] Fine-tuning setup (frozen stage, unfrozen stage, learning rates, epochs)
- [ ] Curves, test metrics, confusion matrix, parameter count and size (MB)

### Done when
Section is added to the shared report document.

### Depends on
[M3]

---
**Branch:** `feat/<this issue number>-mobilenetv2-report` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## E1 – [T5] EfficientNet-B0: load ImageNet-pretrained model with a 3-class head

**Labels:** task-5, ws4-efficientnet

Assignment task 5 (SOTA fine-tuning).

**File:** `SOTA_EfficientNetB0.ipynb`

### Tasks
- [ ] `tf.keras.applications.EfficientNetB0(include_top=False, weights="imagenet", input_shape=(64, 64, 3))`
- [ ] Add head: GlobalAveragePooling → Dropout → Dense(3, softmax)
- [ ] Correct preprocessing: EfficientNet includes its own rescaling layer – feed raw 0–255 pixels, do **not** divide by 255
- [ ] Print total and trainable parameter counts

Use the shared split in `animal/train`, `animal/val`, `animal/test` (64×64 RGB PNG, 700/150/150 images per class). Do not re-split or resize. No data augmentation (group decision).

### Done when
Model builds and predicts shape (batch, 3) on one batch from `animal/train`.

### Depends on
[D1]

---
**Branch:** `feat/<this issue number>-efficientnet-build` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## E2 – [T5] EfficientNet-B0: fine-tune and plot loss curves

**Labels:** task-5, ws4-efficientnet

**File:** `SOTA_EfficientNetB0.ipynb`

### Tasks
- [ ] Stage 1: freeze the backbone, train only the head (a few epochs)
- [ ] Stage 2: unfreeze (all or top layers), fine-tune with a low learning rate (e.g. 1e-4 / 1e-5); keep BatchNorm layers in inference mode
- [ ] Use the same train / val split as the custom models; early stopping on validation loss
- [ ] Record time per epoch; plot training vs validation loss → `figures/sota_e_curves.png`
- [ ] Save the model → `results/sota_e.keras`

### Done when
Curves and saved model exist.

### Depends on
[E1]

---
**Branch:** `feat/<this issue number>-efficientnet-finetune` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## E3 – [T5] EfficientNet-B0: test-set evaluation, parameter count, size (MB) and results file

**Labels:** task-5, ws4-efficientnet

Assignment task 5 – "record their performance metrics, specifically noting the total parameter count and model size (MB)".

**File:** `SOTA_EfficientNetB0.ipynb`

### Tasks
- [ ] Test accuracy, precision, recall, F1, confusion matrix → `figures/sota_e_confusion.png`
- [ ] Total and trainable parameters; size on disk in **MB**; MACs at 64×64 (e.g. `tf.profiler` FLOPs / 2) if possible
- [ ] Write `results/sota_e.json` in the shared format of [G2]

### Done when
`results/sota_e.json` exists with all fields.

### Depends on
[E2] [G2]

---
**Branch:** `feat/<this issue number>-efficientnet-evaluate` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## E4 – [T5] EfficientNet-B0: report section

**Labels:** task-5, ws4-efficientnet, report

### Tasks
- [ ] Why EfficientNet-B0 is suitable for edge devices (key building blocks)
- [ ] Fine-tuning setup (frozen stage, unfrozen stage, learning rates, epochs)
- [ ] Curves, test metrics, confusion matrix, parameter count and size (MB)

### Done when
Section is added to the shared report document.

### Depends on
[E3]

---
**Branch:** `feat/<this issue number>-efficientnet-report` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## C1 – [T4] Comparison: Model A vs Model B table and trade-off discussion

**Labels:** task-4, ws5-comparison

Assignment task 4 – comparison part. Built **only from saved results files**, no training and no model code.

**File:** `Comparison.ipynb`

### Tasks
- [ ] Table: total parameters, model size on disk (KB), training time per epoch, test accuracy (also MACs)
- [ ] Bar chart of the four metrics → `figures/compare_AB.png`
- [ ] Discuss trade-offs of moving from standard to depthwise-separable convolutions (parameters / MACs vs accuracy vs training time)

### Done when
Table and discussion are ready for the report.

### Depends on
[A6] [B6]

---
**Branch:** `feat/<this issue number>-compare-a-vs-b` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## C2 – [T6] Final comparison: Model B vs MobileNetV2 vs EfficientNet-B0

**Labels:** task-6, ws5-comparison

Assignment task 6. Built **only from saved results files**.

**File:** `Comparison.ipynb`

### Tasks
- [ ] Table: parameters, size (MB), MACs, time per epoch, test accuracy, precision, recall
- [ ] Plot test accuracy vs parameters and vs size → `figures/accuracy_vs_cost.png`
- [ ] Discussion: custom sub-100k model from scratch vs pre-trained lightweight model – **accuracy, memory footprint, computational cost**; advantages and limitations of each

### Done when
Table, plot and discussion are ready for the report.

### Depends on
[B6] [M3] [E3]

---
**Branch:** `feat/<this issue number>-final-comparison` · open a PR into `main` with `Closes #<this issue number>` in the description.

---

## R1 – [T7] Report assembly and submission

**Labels:** task-7, ws0-shared, report

### Tasks
- [ ] Title page with group number, index numbers and names of all members
- [ ] GitHub repository link (assignment section 4)
- [ ] Merge sections: dataset ([D3]), Model A ([A7]), Model B ([B7]), comparison ([C1]), MobileNetV2 ([M4]), EfficientNet-B0 ([E4]), final comparison ([C2])
- [ ] Code: every notebook runs top to bottom and is commented
- [ ] Upload report PDF and code separately to Moodle as `<Groupno>_A03_EN3150`

### Done when
Submitted before the deadline.

### Depends on
[A7] [B7] [M4] [E4] [C1] [C2]

---
**Branch:** `feat/<this issue number>-report-submission` · open a PR into `main` with `Closes #<this issue number>` in the description.
