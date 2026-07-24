import os


class LiDARExtractor:

    def __init__(self, nusc):
        """
        Initialize with an existing NuScenes object.
        """
        self.nusc = nusc

    def get_lidar_path(self, sample):
        """
        Returns the LiDAR file path for a sample.
        """

        lidar_token = sample["data"]["LIDAR_TOP"]

        sample_data = self.nusc.get(
            "sample_data",
            lidar_token
        )

        lidar_path = os.path.join(
            self.nusc.dataroot,
            sample_data["filename"]
        )

        return lidar_path

    def print_lidar_summary(self, sample):
        """
        Prints LiDAR file path summary.
        """

        lidar_path = self.get_lidar_path(sample)

        print("=" * 80)
        print("LiDAR Summary")
        print("=" * 80)
        print("LiDAR Path:")
        print(lidar_path)