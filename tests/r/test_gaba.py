from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gaba import gaba


def test_gaba():
  """Test module gaba.py by downloading
   gaba.csv and testing shape of
   extracted data has 9 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gaba(test_path)
  try:
    assert x_train.shape == (9, 7)
  except:
    shutil.rmtree(test_path)
    raise()
