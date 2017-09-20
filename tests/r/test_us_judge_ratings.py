from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_judge_ratings import us_judge_ratings


def test_us_judge_ratings():
  """Test module us_judge_ratings.py by downloading
   us_judge_ratings.csv and testing shape of
   extracted data has 43 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_judge_ratings(test_path)
  try:
    assert x_train.shape == (43, 12)
  except:
    shutil.rmtree(test_path)
    raise()
