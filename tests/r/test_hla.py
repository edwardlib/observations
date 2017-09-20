from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hla import hla


def test_hla():
  """Test module hla.py by downloading
   hla.csv and testing shape of
   extracted data has 271 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hla(test_path)
  try:
    assert x_train.shape == (271, 8)
  except:
    shutil.rmtree(test_path)
    raise()
