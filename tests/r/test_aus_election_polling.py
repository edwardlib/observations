from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aus_election_polling import aus_election_polling


def test_aus_election_polling():
  """Test module aus_election_polling.py by downloading
   aus_election_polling.csv and testing shape of
   extracted data has 239 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aus_election_polling(test_path)
  try:
    assert x_train.shape == (239, 14)
  except:
    shutil.rmtree(test_path)
    raise()
