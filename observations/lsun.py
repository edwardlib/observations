from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import zipfile

from observations.util import maybe_download_and_extract


def lsun(path, category='bedroom'):
  """Load data set(s) from the Large-Scale Understanding Challenge
  (LSUN) [@yu2015lsun]. It consists of images in 10 different
  categories, each with a variable amount of training images (~100,000
  to ~3 million) and 300 validation images. There is a fixed set of
  10,000 test images.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filenames are
      `category + _train_lmdb/`, `category + _test_lmdb/`,
      `category + _val_lmdb/`.
    category: str or list of str.
      Category from LSUN. Can be one of "bedroom", "bridge",
      "church_outdoor", "classroom", "conference_room", "dining_room",
      "kitchen", "living_room", "restaurant", "tower".

  Returns:
    str. It is a message advising to load data manually.
  """
  def _maybe_download_and_extract(set_name):
    if set_name == 'test':
      target = '{}_lmdb.zip'.format(set_name)
    else:
      target = '{}_{}_lmdb.zip'.format(category, set_name)
    maybe_download_and_extract(path, url + set_name,
                               save_file_name=target)

  path = os.path.expanduser(path)
  url = 'http://lsun.cs.princeton.edu/htbin/download.cgi?tag=latest' \
        '&category={}&set='.format(category)
  if not os.path.exists(os.path.join(path, category + '_train_lmdb')):
    _maybe_download_and_extract('train')
  if not os.path.exists(os.path.join(path, 'test_lmdb')):
    _maybe_download_and_extract('test')
  if not os.path.exists(os.path.join(path, category + '_val_lmdb')):
    _maybe_download_and_extract('val')
  string = "Data set is larger than 1 GB. We recommend loading your " \
           "data in batches."
  return string
