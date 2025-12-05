# Task 1: Edge AI Prototype Report

## 1. Model Overview
We trained a lightweight Convolutional Neural Network (CNN) using TensorFlow.
- **Dataset:** Fashion MNIST (used as a proxy for recyclable item classification).
- **Architecture:** 2 Convolutional layers, 2 Max Pooling layers, and 1 Dense hidden layer.
- **Input Shape:** 28x28 grayscale images.

## 2. Accuracy Metrics
After training for 5 epochs, the model typically achieves:
- **Training Accuracy:** ~90%
- **Validation Accuracy:** ~88%
*(Note: These are estimated values based on standard performance on this dataset. Actual results may vary slightly upon execution.)*

## 3. Deployment Steps (TensorFlow Lite)
To deploy this model to an edge device (e.g., Raspberry Pi or Android):

1.  **Train & Save:** Train the model in Python and save it.
2.  **Convert:** Use `tf.lite.TFLiteConverter` to convert the SavedModel to a `.tflite` file.
    - *Optimization:* Applied default optimizations (quantization) to reduce file size.
3.  **Transfer:** Copy the `model.tflite` file to the edge device.
4.  **Inference:**
    - Install the TFLite runtime on the device (`pip install tflite-runtime`).
    - Load the model using `Interpreter`.
    - Resize and preprocess input images from the camera.
    - Run inference and interpret the output logits.

## 4. Benefits of Edge AI for Real-Time Applications
- **Low Latency:** Processing happens locally, eliminating the round-trip time to a server. This is critical for applications like autonomous driving or industrial robotics where milliseconds count.
- **Bandwidth Efficiency:** Sending high-definition video streams to the cloud consumes massive bandwidth. Edge AI processes raw data locally and only sends small metadata (e.g., "Plastic Bottle Detected").
- **Reliability:** The system works even without an internet connection.
- **Privacy:** Images/audio are processed on-device and don't need to be stored or transmitted, protecting user privacy.
