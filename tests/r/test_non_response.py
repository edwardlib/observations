from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.non_response import non_response


def test_non_response():
  """Test module non_response.py by downloading
   non_response.csv and testing shape of
   extracted data has 12 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = non_response(test_path)
  try:
    assert x_train.shape == (12, 4)
  except:
    shutil.rmtree(test_path)
    raise()
