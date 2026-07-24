# Q-VAR

## Quantum View-dependent Appearance Rendering

Q-VAR is a benchmark and data preparation pipeline focused on studying the view-dependent appearance of physical objects from multi-view camera observations.

The current implementation uses the NuScenes dataset as the initial data source and prepares physically consistent object tracks for further view-dependent appearance analysis and rendering.

---

## Project Objective

The primary objective of Q-VAR is to organize and prepare multi-view observations of the same physical object across different viewpoints.

The pipeline focuses on:

- Identifying the same physical object across multiple frames.
- Collecting its observations from different camera viewpoints.
- Understanding the object's viewing-angle variation.
- Linking object annotations with camera images.
- Preparing the data for future view-dependent appearance rendering and evaluation.

---

## Dataset

The current prototype uses the **NuScenes Mini dataset**.

The dataset provides:

- Multiple camera views.
- LiDAR data.
- Ego-vehicle pose information.
- Camera calibration information.
- Object annotations.
- Physical object tracking across multiple frames.

The complete dataset is not included in this repository. It must be downloaded separately and placed inside the expected dataset directory.

---

## Current Pipeline

```text
NuScenes Dataset
        │
        ▼
Scene Extraction
        │
        ▼
Sample and Annotation Extraction
        │
        ▼
Physical Instance Identification
        │
        ▼
Category Filtering
        │
        ▼
Track-Length Filtering
        │
        ▼
Camera-Image Association
        │
        ▼
3D Object Representation
        │
        ▼
3D → Camera Coordinate Transformation
        │
        ▼
Camera → Image Coordinate Projection
        │
        ▼
2D Bounding Box Generation
        │
        ▼
Viewing-Angle Analysis
        │
        ▼
Q-VAR Dataset Preparation
