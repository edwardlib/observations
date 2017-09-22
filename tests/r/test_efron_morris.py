from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.efron_morris import efron_morris


def test_efron_morris():
  """Test module efron_morris.py by downloading
   efron_morris.csv and testing shape of
   extracted data has 18 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = efron_morris(test_path)
  try:
    assert x_train.shape == (18, 7)
  except:
    shutil.rmtree(test_path)
    raise()
