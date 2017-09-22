from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cpus import cpus


def test_cpus():
  """Test module cpus.py by downloading
   cpus.csv and testing shape of
   extracted data has 209 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cpus(test_path)
  try:
    assert x_train.shape == (209, 9)
  except:
    shutil.rmtree(test_path)
    raise()
