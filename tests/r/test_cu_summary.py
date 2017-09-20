from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cu_summary import cu_summary


def test_cu_summary():
  """Test module cu_summary.py by downloading
   cu_summary.csv and testing shape of
   extracted data has 117 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cu_summary(test_path)
  try:
    assert x_train.shape == (117, 5)
  except:
    shutil.rmtree(test_path)
    raise()
