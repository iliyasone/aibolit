// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

package javalang.brewtab.com;

class MethodChain {

    private int a;
    private int b;

    public int chain1() {
        Object a = new Object();
        DifferentMethods b = new DifferentMethods();
        b.func(a);
        return 100500;
    }

    public Object chain2() {
        ++b;
        ++a;
        return new Object();
    }
}
