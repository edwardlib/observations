from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.infant_mortality import infant_mortality


def test_infant_mortality():
  """Test module infant_mortality.py by downloading
   infant_mortality.csv and testing shape of
   extracted data has 9 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = infant_mortality(test_path)
  try:
    assert x_train.shape == (9, 2)
  except:
    shutil.rmtree(test_path)
    raise()
