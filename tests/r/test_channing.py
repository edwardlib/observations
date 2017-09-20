from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.channing import channing


def test_channing():
  """Test module channing.py by downloading
   channing.csv and testing shape of
   extracted data has 462 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = channing(test_path)
  try:
    assert x_train.shape == (462, 6)
  except:
    shutil.rmtree(test_path)
    raise()
