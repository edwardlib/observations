from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.modelcars import modelcars


def test_modelcars():
  """Test module modelcars.py by downloading
   modelcars.csv and testing shape of
   extracted data has 12 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = modelcars(test_path)
  try:
    assert x_train.shape == (12, 2)
  except:
    shutil.rmtree(test_path)
    raise()
