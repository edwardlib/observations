from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hair_eye_color import hair_eye_color


def test_hair_eye_color():
  """Test module hair_eye_color.py by downloading
   hair_eye_color.csv and testing shape of
   extracted data has 32 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hair_eye_color(test_path)
  try:
    assert x_train.shape == (32, 4)
  except:
    shutil.rmtree(test_path)
    raise()
