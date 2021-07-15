from .darknet import Darknet
from .detectors_resnet import DetectoRS_ResNet, DetectoRS_ResNetV1d
from .detectors_resnext import DetectoRS_ResNeXt
from .hourglass import HourglassNet
from .hrnet import HRNet
from .regnet import RegNet
from .res2net import Res2Net
from .resnest import ResNeSt
from .resnet import ResNet, ResNetV1d
from .resnext import ResNeXt
from .ssd_vgg import SSDVGG
from .trident_resnet import TridentResNet
from .ssd_res50 import SSDRES
from .vgg import VGG
from .detectors_resnest import DetectoRS_ResNeSt
from .swin_transformer import SwinTransformer

__all__ = [
    'RegNet', 'ResNet', 'ResNetV1d', 'ResNeXt', 'SSDVGG', 'HRNet', 'Res2Net',
    'HourglassNet', 'DetectoRS_ResNet', 'DetectoRS_ResNeXt', 'Darknet',
    'ResNeSt', 'TridentResNet', 'SSDRES', 'VGG', 'DetectoRS_ResNeSt', 'DetectoRS_ResNetV1d',
    'SwinTransformer'
]