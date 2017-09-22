from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pulpfiber import pulpfiber


def test_pulpfiber():
  """Test module pulpfiber.py by downloading
   pulpfiber.csv and testing shape of
   extracted data has 62 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pulpfiber(test_path)
  try:
    assert x_train.shape == (62, 8)
  except:
    shutil.rmtree(test_path)
    raise()
