from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ornstein import ornstein


def test_ornstein():
  """Test module ornstein.py by downloading
   ornstein.csv and testing shape of
   extracted data has 248 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ornstein(test_path)
  try:
    assert x_train.shape == (248, 4)
  except:
    shutil.rmtree(test_path)
    raise()
