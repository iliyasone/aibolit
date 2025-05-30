# SPDX-FileCopyrightText: Copyright (c) 2020 Aibolit
# SPDX-License-Identifier: MIT


from typing import List, Optional, Tuple, Dict

import javalang

from aibolit.utils.java_parser import JavalangImproved, ASTNode


class VarDeclarationDistance:
    '''
    Returns lines where variable first time used but declared more than
    specific number of lined before
    '''

    def __init__(self, lines_th: int):
        self.__lines_th = lines_th

    def __node_name(self, node) -> Optional[str]:
        qualifier = node.qualifier if hasattr(node, 'qualifier') else None
        member = node.member if hasattr(node, 'member') else None
        name = node.name if hasattr(node, 'name') else None
        return qualifier or member or name

    def __group_vars_by_method(self, items: List[Tuple[ASTNode, Optional[str]]]) -> List[Dict]:
        '''
        Group variables by method scope and calculate for each the declaration
        line and first usage line
        '''
        var_scopes: List[Dict] = []
        vars: Dict = {}
        unique_methods = list(set(
            map(lambda v: v[0].method_line, items)
        ))

        for method in unique_methods:
            method_items = map(
                lambda v: {"line": v[0].line, "name": v[1], "ntype": type(v[0].node)},
                filter(lambda v: v[0].method_line == method, items)
            )
            vars = {}
            var_scopes += [vars]
            for item in method_items:
                if item['ntype'] in [javalang.tree.MethodDeclaration]:
                    vars = {}
                    var_scopes += [vars]
                    continue

                if (item['ntype'] == javalang.tree.VariableDeclarator):
                    vars[item['name']] = {'decl': item['line'], 'first_usage': None}
                    continue

                if (item['ntype'] == javalang.tree.VariableDeclarator):
                    vars[item['name']] = {'decl': item['line']}
                    continue

                if item['name'] in vars.keys() and vars[item['name']]['first_usage'] is None:
                    vars[item['name']]['first_usage'] = item['line']

        return var_scopes

    def __line_diff(self, usage_line: int, declaration_line: int, empty_lines: List[int]) -> int:
        '''
        Calculate line difference between variable declaration and first usage
        taking into account empty lines
        '''
        lines_range = set(range(declaration_line + 1, usage_line))
        return len(lines_range.difference(empty_lines))

    def value(self, filename: str) -> List[int]:
        ''''''
        tree = JavalangImproved(filename)
        empty_lines = tree.get_empty_lines()
        items = list(
            map(lambda v: (v, self.__node_name(v.node)), tree.tree_to_nodes())
        )
        var_scopes = self.__group_vars_by_method(items)
        violations = []
        for scope in var_scopes:
            for var in scope:
                if scope[var]['first_usage'] is None:
                    continue

                line_diff = self.__line_diff(
                    scope[var]['first_usage'],
                    scope[var]['decl'],
                    empty_lines
                )
                if line_diff < self.__lines_th:
                    continue

                violations.append(scope[var]['first_usage'])

        return violations
