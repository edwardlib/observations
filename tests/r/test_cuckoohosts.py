from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cuckoohosts import cuckoohosts


def test_cuckoohosts():
  """Test module cuckoohosts.py by downloading
   cuckoohosts.csv and testing shape of
   extracted data has 10 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cuckoohosts(test_path)
  try:
    assert x_train.shape == (10, 12)
  except:
    shutil.rmtree(test_path)
    raise()
