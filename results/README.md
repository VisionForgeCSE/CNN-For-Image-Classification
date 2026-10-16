# Results format

Every model notebook saves its numbers here in the **same format**, so the comparison
notebook can build its tables from these files alone – nobody needs another member's code.

| Model | `id` | Notebook |
|---|---|---|
| Model A – standard CNN | `model_a` | `ModelA.ipynb` |
| Model B – depthwise-separable CNN | `model_b` | `ModelB.ipynb` |
| MobileNetV2 (pre-trained) | `sota_mobilenetv2` | `SOTA_MobileNetV2.ipynb` |
| EfficientNet-B0 (pre-trained) | `sota_efficientnetb0` | `SOTA_EfficientNetB0.ipynb` |

## Files per model

| File | Content |
|---|---|
| `results/<id>.json` | numbers below |
| `results/<id>.keras` | trained model without optimizer state |
| `figures/<id>_curves.png` | training / validation loss (and accuracy) per epoch |
| `figures/<id>_confusion.png` | test-set confusion matrix |

## Keys in `results/<id>.json`

| Key | Type | Meaning |
|---|---|---|
| `model` | str | display name, e.g. `"Model A"` |
| `trainable_params` | int | `sum(w.numpy().size for w in model.trainable_weights)` |
| `total_params` | int | `model.count_params()` |
| `macs` | int | multiply-accumulate operations for one 64×64 image |
| `size_kb` | float | size on disk of `results/<id>.keras` in KB |
| `size_mb` | float | same in MB (`size_kb / 1024`) |
| `epochs` | int | epochs actually trained |
| `time_per_epoch_s` | float | mean seconds per epoch, epoch 1 excluded |
| `optimizer` | str | e.g. `"Adam"` |
| `learning_rate` | float | e.g. `0.001` |
| `test_accuracy` | float | 0–1 |
| `precision_macro` | float | 0–1 |
| `recall_macro` | float | 0–1 |
| `f1_macro` | float | 0–1 |
| `per_class` | dict | `{"cats": {"precision": …, "recall": …, "f1": …}, …}` |
| `confusion_matrix` | list[list[int]] | rows = true class, columns = predicted, order `["cats", "dogs", "snakes"]` |
| `history` | dict | `loss`, `val_loss`, `accuracy`, `val_accuracy` lists from `model.fit` |

All values must be plain Python types (use `float(...)`, `int(...)`, `.tolist()`), otherwise `json.dump` fails.

## Example

```json
{
  "model": "Model A",
  "trainable_params": 421699,
  "total_params": 421699,
  "macs": 60195200,
  "size_kb": 1680.2,
  "size_mb": 1.64,
  "epochs": 20,
  "time_per_epoch_s": 3.73,
  "optimizer": "Adam",
  "learning_rate": 0.001,
  "test_accuracy": 0.7111,
  "precision_macro": 0.7087,
  "recall_macro": 0.7111,
  "f1_macro": 0.7037,
  "per_class": {"cats": {"precision": 0.6667, "recall": 0.7333, "f1": 0.6984}},
  "confusion_matrix": [[110, 30, 10], [45, 78, 27], [10, 8, 132]],
  "history": {"loss": [1.05, 0.94], "val_loss": [0.90, 0.89], "accuracy": [0.40, 0.52], "val_accuracy": [0.54, 0.57]}
}
```

## Saving it (copy into your notebook)

```python
import json, os
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

def save_results(model_id, name, model, history, epoch_times, optimizer, lr, macs, y_true, y_pred, class_names):
    path = f"results/{model_id}.keras"
    model.save(path)
    p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average=None, zero_division=0)
    pm, rm, fm, _ = precision_recall_fscore_support(y_true, y_pred, average="macro", zero_division=0)
    out = {
        "model": name,
        "trainable_params": int(sum(w.numpy().size for w in model.trainable_weights)),
        "total_params": int(model.count_params()),
        "macs": int(macs),
        "size_kb": os.path.getsize(path) / 1024,
        "size_mb": os.path.getsize(path) / 1024 ** 2,
        "epochs": len(history.history["loss"]),
        "time_per_epoch_s": float(sum(epoch_times[1:]) / max(len(epoch_times) - 1, 1)),
        "optimizer": optimizer,
        "learning_rate": float(lr),
        "test_accuracy": float(accuracy_score(y_true, y_pred)),
        "precision_macro": float(pm), "recall_macro": float(rm), "f1_macro": float(fm),
        "per_class": {c: {"precision": float(p[i]), "recall": float(r[i]), "f1": float(f1[i])}
                      for i, c in enumerate(class_names)},
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "history": {k: [float(v) for v in vals] for k, vals in history.history.items()
                    if k in ("loss", "val_loss", "accuracy", "val_accuracy")},
    }
    with open(f"results/{model_id}.json", "w") as f:
        json.dump(out, f, indent=2)
```

`model.save` stores the optimizer state too; if you want the pure deployable size, save an
uncompiled copy (`clean = build_fn(); clean.set_weights(model.get_weights()); clean.save(path)`).
