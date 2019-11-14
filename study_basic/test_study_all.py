# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 上午12:04
# @Author  : chester.wang
# @Email   : wangtongpenng@126.com
from unittest import TestCase


# @File    : test_study_all.py
class TestStudyAll(TestCase):

    def test_all_not_prevent_any_symbols(self):
        import study_all
        'baz' in study_all.__all__
        self.assertIn('bza', study_all.__all__)
        from study_all import baz

    def test_all_not_prevent_dir_and_vars_include_any_symbols(self):
        import study_all
        self.assertIn('baz', vars(study_all))
        self.assertIn('baz', dir(study_all))
