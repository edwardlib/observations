from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nlsy_v import nlsy_v


def test_nlsy_v():
  """Test module nlsy_v.py by downloading
   nlsy_v.csv and testing shape of
   extracted data has 400 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nlsy_v(test_path)
  try:
    assert x_train.shape == (400, 7)
  except:
    shutil.rmtree(test_path)
    raise()
