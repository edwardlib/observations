from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.audit import audit


def test_audit():
  """Test module audit.py by downloading
   audit.csv and testing shape of
   extracted data has 241 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = audit(test_path)
  try:
    assert x_train.shape == (241, 3)
  except:
    shutil.rmtree(test_path)
    raise()
