from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nlschools import nlschools


def test_nlschools():
  """Test module nlschools.py by downloading
   nlschools.csv and testing shape of
   extracted data has 2287 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nlschools(test_path)
  try:
    assert x_train.shape == (2287, 6)
  except:
    shutil.rmtree(test_path)
    raise()
