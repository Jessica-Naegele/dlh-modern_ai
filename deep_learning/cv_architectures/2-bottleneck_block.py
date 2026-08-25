#!/usr/bin/env python3
"""
--- TASK 2 ---
A function which implements a ResNet bottleneck residual block
with the following arguments: x, filters, stride, downsample,
name
"""

from tensorflow import keras


def bottleneck_block(
        x,
        filters,
        stride=1,
        downsample=False,
        name=None
):
    """
    implement ResNet bottleneck residual block

    args:
    - x: input tensor
    - filters: # number of filters for 3x3 convolution
    - stride: used for spaital downsampling - stride for first convolution
    - downsample: boolean
    - name: optional string to name the block layers

    returns:
    bottleneck residual block

    The block should consist of
    - A 1×1 convolution that reduces the number of channels.
    - A 3×3 convolution applied to the reduced representation.
    - A 1×1 convolution that expands the channels by a factor of 4.
    - Batch Normalization after each convolution.
    - ReLU activation after the first and second convolutions.
    - A residual (skip) connection:
    - Identity shortcut if downsample=False.
    - Projection shortcut (1×1 convolution + BatchNorm) if downsample=True.
    - A final ReLU activation after adding the shortcut.
    """
    bn = x

    # 1x1 convolution --> reduces number of channels followed
    # by batchnorm
    bn = keras.layers.Conv2D(
        filters=filters,
        kernel_size=(1, 1),
        strides=stride,
        use_bias=False,
        name=f"{name}_conv1" if name else None
        )(bn)
    bn = keras.layers.BatchNormalization(
        name=f"{name}_bn1" if name else None
        )(bn)
    bn = keras.layers.Activation(
        'relu',
        name=f"{name}_relu1" if name else None
        )(bn)

    # 3x3 convolution
    bn = keras.layers.Conv2D(
        filters=filters,
        kernel_size=(3, 3),
        padding='same',
        use_bias=False,
        name=f"{name}_conv2" if name else None
        )(bn)
    bn = keras.layers.BatchNormalization(
        name=f"{name}_bn2" if name else None
        )(bn)
    bn = keras.layers.Activation(
        'relu',
        name=f"{name}_relu2" if name else None
        )(bn)

    # 1x1 convolution
    bn = keras.layers.Conv2D(
        filters=filters * 4,
        kernel_size=(1, 1),
        use_bias=False,
        name=f"{name}_conv3" if name else None
        )(bn)
    bn = keras.layers.BatchNormalization(
        name=f"{name}_bn3" if name else None
        )(bn)

    # introducing the shortcut
    if downsample:
        sc = keras.layers.Conv2D(
            filters=filters * 4,
            kernel_size=(1, 1),
            strides=stride,
            use_bias=False,
            name=f"{name}_shortcut_conv" if name else None
            )(x)
        sc = keras.layers.BatchNormalization(
            name=f"{name}_shortcut_bn" if name else None
            )(sc)

    else:
        sc = x

    out = keras.layers.add(
        [bn, sc],
        name=f"{name}_add" if name else None
        )
    out = keras.layers.Activation(
        'relu',
        name=f"{name}_out" if name else None
        )(out)

    return out
