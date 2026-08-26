#!/usr/bin/env python3
"""
--- TASK 3 ---
A function building ResNet-101 architecture with arguments of
input_shape, num_classes. Having several blocks
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
    """
    bn = x
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


def make_layer(x, blocks, filters, stride=1, name=None):
    """ function helping to create layers """
    x = bottleneck_block(
        x,
        filters,
        stride=stride,
        downsample=True,
        name=f'{name}_block1'
    )
    for i in range(1, blocks):
        x = bottleneck_block(
            x,
            filters,
            stride=1,
            downsample=False,
            name=f'{name}_block{i+1}'
        )
    return x


def build_resnet101(input_shape=(224, 224, 3), num_classes=1000):
    """ function to create a resnet architecure

    - args:
    - input_shape: tuple
    - num_classes: # output classes

    returns:
    - architecture
    """

    # initial layer
    input = keras.layers.Input(shape=input_shape)

    # Initial Stage
    """
    1) 7x7 Conv layer with 64 filters and stride 2
    2) batch normalization + ReLu
    3) 3x3 Max Pooling layer with stride 2
    """
    resnet = keras.layers.Conv2D(
        filters=64,
        kernel_size=(7, 7),
        strides=2,
        padding='same',
        use_bias=False,
        name="conv1"
    )(input)
    resnet = keras.layers.BatchNormalization(name="bn1")(resnet)
    resnet = keras.layers.Activation(
        'relu',
        name="relu1"
    )(resnet)
    resnet = keras.layers.MaxPool2D(
        pool_size=(3, 3),
        strides=2,
        padding='same',
        name='maxpool'
    )(resnet)

    # Stack Bottleneck resdiual Blocks

    # 1. Residual Block - 3 blocks in conv2_x
    resnet = make_layer(resnet, 3, 64, 1, name="layer1")
    # 2. Residual Block - 4 Bocks in conv3_x
    resnet = make_layer(resnet, 4, 128, 2, name="layer2")
    # 3. Residual Block - 23 Bocks in conv4_x
    resnet = make_layer(resnet, 23, 256, 2, name="layer3")
    # 4. Residual Block - 3 Bocks in conv5_x
    resnet = make_layer(resnet, 3, 512, 2, name="layer4")

    # End with global average pooling and fully connected classification layer

    resnet = keras.layers.GlobalAveragePooling2D(
        name="GlobalAveragePooling"
    )(resnet)
    outputs = keras.layers.Dense(
        units=num_classes,
        activation='softmax',
        name="Dense"
    )(resnet)

    # instantiate keras model
    model = keras.Model(inputs=input, outputs=outputs)

    return model
