from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cloud_seeding2 import cloud_seeding2


def test_cloud_seeding2():
  """Test module cloud_seeding2.py by downloading
   cloud_seeding2.csv and testing shape of
   extracted data has 108 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cloud_seeding2(test_path)
  try:
    assert x_train.shape == (108, 8)
  except:
    shutil.rmtree(test_path)
    raise()
