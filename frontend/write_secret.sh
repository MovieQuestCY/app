#!/bin/sh
echo "export const tmdbToken = \"$(cat /run/secrets/TMDB_API_KEY)\"" > ./src/secrets/index.ts
