from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.banking_crises import banking_crises


def test_banking_crises():
  """Test module banking_crises.py by downloading
   banking_crises.csv and testing shape of
   extracted data has 211 rows and 71 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = banking_crises(test_path)
  try:
    assert x_train.shape == (211, 71)
  except:
    shutil.rmtree(test_path)
    raise()
