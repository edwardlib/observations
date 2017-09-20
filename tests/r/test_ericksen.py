from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ericksen import ericksen


def test_ericksen():
  """Test module ericksen.py by downloading
   ericksen.csv and testing shape of
   extracted data has 66 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ericksen(test_path)
  try:
    assert x_train.shape == (66, 9)
  except:
    shutil.rmtree(test_path)
    raise()
