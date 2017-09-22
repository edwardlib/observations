from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.minwage import minwage


def test_minwage():
  """Test module minwage.py by downloading
   minwage.csv and testing shape of
   extracted data has 612 rows and 58 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = minwage(test_path)
  try:
    assert x_train.shape == (612, 58)
  except:
    shutil.rmtree(test_path)
    raise()
