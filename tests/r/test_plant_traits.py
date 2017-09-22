from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.plant_traits import plant_traits


def test_plant_traits():
  """Test module plant_traits.py by downloading
   plant_traits.csv and testing shape of
   extracted data has 136 rows and 31 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = plant_traits(test_path)
  try:
    assert x_train.shape == (136, 31)
  except:
    shutil.rmtree(test_path)
    raise()
