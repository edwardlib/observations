from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gestation import gestation


def test_gestation():
  """Test module gestation.py by downloading
   gestation.csv and testing shape of
   extracted data has 1236 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gestation(test_path)
  try:
    assert x_train.shape == (1236, 23)
  except:
    shutil.rmtree(test_path)
    raise()
