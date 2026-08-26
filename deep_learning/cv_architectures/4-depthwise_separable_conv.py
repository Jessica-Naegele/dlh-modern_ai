#!/usr/bin/env python3
"""
Module containing depthwise_separable_conv function
"""
from tensorflow import keras as K


def depthwise_separable_conv(X, filters, stride=1):
    """
    Builds a depthwise separable convolution block for MobileNetV1.

    Args:
        X: input tensor
        filters: number of output channels for pointwise convolution
        stride: stride applied to depthwise convolution

    Returns:
        Output tensor of the depthwise separable convolution block
    """
    # 1. Depthwise Convolution (3x3 spatial filtering per channel)
    x = K.layers.DepthwiseConv2D(
        kernel_size=(3, 3),
        strides=stride,
        padding='same'
    )(X)
    x = K.layers.BatchNormalization()(x)
    x = K.layers.ReLU()(x)

    # 2. Pointwise Convolution (1x1 channel mixing & expansion)
    x = K.layers.Conv2D(
        filters=filters,
        kernel_size=(1, 1),
        strides=1,
        padding='same'
    )(x)
    x = K.layers.BatchNormalization()(x)
    x = K.layers.ReLU()(x)

    return x
