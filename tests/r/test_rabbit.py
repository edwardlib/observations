from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rabbit import rabbit


def test_rabbit():
  """Test module rabbit.py by downloading
   rabbit.csv and testing shape of
   extracted data has 60 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rabbit(test_path)
  try:
    assert x_train.shape == (60, 5)
  except:
    shutil.rmtree(test_path)
    raise()
