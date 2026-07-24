from nuscenes.nuscenes import NuScenes


class SampleExtractor:

    def __init__(self, nusc):
        """
        Initialize with an existing NuScenes object.
        """
        self.nusc = nusc

    def get_samples_in_scene(self, scene_token):
        """
        Traverse all samples in a scene.
        Returns a list of sample dictionaries.
        """

        scene = self.nusc.get("scene", scene_token)

        sample_token = scene["first_sample_token"]

        samples = []

        while sample_token != "":
            sample = self.nusc.get("sample", sample_token)

            samples.append(sample)

            sample_token = sample["next"]

        return samples

    def get_sample_count(self, scene_token):
        """
        Returns the number of samples in a scene.
        """

        samples = self.get_samples_in_scene(scene_token)

        return len(samples)

    def print_sample_summary(self, scene_token):
        """
        Prints summary of samples in a scene.
        """

        samples = self.get_samples_in_scene(scene_token)

        print("=" * 80)
        print(f"Sample Summary for Scene: {scene_token}")
        print("=" * 80)

        print(f"Total Samples: {len(samples)}")

        for i, sample in enumerate(samples[:5]):
            print(f"\nSample {i+1}")
            print("-" * 40)
            print("Token:", sample["token"])
            print("Timestamp:", sample["timestamp"])
            print("Next:", sample["next"])
            print("Previous:", sample["prev"])