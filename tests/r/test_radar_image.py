from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.radar_image import radar_image


def test_radar_image():
  """Test module radar_image.py by downloading
   radar_image.csv and testing shape of
   extracted data has 1573 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = radar_image(test_path)
  try:
    assert x_train.shape == (1573, 5)
  except:
    shutil.rmtree(test_path)
    raise()
