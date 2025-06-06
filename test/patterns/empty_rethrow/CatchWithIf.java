// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

class Book {
  void func() {}
  void func2() {}

  void foo() throws IOException, AnyException {
    try {
      Files.readAllBytes();
    } catch (IOException e) { // here
      int i = 0;
	  i++;
	  func();
	  func2();
	  if (true) {
	    throw e;
	  }
    }
  }
}
