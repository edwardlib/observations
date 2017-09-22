from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cloud import cloud


def test_cloud():
  """Test module cloud.py by downloading
   cloud.csv and testing shape of
   extracted data has 19 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cloud(test_path)
  try:
    assert x_train.shape == (19, 2)
  except:
    shutil.rmtree(test_path)
    raise()
