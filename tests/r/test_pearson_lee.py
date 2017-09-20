from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pearson_lee import pearson_lee


def test_pearson_lee():
  """Test module pearson_lee.py by downloading
   pearson_lee.csv and testing shape of
   extracted data has 746 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pearson_lee(test_path)
  try:
    assert x_train.shape == (746, 6)
  except:
    shutil.rmtree(test_path)
    raise()
