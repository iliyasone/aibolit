// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

class Temp extends Base
{

    private int i;

    Temp(int x)
    {
		this.i = x;
    }
    // constructor with one arguemnt.
    Temp(int x, int z, int u, int y)
    {
		this(y); this(z);
    }

    public static void main(String[] args)
    {
        // Object creation by calling no-argument
        // constructor.
        new Temp(4,5,6,7);
    }
}
