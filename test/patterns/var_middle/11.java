// SPDX-FileCopyrightText: Copyright (c) 2024-2025 Yegor Bugayenko
// SPDX-License-Identifier: MIT

package javalang.brewtab.com;

class Test {

    public PartETag uploadPart(File file, String key, String uploadId,
      int partNum) throws IOException {
      InputStream inputStream = new FileInputStream(file);
      return uploadPart(inputStream, key, uploadId, partNum, file.length());
    }
}
