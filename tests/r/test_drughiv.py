from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.drughiv import drughiv


def test_drughiv():
  """Test module drughiv.py by downloading
   drughiv.csv and testing shape of
   extracted data has 34 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = drughiv(test_path)
  try:
    assert x_train.shape == (34, 3)
  except:
    shutil.rmtree(test_path)
    raise()
