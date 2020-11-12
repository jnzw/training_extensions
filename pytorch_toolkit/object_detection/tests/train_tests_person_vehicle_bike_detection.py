# Copyright (C) 2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.

import os

from common.test_case import create_test_case


class PersonVehicleBikeDetection2000TestCase(
        create_test_case(
            'person-vehicle-bike-detection',
            'person-vehicle-bike-detection-2000',
            os.path.dirname(__file__) + '/../../../data/airport/annotation_example_train.json',
            os.path.dirname(__file__) + '/../../../data/airport/train'
        )
):
    """ Test case for person-vehicle-bike-detection-2000 model. """


class PersonVehicleBikeDetection2001TestCase(
        create_test_case(
            'person-vehicle-bike-detection',
            'person-vehicle-bike-detection-2001',
            os.path.dirname(__file__) + '/../../../data/airport/annotation_example_train.json',
            os.path.dirname(__file__) + '/../../../data/airport/train'
        )
):
    """ Test case for person-vehicle-bike-detection-2001 model. """


class PersonVehicleBikeDetection2002TestCase(
        create_test_case(
            'person-vehicle-bike-detection',
            'person-vehicle-bike-detection-2002',
            os.path.dirname(__file__) + '/../../../data/airport/annotation_example_train.json',
            os.path.dirname(__file__) + '/../../../data/airport/train'
        )
):
    """ Test case for person-vehicle-bike-detection-2002 model. """
