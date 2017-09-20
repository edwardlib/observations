from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lanza import lanza


def test_lanza():
  """Test module lanza.py by downloading
   lanza.csv and testing shape of
   extracted data has 198 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lanza(test_path)
  try:
    assert x_train.shape == (198, 3)
  except:
    shutil.rmtree(test_path)
    raise()
