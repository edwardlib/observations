from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.charity import charity


def test_charity():
  """Test module charity.py by downloading
   charity.csv and testing shape of
   extracted data has 4268 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = charity(test_path)
  try:
    assert x_train.shape == (4268, 8)
  except:
    shutil.rmtree(test_path)
    raise()
