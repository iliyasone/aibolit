// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

class MultipleWhile {
  void bar() {
    while (true) {
      x = 1;
    }
    // more code
    while (false) {
      x = 1;
    }
  }
}
