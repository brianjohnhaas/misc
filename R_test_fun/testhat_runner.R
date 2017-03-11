#!/usr/bin/env Rscript

library(testthat)
source('example.R')

test_dir('tests', reporter = 'Summary')

