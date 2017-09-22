from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.puromycin import puromycin


def test_puromycin():
  """Test module puromycin.py by downloading
   puromycin.csv and testing shape of
   extracted data has 23 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = puromycin(test_path)
  try:
    assert x_train.shape == (23, 3)
  except:
    shutil.rmtree(test_path)
    raise()
