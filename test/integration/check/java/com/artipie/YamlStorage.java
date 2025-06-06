/*
 * SPDX-FileCopyrightText: Copyright (c) 2020 artipie.com
 * SPDX-License-Identifier: MIT
 */
package com.artipie;

import com.amihaiemil.eoyaml.StrictYamlMapping;
import com.amihaiemil.eoyaml.YamlMapping;
import com.artipie.asto.Storage;
import com.artipie.asto.fs.FileStorage;
import com.artipie.asto.s3.S3Storage;
import java.net.URI;
import java.nio.file.Path;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.S3AsyncClientBuilder;

/**
 * Storage settings built from YAML.
 *
 * @since 0.2
 */
@SuppressWarnings("PMD.AvoidDuplicateLiterals")
final class YamlStorage {

    /**
     * YAML storage settings.
     */
    private final YamlMapping yaml;

    /**
     * Ctor.
     * @param yaml YAML storage settings.
     */
    YamlStorage(final YamlMapping yaml) {
        this.yaml = yaml;
    }

    /**
     * Provides a storage.
     *
     * @return Storage instance.
     */
    public Storage storage() {
        @SuppressWarnings("deprecation") final YamlMapping strict =
            new StrictYamlMapping(this.yaml);
        final String type = strict.string("type");
        final Storage storage;
        if ("fs".equals(type)) {
            storage = new FileStorage(Path.of(strict.string("path")));
        } else if ("s3".equals(type)) {
            storage = new S3Storage(
                this.s3Client(),
                strict.string("bucket"),
                !"false".equals(this.yaml.string("multipart"))
            );
        } else {
            throw new IllegalStateException(String.format("Unsupported storage type: '%s'", type));
        }
        return storage;
    }

    /**
     * Creates {@link S3AsyncClient} instance based on YAML config.
     *
     * @return Built S3 client.
     * @checkstyle MethodNameCheck (3 lines)
     */
    @SuppressWarnings("deprecation")
    private S3AsyncClient s3Client() {
        final S3AsyncClientBuilder builder = S3AsyncClient.builder();
        final String region = this.yaml.string("region");
        if (region != null) {
            builder.region(Region.of(region));
        }
        final String endpoint = this.yaml.string("endpoint");
        if (endpoint != null) {
            builder.endpointOverride(URI.create(endpoint));
        }
        return builder
            .credentialsProvider(
                credentials(new StrictYamlMapping(this.yaml).yamlMapping("credentials"))
            )
            .build();
    }

    /**
     * Creates {@link StaticCredentialsProvider} instance based on YAML config.
     *
     * @param yaml Credentials config YAML.
     * @return Credentials provider.
     */
    private static StaticCredentialsProvider credentials(final YamlMapping yaml) {
        final String type = yaml.string("type");
        if ("basic".equals(type)) {
            return StaticCredentialsProvider.create(
                AwsBasicCredentials.create(
                    yaml.string("accessKeyId"),
                    yaml.string("secretAccessKey")
                )
            );
        } else {
            throw new IllegalArgumentException(
                String.format("Unsupported S3 credentials type: %s", type)
            );
        }
    }
}
