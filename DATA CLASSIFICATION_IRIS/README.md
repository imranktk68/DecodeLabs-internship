# Iris KNN Classifier

Small project demonstrating a K-Nearest Neighbors classifier on the Iris dataset.

## Files

- `KNN-classifier_Iris.py`: main script to train/evaluate a KNN model.
- `requirements.txt`: Python dependencies.

## Setup

Create a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

Train and evaluate with default settings:

```bash
python KNN-classifier_Iris.py
```

Specify neighbors, test size, save model, and produce a confusion matrix plot:

```bash
python KNN-classifier_Iris.py --k 5 --test-size 0.2 --plot --save-model knn_iris.joblib
```

## Notes

- The script uses scikit-learn's built-in Iris dataset.
- Model is saved with `joblib` when `--save-model` is provided.
- The confusion matrix image is written to `knn_iris_confusion_k{k}.png` when `--plot` is used.

## Next steps

- Add unit tests or a small example notebook if desired.
