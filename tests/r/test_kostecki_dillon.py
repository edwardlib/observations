from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kostecki_dillon import kostecki_dillon


def test_kostecki_dillon():
  """Test module kostecki_dillon.py by downloading
   kostecki_dillon.csv and testing shape of
   extracted data has 4152 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kostecki_dillon(test_path)
  try:
    assert x_train.shape == (4152, 9)
  except:
    shutil.rmtree(test_path)
    raise()
