#!/bin/bash/env Rscript

suppressMessages(library(vroom))
suppressMessages(library(tidyverse))
suppressMessages(library(stringr))

args = commandArgs(trailingOnly=TRUE)

rate_shift_filter <- function(file, percentage){
  
  data = suppressMessages(vroom(file))
  output1 = paste0(str_split(file, "\\.")[[1]][1], "_rs_top", percentage, ".txt")   
  output2 = paste0(str_split(file, "\\.")[[1]][1], "_rs_bot", 1 - percentage, ".txt") 
  names(data)[1] <- "site"
  
  data <- data[with(data, order(score)), ]
  
  no_of_sites <- as.integer(nrow(data)*percentage/100)
  
  dat1 <- sort(data[(1:no_of_sites), ]$site) 
  dat2 <- sort(data[(no_of_sites:nrow(data)), ]$site)
  
  write.table(dat1, file = output1, eol = " ", row.names = FALSE, col.names = FALSE)
  print(paste0("Writing to ", output1))
  write.table(dat2, file = output2, eol = " ", row.names = FALSE, col.names = FALSE)
  print(paste0("Writing to ", output2))
}


file = args[1]
percent = as.numeric(args[2])
suppressWarnings(rate_shift_filter(file, percent))