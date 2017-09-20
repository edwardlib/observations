from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.infmrt import infmrt


def test_infmrt():
  """Test module infmrt.py by downloading
   infmrt.csv and testing shape of
   extracted data has 102 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = infmrt(test_path)
  try:
    assert x_train.shape == (102, 12)
  except:
    shutil.rmtree(test_path)
    raise()
