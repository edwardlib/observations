from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.coal_miners import coal_miners


def test_coal_miners():
  """Test module coal_miners.py by downloading
   coal_miners.csv and testing shape of
   extracted data has 36 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = coal_miners(test_path)
  try:
    assert x_train.shape == (36, 4)
  except:
    shutil.rmtree(test_path)
    raise()
