from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cancer import cancer


def test_cancer():
  """Test module cancer.py by downloading
   cancer.csv and testing shape of
   extracted data has 228 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cancer(test_path)
  try:
    assert x_train.shape == (228, 10)
  except:
    shutil.rmtree(test_path)
    raise()
