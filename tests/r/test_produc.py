from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.produc import produc


def test_produc():
  """Test module produc.py by downloading
   produc.csv and testing shape of
   extracted data has 816 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = produc(test_path)
  try:
    assert x_train.shape == (816, 11)
  except:
    shutil.rmtree(test_path)
    raise()
