from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.journals import journals


def test_journals():
  """Test module journals.py by downloading
   journals.csv and testing shape of
   extracted data has 180 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = journals(test_path)
  try:
    assert x_train.shape == (180, 10)
  except:
    shutil.rmtree(test_path)
    raise()
