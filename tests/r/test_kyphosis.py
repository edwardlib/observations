from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kyphosis import kyphosis


def test_kyphosis():
  """Test module kyphosis.py by downloading
   kyphosis.csv and testing shape of
   extracted data has 81 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kyphosis(test_path)
  try:
    assert x_train.shape == (81, 4)
  except:
    shutil.rmtree(test_path)
    raise()
