from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.retinopathy import retinopathy


def test_retinopathy():
  """Test module retinopathy.py by downloading
   retinopathy.csv and testing shape of
   extracted data has 394 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = retinopathy(test_path)
  try:
    assert x_train.shape == (394, 9)
  except:
    shutil.rmtree(test_path)
    raise()
