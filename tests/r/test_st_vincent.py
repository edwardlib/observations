from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.st_vincent import st_vincent


def test_st_vincent():
  """Test module st_vincent.py by downloading
   st_vincent.csv and testing shape of
   extracted data has 324 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = st_vincent(test_path)
  try:
    assert x_train.shape == (324, 8)
  except:
    shutil.rmtree(test_path)
    raise()
