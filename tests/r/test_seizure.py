from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.seizure import seizure


def test_seizure():
  """Test module seizure.py by downloading
   seizure.csv and testing shape of
   extracted data has 59 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = seizure(test_path)
  try:
    assert x_train.shape == (59, 7)
  except:
    shutil.rmtree(test_path)
    raise()
