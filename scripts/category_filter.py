import os
import pandas as pd


class CategoryFilter:
    """
    Filters annotation metadata based on object category.
    """

    def __init__(self, input_dir="../outputs", output_dir="../outputs"):
        """
        Initialize input and output directories.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def filter_by_category(
        self,
        input_filename="annotation_metadata.csv",
        category="vehicle.car",
        output_filename="filtered_vehicle_annotations.csv"
    ):
        """
        Filter annotations by category and save the result.
        """

        input_path = os.path.join(self.input_dir, input_filename)

        df = pd.read_csv(input_path)

        filtered_df = df[df["category"] == category]

        output_path = os.path.join(self.output_dir, output_filename)

        filtered_df.to_csv(output_path, index=False)

        print("=" * 60)
        print("Category Filtering Summary")
        print("=" * 60)
        print(f"Target Category : {category}")
        print(f"Total Annotations : {len(df)}")
        print(f"Filtered Objects : {len(filtered_df)}")
        print(f"Output File : {output_path}")
        print("=" * 60)

        return filtered_df
    