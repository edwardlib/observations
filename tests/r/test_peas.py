from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.peas import peas


def test_peas():
  """Test module peas.py by downloading
   peas.csv and testing shape of
   extracted data has 700 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = peas(test_path)
  try:
    assert x_train.shape == (700, 2)
  except:
    shutil.rmtree(test_path)
    raise()
