from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snmesp import snmesp


def test_snmesp():
  """Test module snmesp.py by downloading
   snmesp.csv and testing shape of
   extracted data has 5904 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snmesp(test_path)
  try:
    assert x_train.shape == (5904, 8)
  except:
    shutil.rmtree(test_path)
    raise()
