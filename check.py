# import torch
# print(torch.cuda.is_available())
# print(torch.version.cuda)

import fiftyone as fo
import fiftyone.zoo as foz

# # Load the COCO-2017 dataset with specific classes and splits
# dataset = foz.load_zoo_dataset(
#     "coco-2017",
#     splits=("train", "validation", "test"),
#     classes=["person"],  # Specify that you want to load only the 'person' class
#     max_samples=10  # Load a small subset for quick inspection
# )

# # Launch the FiftyOne app to inspect the loaded data
# session = fo.launch_app(dataset)
# session.wait()

# Load the dataset without filtering for 'person' to check all annotations
# full_dataset = foz.load_zoo_dataset(
#     "coco-2017",
#     splits=("train", "validation"),
#     max_samples=1000  # Load a small sample to inspect
# )

# # Launch the FiftyOne app to inspect all annotations
# session = fo.launch_app(full_dataset)
# session.wait()
import fiftyone as fo

# Delete the existing dataset
fo.delete_zoo_dataset("coco-2017")