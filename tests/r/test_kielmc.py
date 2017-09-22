from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kielmc import kielmc


def test_kielmc():
  """Test module kielmc.py by downloading
   kielmc.csv and testing shape of
   extracted data has 321 rows and 25 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kielmc(test_path)
  try:
    assert x_train.shape == (321, 25)
  except:
    shutil.rmtree(test_path)
    raise()
