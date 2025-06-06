# SPDX-FileCopyrightText: Copyright (c) 2020 Aibolit
# SPDX-License-Identifier: MIT
from aibolit.ast_framework import ASTNodeType, AST
from typing import List
from aibolit.ast_framework.ast_node import ASTNode


class NullCheck():
    '''
    If we check that something equals
    (or not equals) null (except in constructor)
    it is considered a pattern.
    '''
    def value(self, ast: AST) -> List[int]:
        lines: List[int] = list()
        for method_declaration in ast.get_proxy_nodes(ASTNodeType.METHOD_DECLARATION):
            for bin_operation in ast.get_subtree(method_declaration).get_proxy_nodes(ASTNodeType.BINARY_OPERATION):
                if self._check_null(bin_operation):
                    lines.append(bin_operation.operandr.line)
        return lines

    def _check_null(self, bin_operation: ASTNode) -> bool:
        return bin_operation.operator in ["==", "!="] and bin_operation.operandr.node_type == ASTNodeType.LITERAL \
            and bin_operation.operandr.value == "null"
