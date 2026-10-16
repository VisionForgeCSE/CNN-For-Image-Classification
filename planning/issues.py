"""Proposed GitHub issues for EN3150 Assignment 03, organised so that every model issue
touches exactly one model.

    python planning/issues.py markdown   -> writes planning/issues_plan.md (copy-paste text)
    python planning/issues.py create     -> creates labels + issues with `gh api` (run on your own computer
                                            after `gh auth login`; writes planning/branches.md)

References like [A1] in a body are replaced with real issue numbers when the issues are created.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = "VisionForgeCSE/cnn-for-image-classification"

# Two labels per issue, like "[D3] … · day-3 · ws1-orchestrator":
#   task-N  -> which part of the assignment brief (title prefix [TN])
#   wsN-…   -> which workstream / owner, so each member filters their own issues
LABELS = {
    "task-0":           ("c5def5", "Project setup and shared conventions"),
    "task-1":           ("bfd4f2", "Brief 1 – Data preparation (64x64, 70/15/15)"),
    "task-2":           ("a2eeef", "Brief 2 – Custom architecture design"),
    "task-3":           ("7fd3ed", "Brief 3 – Optimizer selection & tuning"),
    "task-4":           ("5ab8e0", "Brief 4 – Custom model training & evaluation"),
    "task-5":           ("3c9bd6", "Brief 5 – SOTA fine-tuning & evaluation"),
    "task-6":           ("1d7fc9", "Brief 6 – Final comparison & trade-off discussion"),
    "task-7":           ("0b5cad", "Report assembly and submission"),
    "ws0-shared":       ("ededed", "Shared: setup, dataset, conventions, submission"),
    "ws1-model-a":      ("1f77b4", "Model A – standard CNN"),
    "ws2-model-b":      ("ff7f0e", "Model B – depthwise-separable CNN (<= 100k params)"),
    "ws3-mobilenetv2":  ("2ca02c", "Pre-trained MobileNetV2"),
    "ws4-efficientnet": ("9467bd", "Pre-trained EfficientNet-B0"),
    "ws5-comparison":   ("d62728", "Comparisons built from saved results only (no training)"),
    "report":           ("8c564b", "Report writing"),
}

DATA_NOTE = ("Use the shared split in `animal/train`, `animal/val`, `animal/test` "
             "(64×64 RGB PNG, 700/150/150 images per class). Do not re-split or resize. "
             "No data augmentation (group decision).")

RESULTS_NOTE = ("Save results in the format defined in [G2]: `results/{id}.json`, "
                "`figures/{id}_curves.png`, `figures/{id}_confusion.png`.")


def custom_model_issues(p, name, file, arch_tasks, arch_done, extra_justify):
    """Same 7-issue structure for Model A (p='A') and Model B (p='B')."""
    lab = [f"model-{p}"]
    rid = f"model_{p.lower()}"
    return [
        dict(id=f"{p}1", labels=lab, title=f"Model {p}: build the {name} architecture",
             body=f"""Assignment task 2 (Custom Architecture Design).

**File:** `{file}`

### Tasks
{arch_tasks}
- [ ] Load the data from `animal/` with `image_dataset_from_directory` (image_size 64×64, seed 42) and scale pixels to 0–1
- [ ] `build_model_{p.lower()}()` function so the model can be rebuilt with fresh weights
- [ ] `model.summary()` output in the notebook

{DATA_NOTE}

### Done when
{arch_done}

### Depends on
[D1]"""),
        dict(id=f"{p}2", labels=lab, title=f"Model {p}: parameter / MAC table and design justification",
             body=f"""Assignment task 2 – "explicitly detail the network parameters … calculate the total trainable parameters … hardware-aware justification for activation functions".

**File:** `{file}`

### Tasks
- [ ] Table per layer: kernel size, filters / units, output shape, trainable parameters (calculated by formula, not only `model.summary()`)
- [ ] Multiply-accumulate operations (MACs) per layer and in total
- [ ] Check: hand-calculated total == `model.count_params()`
- [ ] Justify kernel sizes, filter counts and dense units
- [ ] Hardware-aware activation justification: ReLU is a single comparison (max(0, x)), no exponentials like sigmoid/tanh, cheap on microcontrollers / int8 hardware; softmax only once at the output
{extra_justify}
### Done when
Table and justification are in the notebook as markdown and ready to copy into the report.

### Depends on
[{p}1]"""),
        dict(id=f"{p}3", labels=lab, title=f"Model {p}: optimizer and learning-rate comparison (Adam vs SGD vs SGD+Momentum)",
             body=f"""Assignment task 3 (Optimizer Selection & Tuning) for Model {p}.

**File:** `{file}`

### Tasks
- [ ] Every run starts from a freshly built model with the same seed (fair comparison)
- [ ] Runs: chosen optimizer (e.g. Adam) vs **plain SGD** vs **SGD with momentum** (e.g. 0.9); same epochs for all
- [ ] Try at least 3 learning rates for the chosen optimizer and say why the final one was chosen
- [ ] Plot validation loss / accuracy of all runs → `figures/{rid}_optimizers.png`
- [ ] Table: best val accuracy, epoch of best val accuracy, final val loss → `results/{rid}_optimizers.csv`
- [ ] Explain the effect of the momentum parameter on convergence speed and stability (compare SGD vs SGD+Momentum curves)

Select on the **validation** set only – the test set is not used here.

### Done when
Figure, CSV and a short written explanation exist; the chosen optimizer + learning rate is stated.

### Depends on
[{p}1]"""),
        dict(id=f"{p}4", labels=lab, title=f"Model {p}: final training (>= 20 epochs) and loss curves",
             body=f"""Assignment task 4 – "train for at least 20 epochs and plot the training/validation loss curves".

**File:** `{file}`

### Tasks
- [ ] Train Model {p} with the optimizer / learning rate chosen in [{p}3] for at least 20 epochs
- [ ] Record the time of every epoch (Keras callback); report the mean excluding epoch 1
- [ ] Plot training vs validation **loss** (and accuracy) → `figures/{rid}_curves.png`
- [ ] Comment on over/under-fitting seen in the curves
- [ ] Save the trained model → `results/{rid}.keras`

### Done when
Curves figure and saved model exist; time per epoch is printed.

### Depends on
[{p}3]"""),
        dict(id=f"{p}5", labels=lab, title=f"Model {p}: test-set evaluation (accuracy, confusion matrix, precision, recall)",
             body=f"""Assignment task 4 – evaluation part. The test set is used **only once**, here.

**File:** `{file}`

### Tasks
- [ ] Test accuracy
- [ ] Per-class and macro precision, recall (and F1) with `classification_report`
- [ ] Confusion matrix (counts and row-normalised) → `figures/{rid}_confusion.png`
- [ ] Short discussion: which classes are confused (e.g. cats ↔ dogs) and why

### Done when
All metrics printed and the confusion-matrix figure saved.

### Depends on
[{p}4]"""),
        dict(id=f"{p}6", labels=lab, title=f"Model {p}: model size on disk and results file",
             body=f"""Values needed for the Model A vs Model B comparison table.

**File:** `{file}`

### Tasks
- [ ] Size on disk in KB of a clean copy without optimizer state (also report float32 = params×4 B and int8 = params×1 B estimates)
- [ ] Write `results/{rid}.json` in the shared format of [G2]

{RESULTS_NOTE.format(id=rid)}

### Done when
`results/{rid}.json` contains params, MACs, size, time per epoch, test accuracy, precision, recall and the confusion matrix.

### Depends on
[{p}5] [G2]"""),
        dict(id=f"{p}7", labels=lab + ["report"], title=f"Model {p}: report section",
             body=f"""Write the Model {p} part of the report.

### Tasks
- [ ] Architecture diagram / table and parameter calculation ([{p}2])
- [ ] Optimizer + learning-rate choice, SGD vs SGD+Momentum, effect of momentum ([{p}3])
- [ ] Loss curves and interpretation ([{p}4])
- [ ] Test metrics and confusion matrix with discussion ([{p}5])

### Done when
Section is added to the shared report document.

### Depends on
[{p}6]"""),
    ]


def sota_issues(p, label, arch, keras_cls, file, preprocess):
    rid = f"sota_{p.lower()}"
    lab = [label]
    return [
        dict(id=f"{p}1", labels=lab, title=f"{arch}: load ImageNet-pretrained model with a 3-class head",
             body=f"""Assignment task 5 (SOTA fine-tuning).

**File:** `{file}`

### Tasks
- [ ] `tf.keras.applications.{keras_cls}(include_top=False, weights="imagenet", input_shape=(64, 64, 3))`
- [ ] Add head: GlobalAveragePooling → Dropout → Dense(3, softmax)
- [ ] Correct preprocessing: {preprocess}
- [ ] Print total and trainable parameter counts

{DATA_NOTE}

### Done when
Model builds and predicts shape (batch, 3) on one batch from `animal/train`.

### Depends on
[D1]"""),
        dict(id=f"{p}2", labels=lab, title=f"{arch}: fine-tune and plot loss curves",
             body=f"""**File:** `{file}`

### Tasks
- [ ] Stage 1: freeze the backbone, train only the head (a few epochs)
- [ ] Stage 2: unfreeze (all or top layers), fine-tune with a low learning rate (e.g. 1e-4 / 1e-5); keep BatchNorm layers in inference mode
- [ ] Use the same train / val split as the custom models; early stopping on validation loss
- [ ] Record time per epoch; plot training vs validation loss → `figures/{rid}_curves.png`
- [ ] Save the model → `results/{rid}.keras`

### Done when
Curves and saved model exist.

### Depends on
[{p}1]"""),
        dict(id=f"{p}3", labels=lab, title=f"{arch}: test-set evaluation, parameter count, size (MB) and results file",
             body=f"""Assignment task 5 – "record their performance metrics, specifically noting the total parameter count and model size (MB)".

**File:** `{file}`

### Tasks
- [ ] Test accuracy, precision, recall, F1, confusion matrix → `figures/{rid}_confusion.png`
- [ ] Total and trainable parameters; size on disk in **MB**; MACs at 64×64 (e.g. `tf.profiler` FLOPs / 2) if possible
- [ ] Write `results/{rid}.json` in the shared format of [G2]

### Done when
`results/{rid}.json` exists with all fields.

### Depends on
[{p}2] [G2]"""),
        dict(id=f"{p}4", labels=lab + ["report"], title=f"{arch}: report section",
             body=f"""### Tasks
- [ ] Why {arch} is suitable for edge devices (key building blocks)
- [ ] Fine-tuning setup (frozen stage, unfrozen stage, learning rates, epochs)
- [ ] Curves, test metrics, confusion matrix, parameter count and size (MB)

### Done when
Section is added to the shared report document.

### Depends on
[{p}3]"""),
    ]


ISSUES = [
    # ---------------- shared ----------------
    dict(id="G1", labels=["shared"], title="Setup: requirements.txt (TensorFlow) and README",
         body="""The current `requirements.txt` lists PyTorch, but all notebooks use TensorFlow/Keras.

### Tasks
- [ ] `requirements.txt`: tensorflow, numpy, pandas, matplotlib, scikit-learn, pillow, huggingface_hub, jupyter
- [ ] `.gitignore`: `.ipynb_checkpoints/`, large model files if needed
- [ ] README: project title, group members, dataset link, which notebook belongs to which model, run order (Dataset.ipynb first)

### Done when
`pip install -r requirements.txt` on a fresh environment lets every notebook run."""),
    # ---------------- dataset (assignment task 1) ----------------
    dict(id="D1", labels=["data"], assignee="Sandali0726", closed=True,
         title="Dataset generation: choose, download, downscale to 64×64 and split 70/15/15",
         body="""Assignment task 1 (Data Preparation). Every model uses the output of this issue.

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

**Status:** done before the issues were created (PRs #44, #45, #46)."""),
    dict(id="D2", assignee="Sandali0726", labels=["data"], title="Dataset: update dataset information in the course sheet",
         body="""Assignment task 1 – "update information about your dataset in this sheet".

### Tasks
- [ ] Fill in dataset name, link, number of classes, number of images, image size (64×64) and the split

### Done when
Group row in the sheet is complete.

### Depends on
[D1]"""),
    dict(id="D3", assignee="Sandali0726", labels=["data", "report"], title="Dataset: report section and figures",
         body="""**File:** `Dataset.ipynb`

### Tasks
- [ ] Grid of sample 64×64 images per class → `figures/samples.png`
- [ ] Bar chart of images per class in each split → `figures/class_distribution.png`
- [ ] Report paragraph: source, classes, original size, why 64×64 (edge sensor), preprocessing steps and split ([D1]); include `before_after.png`

### Done when
Section is added to the shared report document.

### Depends on
[D1]"""),
    dict(id="G2", labels=["shared"], title="Results format convention for all models",
         body="""Agree once on how every model saves its numbers, so comparisons are built from files and no one needs another member's code.

**File:** `results/README.md`

### Tasks
- [ ] Each model writes `results/<id>.json` with id one of `model_a`, `model_b`, `sota_mobilenetv2`, `sota_efficientnetb0`
- [ ] Keys: `model`, `trainable_params`, `total_params`, `macs`, `size_kb`, `size_mb`, `epochs`, `time_per_epoch_s`, `optimizer`, `learning_rate`, `test_accuracy`, `precision_macro`, `recall_macro`, `f1_macro`, `confusion_matrix`, `history` (`loss`, `val_loss`, `accuracy`, `val_accuracy`)
- [ ] Figure names: `figures/<id>_curves.png`, `figures/<id>_confusion.png`
- [ ] Small example JSON in `results/README.md`

### Done when
`results/README.md` is merged."""),
]

ISSUES += custom_model_issues(
    "A", "standard CNN", "ModelA.ipynb",
    "- [ ] Interleave standard `Conv2D` (3×3, ReLU) and `MaxPooling2D` (2×2) layers, e.g. 4 blocks with 32 / 64 / 128 / 256 filters\n"
    "- [ ] Classifier head: GlobalAveragePooling (or Flatten) → Dense → Dropout → Dense(3, softmax)",
    "Model builds for input (64, 64, 3) and outputs 3 class probabilities; parameter count printed.",
    "")

ISSUES += custom_model_issues(
    "B", "lightweight depthwise-separable CNN", "ModelB.ipynb",
    "- [ ] Replace the standard convolutions with **depthwise-separable** convolutions (`SeparableConv2D`, or `DepthwiseConv2D` + 1×1 `Conv2D`)\n"
    "- [ ] Interleave with max-pooling; small classifier head ending in Dense(3, softmax)\n"
    "- [ ] **Total trainable parameters must not exceed 100,000** – add an `assert model.count_params() <= 100_000`",
    "Model builds for input (64, 64, 3), outputs 3 class probabilities and has <= 100,000 trainable parameters.",
    "- [ ] Show why depthwise-separable convs reduce MACs: k·k·C_in + C_in·C_out instead of k·k·C_in·C_out per output pixel\n")

ISSUES += sota_issues("M", "sota-mobilenetv2", "MobileNetV2", "MobileNetV2", "SOTA_MobileNetV2.ipynb",
                      "`tf.keras.applications.mobilenet_v2.preprocess_input` (expects 0–255 pixels, maps to [-1, 1]); "
                      "Keras will warn that 64×64 is not a standard size and load the 224 weights – this is expected")
ISSUES += sota_issues("E", "sota-efficientnet", "EfficientNet-B0", "EfficientNetB0", "SOTA_EfficientNetB0.ipynb",
                      "EfficientNet includes its own rescaling layer – feed raw 0–255 pixels, do **not** divide by 255")

ISSUES += [
    dict(id="C1", labels=["comparison"], title="Comparison: Model A vs Model B table and trade-off discussion",
         body="""Assignment task 4 – comparison part. Built **only from saved results files**, no training and no model code.

**File:** `Comparison.ipynb`

### Tasks
- [ ] Table: total parameters, model size on disk (KB), training time per epoch, test accuracy (also MACs)
- [ ] Bar chart of the four metrics → `figures/compare_AB.png`
- [ ] Discuss trade-offs of moving from standard to depthwise-separable convolutions (parameters / MACs vs accuracy vs training time)

### Done when
Table and discussion are ready for the report.

### Depends on
[A6] [B6]"""),
    dict(id="C2", labels=["comparison"], title="Final comparison: Model B vs MobileNetV2 vs EfficientNet-B0",
         body="""Assignment task 6. Built **only from saved results files**.

**File:** `Comparison.ipynb`

### Tasks
- [ ] Table: parameters, size (MB), MACs, time per epoch, test accuracy, precision, recall
- [ ] Plot test accuracy vs parameters and vs size → `figures/accuracy_vs_cost.png`
- [ ] Discussion: custom sub-100k model from scratch vs pre-trained lightweight model – **accuracy, memory footprint, computational cost**; advantages and limitations of each

### Done when
Table, plot and discussion are ready for the report.

### Depends on
[B6] [M3] [E3]"""),
    dict(id="R1", labels=["report"], title="Report assembly and submission",
         body="""### Tasks
- [ ] Title page with group number, index numbers and names of all members
- [ ] GitHub repository link (assignment section 4)
- [ ] Merge sections: dataset ([D3]), Model A ([A7]), Model B ([B7]), comparison ([C1]), MobileNetV2 ([M4]), EfficientNet-B0 ([E4]), final comparison ([C2])
- [ ] Code: every notebook runs top to bottom and is commented
- [ ] Upload report PDF and code separately to Moodle as `<Groupno>_A03_EN3150`

### Done when
Submitted before the deadline.

### Depends on
[A7] [B7] [M4] [E4] [C1] [C2]"""),
]

OWNER = {"G": "Shared", "D": "Sandali0726", "A": "Model A owner", "B": "Model B owner", "M": "MobileNetV2 owner",
         "E": "EfficientNet-B0 owner", "C": "Comparison (one person)", "R": "Whole group"}

TASK_OF = {"G1": 0, "G2": 0, "D1": 1, "D2": 1, "D3": 1, "C1": 4, "C2": 6, "R1": 7,
           **{f"{p}{n}": t for p in "AB" for n, t in zip(range(1, 8), [2, 2, 3, 4, 4, 4, 4])},
           **{f"{p}{n}": 5 for p in "ME" for n in range(1, 5)}}
WS_OF = {"G": "ws0-shared", "D": "ws0-shared", "R": "ws0-shared", "A": "ws1-model-a", "B": "ws2-model-b",
         "M": "ws3-mobilenetv2", "E": "ws4-efficientnet", "C": "ws5-comparison"}
_STEPS = {1: "build", 2: "params-macs", 3: "optimizers", 4: "train", 5: "evaluate", 6: "results", 7: "report"}
_SOTA_STEPS = {1: "build", 2: "finetune", 3: "evaluate", 4: "report"}
BRANCH_SLUG = {"G1": "setup-requirements-readme", "G2": "results-format",
               "D1": "dataset-generation", "D2": "dataset-sheet", "D3": "dataset-report",
               "C1": "compare-a-vs-b", "C2": "final-comparison", "R1": "report-submission",
               **{f"{p}{n}": f"model-{p.lower()}-{st}" for p in "AB" for n, st in _STEPS.items()},
               **{f"M{n}": f"mobilenetv2-{st}" for n, st in _SOTA_STEPS.items()},
               **{f"E{n}": f"efficientnet-{st}" for n, st in _SOTA_STEPS.items()}}


for _i in ISSUES:   # apply the "[TN] title · task-N · wsN-owner" pattern
    _t = TASK_OF[_i["id"]]
    _i["labels"] = [f"task-{_t}", WS_OF[_i["id"][0]]] + (["report"] if "report" in _i["labels"] else [])
    _i["branch_slug"] = BRANCH_SLUG[_i["id"]]
    _i["title"] = f"[T{_t}] {_i['title']}"
    _i["body"] += ("\n\n---\n**Branch:** `feat/<this issue number>-" + _i["branch_slug"] + "` · "
                   "open a PR into `main` with `Closes #<this issue number>` in the description.")


def to_markdown():
    out = ["# Proposed issues – EN3150 Assignment 03\n",
           "Every model issue touches exactly one model and depends only on shared issues (G*) "
           "or issues of the same model. Comparison issues (C*) read saved `results/*.json` only.\n",
           "Pattern: title `[TN] …` = part N of the brief; labels `task-N` + workstream `wsN-…`; "
           "one branch `feat/<issue>-<slug>` and one PR per issue.\n",
           "| ID | Owner | Labels | Status | Title | Branch |", "|---|---|---|---|---|---|"]
    for i in ISSUES:
        status = "closed (done)" if i.get("closed") else "open"
        out.append(f"| {i['id']} | {OWNER[i['id'][0]]} | {', '.join(i['labels'])} | {status} | {i['title']} | `feat/<#>-{i['branch_slug']}` |")
    for i in ISSUES:
        out += ["\n---\n", f"## {i['id']} – {i['title']}\n", f"**Labels:** {', '.join(i['labels'])}" + (f" · **Assignee:** {i['assignee']}" if i.get("assignee") else "") + (" · **Create as closed**" if i.get("closed") else "") + "\n", i["body"]]
    return "\n".join(out) + "\n"


def gh(*args, data=None):
    cmd = ["gh", "api", *args]
    r = subprocess.run(cmd, input=json.dumps(data) if data else None, capture_output=True, text=True,
                       encoding="utf-8")   # Windows would otherwise use cp1252 and fail on → ≤ etc.
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
    return json.loads(r.stdout) if r.stdout.strip() else None


def create():
    for name, (color, desc) in LABELS.items():
        try:
            gh(f"repos/{REPO}/labels", "--input", "-", data={"name": name, "color": color, "description": desc})
        except RuntimeError as e:
            if "already_exists" not in str(e):
                raise
    numbers, branches = {}, []
    for i in ISSUES:   # dependencies always point to earlier issues, so numbers are known in time
        body = re.sub(r"\[([A-Z]\d)\]", lambda m: f"#{numbers[m.group(1)]}" if m.group(1) in numbers else m.group(0), i["body"])
        data = {"title": i["title"], "body": body, "labels": i["labels"]}
        if i.get("assignee"):
            data["assignees"] = [i["assignee"]]
        res = gh(f"repos/{REPO}/issues", "--input", "-", data=data)
        numbers[i["id"]] = res["number"]
        if i.get("closed"):   # work that was finished before the issues existed
            gh(f"repos/{REPO}/issues/{res['number']}", "-X", "PATCH", "--input", "-",
               data={"state": "closed", "state_reason": "completed"})
        body = body.replace("<this issue number>", str(res["number"]))
        gh(f"repos/{REPO}/issues/{res['number']}", "-X", "PATCH", "--input", "-", data={"body": body})
        branches.append(f"| #{res['number']} | {i['title']} | `feat/{res['number']}-{i['branch_slug']}` |")
        print(f"{i['id']} -> #{res['number']}  {i['title']}")
    Path(__file__).with_name("branches.md").write_text(
        "| Issue | Title | Branch |\n|---|---|---|\n" + "\n".join(branches) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")   # Windows consoles cannot print every character (e.g. ×)
    if sys.argv[1:] == ["create"]:
        create()
    else:
        path = Path(__file__).with_name("issues_plan.md")
        path.write_text(to_markdown(), encoding="utf-8")
        print("written", path, len(ISSUES), "issues")
