from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.empl_uk import empl_uk


def test_empl_uk():
  """Test module empl_uk.py by downloading
   empl_uk.csv and testing shape of
   extracted data has 1031 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = empl_uk(test_path)
  try:
    assert x_train.shape == (1031, 7)
  except:
    shutil.rmtree(test_path)
    raise()
