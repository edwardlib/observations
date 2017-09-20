from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cgd import cgd


def test_cgd():
  """Test module cgd.py by downloading
   cgd.csv and testing shape of
   extracted data has 203 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cgd(test_path)
  try:
    assert x_train.shape == (203, 16)
  except:
    shutil.rmtree(test_path)
    raise()
