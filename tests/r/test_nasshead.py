from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nasshead import nasshead


def test_nasshead():
  """Test module nasshead.py by downloading
   nasshead.csv and testing shape of
   extracted data has 56 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nasshead(test_path)
  try:
    assert x_train.shape == (56, 3)
  except:
    shutil.rmtree(test_path)
    raise()
