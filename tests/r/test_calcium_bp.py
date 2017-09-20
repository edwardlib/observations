from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.calcium_bp import calcium_bp


def test_calcium_bp():
  """Test module calcium_bp.py by downloading
   calcium_bp.csv and testing shape of
   extracted data has 21 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = calcium_bp(test_path)
  try:
    assert x_train.shape == (21, 2)
  except:
    shutil.rmtree(test_path)
    raise()
