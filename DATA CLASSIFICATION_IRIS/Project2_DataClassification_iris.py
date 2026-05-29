from pathlib import Path
import argparse
import joblib
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay


def run(k: int = 3, test_size: float = 0.2, random_state: int | None = 42, save_model: str | None = None, plot: bool = False):
    data = load_iris()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"KNN (k={k}) accuracy: {acc:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

    if plot:
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
        fig, ax = plt.subplots(figsize=(6, 4))
        disp.plot(ax=ax)
        plt.title(f"KNN (k={k}) Confusion Matrix")
        out_path = Path(f"knn_iris_confusion_k{k}.png")
        fig.savefig(out_path, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved confusion matrix plot to {out_path}")

    if save_model:
        out = Path(save_model)
        joblib.dump(clf, out)
        print(f"Saved trained model to {out}")

    return clf


def parse_args():
    p = argparse.ArgumentParser(description="Train and evaluate a KNN classifier on the Iris dataset")
    p.add_argument("--k", type=int, default=3, help="number of neighbors (default: 3)")
    p.add_argument("--test-size", type=float, default=0.2, help="test set fraction (default: 0.2)")
    p.add_argument("--random-state", type=int, default=42, help="random state for train/test split")
    p.add_argument("--save-model", type=str, default=None, help="path to save trained model (joblib)")
    p.add_argument("--plot", action="store_true", help="save confusion matrix plot")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(k=args.k, test_size=args.test_size, random_state=args.random_state, save_model=args.save_model, plot=args.plot)
