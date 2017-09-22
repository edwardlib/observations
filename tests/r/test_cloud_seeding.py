from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cloud_seeding import cloud_seeding


def test_cloud_seeding():
  """Test module cloud_seeding.py by downloading
   cloud_seeding.csv and testing shape of
   extracted data has 28 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cloud_seeding(test_path)
  try:
    assert x_train.shape == (28, 7)
  except:
    shutil.rmtree(test_path)
    raise()
