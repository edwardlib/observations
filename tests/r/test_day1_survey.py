from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.day1_survey import day1_survey


def test_day1_survey():
  """Test module day1_survey.py by downloading
   day1_survey.csv and testing shape of
   extracted data has 43 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = day1_survey(test_path)
  try:
    assert x_train.shape == (43, 13)
  except:
    shutil.rmtree(test_path)
    raise()
