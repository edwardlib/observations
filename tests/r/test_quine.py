from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.quine import quine


def test_quine():
  """Test module quine.py by downloading
   quine.csv and testing shape of
   extracted data has 146 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = quine(test_path)
  try:
    assert x_train.shape == (146, 5)
  except:
    shutil.rmtree(test_path)
    raise()
