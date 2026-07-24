import os
import pandas as pd


class ImageAnnotationLinker:
    """
    Links annotation metadata with image metadata
    using sample_token.
    """

    def __init__(self,
                 input_dir="../outputs",
                 output_dir="../outputs"):

        self.input_dir = input_dir
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def link_annotations_to_images(
        self,
        annotation_file="annotation_metadata.csv",
        image_file="image_metadata.csv",
        output_file="linked_image_annotations.csv"
    ):

        annotation_path = os.path.join(
            self.input_dir,
            annotation_file
        )

        image_path = os.path.join(
            self.input_dir,
            image_file
        )

        annotation_df = pd.read_csv(annotation_path)

        image_df = pd.read_csv(image_path)

        linked_df = pd.merge(
            annotation_df,
            image_df,
            on="sample_token",
            how="inner"
        )

        output_path = os.path.join(
            self.output_dir,
            output_file
        )

        linked_df.to_csv(
            output_path,
            index=False
        )

        print("=" * 60)
        print("Image Annotation Linking Summary")
        print("=" * 60)
        print(f"Annotations : {len(annotation_df)}")
        print(f"Images      : {len(image_df)}")
        print(f"Linked Rows : {len(linked_df)}")
        print("=" * 60)
        print(f"Saved to : {output_path}")
        print("=" * 60)

        return linked_df