// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

class Book {
  void foo() throws IOException {
        try {
        // stuff
        } catch (AnException ex) {
			Exception g = new Exception("OMG");
            throw g;
        } catch (IOException | Exception o) {
			int i = 0;
			++i;
        }
		catch (BadException b) {
        }
  }
}
