from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chem import chem


def test_chem():
  """Test module chem.py by downloading
   chem.csv and testing shape of
   extracted data has 24 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chem(test_path)
  try:
    assert x_train.shape == (24, 1)
  except:
    shutil.rmtree(test_path)
    raise()
