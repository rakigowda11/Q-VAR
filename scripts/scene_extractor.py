from nuscenes.nuscenes import NuScenes
import pandas as pd


class SceneExtractor:

    def __init__(self, dataroot, version='v1.0-mini'):
        self.nusc = NuScenes(
            version=version,
            dataroot=dataroot,
            verbose=True
        )

    def get_total_scenes(self):
        return len(self.nusc.scene)

    def get_scene(self, index):
        return self.nusc.scene[index]

    def print_scene_summary(self):
        print("=" * 80)
        print("NuScenes Scene Summary")
        print("=" * 80)

        for i, scene in enumerate(self.nusc.scene):
            print(f"\nScene {i+1}")
            print("-" * 40)
            print("Name :", scene["name"])
            print("Description :", scene["description"])
            print("First Sample :", scene["first_sample_token"])
            print("Last Sample :", scene["last_sample_token"])

    def save_scenes_to_csv(self, output_path):
        """
        Save scene information to a CSV file.
        """

        scene_data = []

        for scene in self.nusc.scene:
            scene_data.append({
                "scene_name": scene["name"],
                "description": scene["description"],
                "first_sample_token": scene["first_sample_token"],
                "last_sample_token": scene["last_sample_token"]
            })

        df = pd.DataFrame(scene_data)
        df.to_csv(output_path, index=False)

        print(f"Scene data saved to: {output_path}")