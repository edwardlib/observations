from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.computers import computers


def test_computers():
  """Test module computers.py by downloading
   computers.csv and testing shape of
   extracted data has 6259 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = computers(test_path)
  try:
    assert x_train.shape == (6259, 10)
  except:
    shutil.rmtree(test_path)
    raise()
