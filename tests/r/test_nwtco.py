from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nwtco import nwtco


def test_nwtco():
  """Test module nwtco.py by downloading
   nwtco.csv and testing shape of
   extracted data has 4028 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nwtco(test_path)
  try:
    assert x_train.shape == (4028, 9)
  except:
    shutil.rmtree(test_path)
    raise()
