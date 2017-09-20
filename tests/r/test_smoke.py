from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.smoke import smoke


def test_smoke():
  """Test module smoke.py by downloading
   smoke.csv and testing shape of
   extracted data has 807 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = smoke(test_path)
  try:
    assert x_train.shape == (807, 10)
  except:
    shutil.rmtree(test_path)
    raise()
