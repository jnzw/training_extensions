"""
 Copyright (c) 2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from .mmdetection import MMDetectionArgConverterMap
from ..registry import ARG_CONVERTER_MAPS

@ARG_CONVERTER_MAPS.register_module()
class MMPoseArgConverterMap(MMDetectionArgConverterMap):

    @staticmethod
    def _train_compression_base_args_map():
        return {
            'train_ann_files': 'data.train.ann_file',
            'train_data_roots': 'data.train.img_prefix',
            'val_ann_files': 'data.val.ann_file',
            'val_data_roots': 'data.val.img_prefix',
            'save_checkpoints_to': 'work_dir',
            'batch_size': 'data.samples_per_gpu',
        }