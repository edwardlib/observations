from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rice import rice


def test_rice():
  """Test module rice.py by downloading
   rice.csv and testing shape of
   extracted data has 72 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rice(test_path)
  try:
    assert x_train.shape == (72, 7)
  except:
    shutil.rmtree(test_path)
    raise()
