from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wage import wage


def test_wage():
  """Test module wage.py by downloading
   wage.csv and testing shape of
   extracted data has 3000 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wage(test_path)
  try:
    assert x_train.shape == (3000, 12)
  except:
    shutil.rmtree(test_path)
    raise()
