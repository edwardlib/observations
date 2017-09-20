from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.faithful import faithful


def test_faithful():
  """Test module faithful.py by downloading
   faithful.csv and testing shape of
   extracted data has 272 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = faithful(test_path)
  try:
    assert x_train.shape == (272, 2)
  except:
    shutil.rmtree(test_path)
    raise()
