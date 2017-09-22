from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.environmental import environmental


def test_environmental():
  """Test module environmental.py by downloading
   environmental.csv and testing shape of
   extracted data has 111 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = environmental(test_path)
  try:
    assert x_train.shape == (111, 4)
  except:
    shutil.rmtree(test_path)
    raise()
