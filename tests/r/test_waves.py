from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.waves import waves


def test_waves():
  """Test module waves.py by downloading
   waves.csv and testing shape of
   extracted data has 18 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = waves(test_path)
  try:
    assert x_train.shape == (18, 2)
  except:
    shutil.rmtree(test_path)
    raise()
