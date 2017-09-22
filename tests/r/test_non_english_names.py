from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.non_english_names import non_english_names


def test_non_english_names():
  """Test module non_english_names.py by downloading
   non_english_names.csv and testing shape of
   extracted data has 11 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = non_english_names(test_path)
  try:
    assert x_train.shape == (11, 2)
  except:
    shutil.rmtree(test_path)
    raise()
