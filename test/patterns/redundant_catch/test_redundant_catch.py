# SPDX-FileCopyrightText: Copyright (c) 2020 Aibolit
# SPDX-License-Identifier: MIT

import os
from unittest import TestCase

from aibolit.patterns.redundant_catch.redundant_catch import RedundantCatch
from aibolit.ast_framework import AST
from aibolit.utils.ast_builder import build_ast


class RedundantCatchTestCase(TestCase):
    def test_simple(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/Simple.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [3])

    def test_both_catches(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/BothCatches.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [3])

    def test_fake(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/TrickyFake.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_try_inside_anonymous(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/TryInsideAnonymous.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [6, 14])

    def test_multiple_catch(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/MultipleCatch.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [3])

    def test_sequential_catch(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/SequentialCatch.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [3])

    def test_sequential_catch_try(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/SequentialCatchTry.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [3, 10])

    def test_try_inside_catch(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/TryInsideCatch.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [7])

    def test_try_inside_finally(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/TryInsideFinally.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [8])

    def test_try_inside_try(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/TryInsideTry.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [5])

    def test_catch_with_functions(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/CatchWithFunctions.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [6])

    def test_catch_with_similar_name(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/NotThrow.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [256])

    def test_try_without_throws(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/ExcelReader.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_try_in_constructor(self):
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/ExcelAnalyserImpl.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [43])

    def test_fake_try_in_lambda(self):
        """
        If function has throws, the pattern shouldn't be recognized
        if the same exception is caught in anonymous lambda
        """
        pattern = RedundantCatch()
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/Cache.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        lines = pattern.value(ast)
        self.assertEqual(lines, [])
