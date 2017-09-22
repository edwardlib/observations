from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.capability import capability


def test_capability():
  """Test module capability.py by downloading
   capability.csv and testing shape of
   extracted data has 75 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = capability(test_path)
  try:
    assert x_train.shape == (75, 1)
  except:
    shutil.rmtree(test_path)
    raise()
