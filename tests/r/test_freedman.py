from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.freedman import freedman


def test_freedman():
  """Test module freedman.py by downloading
   freedman.csv and testing shape of
   extracted data has 110 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = freedman(test_path)
  try:
    assert x_train.shape == (110, 4)
  except:
    shutil.rmtree(test_path)
    raise()
