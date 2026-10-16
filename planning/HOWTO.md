# How to create the issues, branches and PRs

Pattern (same as the example board):

- **Issue title** `[TN] …` – N = part of the assignment brief (T0 setup, T1 data, T2 architecture,
  T3 optimizers, T4 training & evaluation, T5 SOTA, T6 final comparison, T7 submission)
- **Labels** `task-N` + one workstream label: `ws0-shared`, `ws1-model-a`, `ws2-model-b`,
  `ws3-mobilenetv2`, `ws4-efficientnet`, `ws5-comparison` (+ `report` for writing tasks)
- **One branch per issue** `feat/<issue number>-<slug>`, e.g. `feat/53-model-a-build`
- **One PR per issue** into `main`, description contains `Closes #<issue number>`

Run everything on your own computer (needs [GitHub CLI](https://cli.github.com/), logged in as a repo admin).

## 1. Create the 30 issues and 15 labels

```bash
git clone https://github.com/VisionForgeCSE/cnn-for-image-classification
cd cnn-for-image-classification
git checkout setup                 # planning/ lives on the setup branch
gh auth login
python planning/issues.py create
```

This creates every issue with its labels, links dependencies as real `#numbers`, assigns the dataset
issues to Sandali0726, closes the finished dataset-generation issue, and writes
`planning/branches.md` (issue number → branch name).

Then on GitHub assign the other issues by workstream label (filter `label:ws1-model-a` etc.).

## 2. Work on one issue = one branch = one PR

```bash
git checkout main && git pull
git checkout -b feat/<number>-<slug>          # name from planning/branches.md
# ... do the work, commit often ...
git push -u origin feat/<number>-<slug>
gh pr create --base main --title "<issue title>" --body "Closes #<number>"
```

Merge the PR on GitHub → the issue closes automatically.

## 3. The `setup` branch

The `setup` branch already contains the work for both setup issues and this issue tooling:

- `requirements.txt` (TensorFlow), `.gitignore`, `README.md`, `figures/` → **[T0] Setup: requirements.txt (TensorFlow) and README**
- `results/README.md` (shared results format) → **[T0] Results format convention for all models**
- `planning/` – issue script, full issue text, this how-to

After step 1, push it and open one PR that closes both setup issues (numbers from `planning/branches.md`):

```bash
git push -u origin setup
gh pr create --base main --head setup --title "[T0] Project setup, results format and issue plan" \
  --body "Closes #<setup issue>
Closes #<results-format issue>"
```

Before merging, fill in the group number, names and index numbers in `README.md`.
