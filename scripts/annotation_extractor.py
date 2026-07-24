class AnnotationExtractor:

    def __init__(self, nusc):
        """
        Initialize with an existing NuScenes object.
        """
        self.nusc = nusc

    def get_annotations(self, sample):
        """
        Returns all annotations for a sample.
        """

        annotations = []

        for ann_token in sample["anns"]:

            annotation = self.nusc.get(
                "sample_annotation",
                ann_token
            )

            annotations.append({
                # Unique ID for this annotation at this sample
                "annotation_token": annotation["token"],

                # Unique ID for the same physical object across samples
                "instance_token": annotation["instance_token"],

                # Sample in which this annotation exists
                "sample_token": annotation["sample_token"],

                # Object information
                "category": annotation["category_name"],
                "translation": annotation["translation"],
                "size": annotation["size"],
                "rotation": annotation["rotation"],

                # Visibility and temporal information
                "visibility_token": annotation["visibility_token"],
                "attribute_tokens": annotation["attribute_tokens"],
                "prev": annotation["prev"],
                "next": annotation["next"],

                # Sensor information
                "num_lidar_pts": annotation["num_lidar_pts"],
                "num_radar_pts": annotation["num_radar_pts"]
            })

        return annotations

    def print_annotation_summary(self, sample):
        """
        Prints summary of annotations in a sample.
        """

        annotations = self.get_annotations(sample)

        print("=" * 80)
        print("Annotation Summary")
        print("=" * 80)

        print(f"Total Objects: {len(annotations)}")

        for i, ann in enumerate(annotations[:5]):

            print(f"\nObject {i+1}")
            print("-" * 40)

            print("Annotation Token:", ann["annotation_token"])
            print("Instance Token:", ann["instance_token"])
            print("Sample Token:", ann["sample_token"])
            print("Category:", ann["category"])
            print("Position:", ann["translation"])
            print("Size:", ann["size"])
            print("LiDAR Points:", ann["num_lidar_pts"])