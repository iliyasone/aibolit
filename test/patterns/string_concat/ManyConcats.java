// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

package javalang.brewtab.com;

import java.util.ArrayList;

class Test {
    public void start() {
        ArrayList<Boolean> list = new ArrayList<>();

        if (true) {
            String aaa = "";
            String eeee = "";
            String i ="a" + aaa + "bbb" + eeee;
            i = "a" + aaa;
            i = aaa + "bbb";
            System.out.println("a" + aaa + "bbb");
        }
    }
}
