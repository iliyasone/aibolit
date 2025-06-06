// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

package javalang.brewtab.com;

public class Overloaded {

    private int a;
    private float b;

    public void method(float b, int a) {
        this.a++;
    }

    public void method(Integer b, int a) {
        this.b++;
    }

    public void method3() {
        int a;
        float b;
        method(a);
        method(b);
    }
}
