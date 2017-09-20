from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.epil import epil


def test_epil():
  """Test module epil.py by downloading
   epil.csv and testing shape of
   extracted data has 236 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = epil(test_path)
  try:
    assert x_train.shape == (236, 9)
  except:
    shutil.rmtree(test_path)
    raise()
