from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.treering import treering


def test_treering():
  """Test module treering.py by downloading
   treering.csv and testing shape of
   extracted data has 7980 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = treering(test_path)
  try:
    assert x_train.shape == (7980, 2)
  except:
    shutil.rmtree(test_path)
    raise()
