from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fars import fars


def test_fars():
  """Test module fars.py by downloading
   fars.csv and testing shape of
   extracted data has 151158 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fars(test_path)
  try:
    assert x_train.shape == (151158, 17)
  except:
    shutil.rmtree(test_path)
    raise()
