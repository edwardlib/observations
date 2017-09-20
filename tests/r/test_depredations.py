from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.depredations import depredations


def test_depredations():
  """Test module depredations.py by downloading
   depredations.csv and testing shape of
   extracted data has 434 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = depredations(test_path)
  try:
    assert x_train.shape == (434, 5)
  except:
    shutil.rmtree(test_path)
    raise()
