from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.epi import epi


def test_epi():
  """Test module epi.py by downloading
   epi.csv and testing shape of
   extracted data has 3570 rows and 57 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = epi(test_path)
  try:
    assert x_train.shape == (3570, 57)
  except:
    shutil.rmtree(test_path)
    raise()
