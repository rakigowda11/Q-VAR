import os


class ImageExtractor:

    CAMERA_CHANNELS = [
        "CAM_FRONT",
        "CAM_FRONT_LEFT",
        "CAM_FRONT_RIGHT",
        "CAM_BACK",
        "CAM_BACK_LEFT",
        "CAM_BACK_RIGHT"
    ]

    def __init__(self, nusc):
        """
        Initialize with an existing NuScenes object.
        """
        self.nusc = nusc

    def get_image_paths(self, sample):
        """
        Returns image paths for all camera channels in a sample.
        """

        image_paths = {}

        for channel in self.CAMERA_CHANNELS:

            if channel in sample["data"]:

                sample_data_token = sample["data"][channel]

                sample_data = self.nusc.get(
                    "sample_data",
                    sample_data_token
                )

                image_path = os.path.join(
                    self.nusc.dataroot,
                    sample_data["filename"]
                )

                image_paths[channel] = image_path

        return image_paths

    def print_image_summary(self, sample):
        """
        Prints image path summary for a sample.
        """

        image_paths = self.get_image_paths(sample)

        print("=" * 80)
        print("Image Summary")
        print("=" * 80)

        for channel, path in image_paths.items():
            print(f"{channel}:")
            print(f"  {path}")