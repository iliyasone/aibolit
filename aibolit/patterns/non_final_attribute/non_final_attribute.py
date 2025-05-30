# SPDX-FileCopyrightText: Copyright (c) 2020 Aibolit
# SPDX-License-Identifier: MIT
from aibolit.ast_framework import ASTNodeType, AST
from typing import List


class NonFinalAttribute:
    '''
    return lines of non-final attributes
    '''
    def value(self, ast: AST) -> List[int]:
        lines: List[int] = []
        for field in ast.get_proxy_nodes(ASTNodeType.FIELD_DECLARATION):
            if 'final' not in field.modifiers:
                lines.append(field.line)
        return lines
