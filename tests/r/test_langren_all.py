from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.langren_all import langren_all


def test_langren_all():
  """Test module langren_all.py by downloading
   langren_all.csv and testing shape of
   extracted data has 61 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = langren_all(test_path)
  try:
    assert x_train.shape == (61, 4)
  except:
    shutil.rmtree(test_path)
    raise()
