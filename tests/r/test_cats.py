from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cats import cats


def test_cats():
  """Test module cats.py by downloading
   cats.csv and testing shape of
   extracted data has 144 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cats(test_path)
  try:
    assert x_train.shape == (144, 3)
  except:
    shutil.rmtree(test_path)
    raise()
