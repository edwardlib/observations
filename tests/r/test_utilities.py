from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.utilities import utilities


def test_utilities():
  """Test module utilities.py by downloading
   utilities.csv and testing shape of
   extracted data has 117 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = utilities(test_path)
  try:
    assert x_train.shape == (117, 12)
  except:
    shutil.rmtree(test_path)
    raise()
