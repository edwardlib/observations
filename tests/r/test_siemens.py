from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.siemens import siemens


def test_siemens():
  """Test module siemens.py by downloading
   siemens.csv and testing shape of
   extracted data has 6146 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = siemens(test_path)
  try:
    assert x_train.shape == (6146, 1)
  except:
    shutil.rmtree(test_path)
    raise()
