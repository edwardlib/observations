from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.french_fries import french_fries


def test_french_fries():
  """Test module french_fries.py by downloading
   french_fries.csv and testing shape of
   extracted data has 696 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = french_fries(test_path)
  try:
    assert x_train.shape == (696, 9)
  except:
    shutil.rmtree(test_path)
    raise()
