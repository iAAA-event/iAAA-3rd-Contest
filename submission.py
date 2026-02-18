import os
import click
import pandas as pd
import numpy as np


def load_data(data_dir: str) -> pd.DataFrame:
    """
    data_dira
        |_ file1
        |_ file2
        |_ file3
        ...
    """
    pass


def predict() -> np.ndarray:
    """Replace this with your actual model logic."""
    rng = np.random.default_rng()
    return rng.integers(0, 2, size=10)


def save_predictions(predictions: np.ndarray, output_path: str) -> None:
    result = pd.DataFrame({
        "id": range(10),
        "prediction": predictions,
    })
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    result.to_csv(output_path, index=False)
    click.echo(f"Saved {len(result)} predictions to {output_path}")


@click.command()
@click.option("--data-dir", required=True, help="Directory containing input data files.")
@click.option("--predictions-file-path", required=True, help="Path to write the output predictions CSV.")
def main(data_dir: str, predictions_file_path: str):
    load_data(data_dir)
    predictions = predict()
    save_predictions(predictions, predictions_file_path)


if __name__ == "__main__":
    main()
