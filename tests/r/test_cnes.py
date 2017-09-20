from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cnes import cnes


def test_cnes():
  """Test module cnes.py by downloading
   cnes.csv and testing shape of
   extracted data has 1529 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cnes(test_path)
  try:
    assert x_train.shape == (1529, 4)
  except:
    shutil.rmtree(test_path)
    raise()
