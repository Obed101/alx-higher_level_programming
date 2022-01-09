#!/usr/bin/env bash
# This script displays the body size of a URL
curl $1 | wc -c
