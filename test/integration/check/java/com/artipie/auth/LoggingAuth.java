/*
 * SPDX-FileCopyrightText: Copyright (c) 2020 artipie.com
 * SPDX-License-Identifier: MIT
 */

package com.artipie.auth;

import com.artipie.http.auth.Authentication;
import com.jcabi.log.Logger;
import java.util.Optional;
import java.util.logging.Level;

/**
 * Loggin implementation of {@link LoggingAuth}.
 * @since 0.9
 */
public final class LoggingAuth implements Authentication {

    /**
     * Origin authentication.
     */
    private final Authentication origin;

    /**
     * Log level.
     */
    private final Level level;

    /**
     * Decorates {@link Authentication} with {@code INFO} logger.
     * @param origin Authentication
     */
    public LoggingAuth(final Authentication origin) {
        this(origin, Level.INFO);
    }

    /**
     * Decorates {@link Authentication} with logger.
     * @param origin Origin auth
     * @param level Log level
     */
    public LoggingAuth(final Authentication origin, final Level level) {
        this.origin = origin;
        this.level = level;
    }

    @Override
    public Optional<String> user(final String username, final String password) {
        final Optional<String> res = this.origin.user(username, password);
        if (res.isEmpty()) {
            Logger.log(this.level, this.origin, "Failed to authenticate '%s' user", username);
        } else {
            Logger.log(this.level, this.origin, "Successfully authenticated '%s' user", username);
        }
        return res;
    }
}
