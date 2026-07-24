import os
import pandas as pd


class DatasetStatistics:
    """
    Generate statistics from annotation metadata.
    """

    def __init__(self, input_dir="../outputs", output_dir="../outputs"):
        self.input_dir = input_dir
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def generate_statistics(
        self,
        input_filename="annotation_metadata.csv",
        output_filename="dataset_statistics.csv"
    ):

        input_path = os.path.join(self.input_dir, input_filename)

        df = pd.read_csv(input_path)

        total_annotations = len(df)

        category_counts = df["category"].value_counts()

        statistics = pd.DataFrame({
            "Category": category_counts.index,
            "Count": category_counts.values
        })

        statistics["Percentage"] = (
            statistics["Count"] / total_annotations * 100
        ).round(2)

        output_path = os.path.join(self.output_dir, output_filename)

        statistics.to_csv(output_path, index=False)

        print("=" * 60)
        print("Dataset Statistics")
        print("=" * 60)
        print(f"Total Objects : {total_annotations}")
        print()

        print(statistics)

        print("=" * 60)
        print(f"Statistics saved to : {output_path}")
        print("=" * 60)

        return statistics