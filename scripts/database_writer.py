import os
import pandas as pd


class DatabaseWriter:

    def __init__(self, output_dir="../outputs"):
        """
        Initialize output directory.
        """
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def save_sample_metadata(self, samples, output_filename="sample_metadata.csv"):
        """
        Save sample metadata to CSV.
        """

        sample_data = []

        for sample in samples:
            sample_data.append({
                "sample_token": sample["token"],
                "timestamp": sample["timestamp"],
                "prev": sample["prev"],
                "next": sample["next"]
            })

        df = pd.DataFrame(sample_data)

        output_path = os.path.join(self.output_dir, output_filename)

        df.to_csv(output_path, index=False)

        print(f"Sample metadata saved to: {output_path}")

    def save_image_metadata(self, samples, image_extractor,
                            output_filename="image_metadata.csv"):
        """
        Save image metadata to CSV.
        """

        image_data = []

        for sample in samples:
            image_paths = image_extractor.get_image_paths(sample)

            for channel, path in image_paths.items():
                image_data.append({
                    "sample_token": sample["token"],
                    "camera_channel": channel,
                    "image_path": path
                })

        df = pd.DataFrame(image_data)

        output_path = os.path.join(self.output_dir, output_filename)

        df.to_csv(output_path, index=False)

        print(f"Image metadata saved to: {output_path}")

    def save_lidar_metadata(self, samples, lidar_extractor,
                            output_filename="lidar_metadata.csv"):
        """
        Save LiDAR metadata to CSV.
        """

        lidar_data = []

        for sample in samples:
            lidar_path = lidar_extractor.get_lidar_path(sample)

            lidar_data.append({
                "sample_token": sample["token"],
                "lidar_path": lidar_path
            })

        df = pd.DataFrame(lidar_data)

        output_path = os.path.join(self.output_dir, output_filename)

        df.to_csv(output_path, index=False)

        print(f"LiDAR metadata saved to: {output_path}")

    def save_annotation_metadata(self, samples, annotation_extractor,
                                 output_filename="annotation_metadata.csv"):
        """
        Save annotation metadata to CSV.
        """

        annotation_data = []

        for sample in samples:
            annotations = annotation_extractor.get_annotations(sample)

            for ann in annotations:
                annotation_data.append({
                    "sample_token": sample["token"],
                    "annotation_token": ann["token"],
                    "category": ann["category"],
                    "translation": ann["translation"],
                    "size": ann["size"],
                    "num_lidar_pts": ann["num_lidar_pts"],
                    "num_radar_pts": ann["num_radar_pts"]
                })

        df = pd.DataFrame(annotation_data)

        output_path = os.path.join(self.output_dir, output_filename)

        df.to_csv(output_path, index=False)

        print(f"Annotation metadata saved to: {output_path}")