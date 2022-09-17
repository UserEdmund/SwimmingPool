#Introduction

According to the idea of “target detection → target tracking → state modeling → behavior warning”, this project first uses swimming pool data set (including homemade live video), and label the data to train the target detection network model based on deep learning, and the fast target detection model based on optimized YOLO. This dataset is not included in this repository (If required, please contact us). And we optimized for lightweight scenes (EIOU loss function, ACON-C activation function, Ghostnet, BiFPN feature fusion, coordinate attention mechanism CA), and evaluated the optimization results through comparative analysis of three network models (Baseline, Ghostnet+, BiFPN+CA). 



# This project is based on Yolov5 + StrongSORT 

The baseline repo is forked from  https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet

For Yolov5 DeepSort OSNet bugs and feature requests please visit [GitHub Issues](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/issues). For business inquiries or professional support requests please send an email to: yolov5.deepsort.pytorch@gmail.com
