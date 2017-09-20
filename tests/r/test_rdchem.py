from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rdchem import rdchem


def test_rdchem():
  """Test module rdchem.py by downloading
   rdchem.csv and testing shape of
   extracted data has 32 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rdchem(test_path)
  try:
    assert x_train.shape == (32, 8)
  except:
    shutil.rmtree(test_path)
    raise()
