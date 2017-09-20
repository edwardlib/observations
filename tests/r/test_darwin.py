from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.darwin import darwin


def test_darwin():
  """Test module darwin.py by downloading
   darwin.csv and testing shape of
   extracted data has 15 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = darwin(test_path)
  try:
    assert x_train.shape == (15, 1)
  except:
    shutil.rmtree(test_path)
    raise()
