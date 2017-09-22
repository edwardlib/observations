from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.esoph import esoph


def test_esoph():
  """Test module esoph.py by downloading
   esoph.csv and testing shape of
   extracted data has 88 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = esoph(test_path)
  try:
    assert x_train.shape == (88, 5)
  except:
    shutil.rmtree(test_path)
    raise()
