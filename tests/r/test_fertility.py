from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fertility import fertility


def test_fertility():
  """Test module fertility.py by downloading
   fertility.csv and testing shape of
   extracted data has 333 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fertility(test_path)
  try:
    assert x_train.shape == (333, 10)
  except:
    shutil.rmtree(test_path)
    raise()
