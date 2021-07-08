#!/bin/bash/env Rscript

suppressMessages(library(vroom))
suppressMessages(library(tidyverse))
suppressMessages(library(stringr))

args = commandArgs(trailingOnly=TRUE)

group_sim_filter <- function(file, percentage){
  
  data = suppressMessages(vroom(file, skip = 3))
  output1 = paste0(str_split(file, "\\.")[[1]][1], "_lnfd", percentage, ".txt")   # "l" stands for least functional divergent
  output2 = paste0(str_split(file, "\\.")[[1]][1], "_mnfd", percentage, ".txt")   # "m" stands for most functional divergent

  
  data$score <- as.numeric(data$score)
  
  names(data)[1] <- "site"
  
  data <- data[with(data, order(score)), ]
  
  no_of_sites <- as.integer(nrow(data)*percentage/100)
  
  per1 <- percentage/2/100
  per2 <- 1-per1
  
  index1 <- 1
  index2 <- as.integer(nrow(data)*per1)
  index3 <- as.integer(nrow(data)*per2)
  index4 <- as.integer(nrow(data))
  print(c(index1, index2, index3, index4))
  
  dat1 <- data[(index2:index3), ]$site
  dat2 <- c(data[(index1:index2), ]$site, data[(index3:index4), ]$site)

  write.table(dat1, file = output1, eol = " ", row.names = FALSE, col.names = FALSE)
  print(paste0("Writing to ", output1))
  write.table(dat2, file = output2, eol = " ", row.names = FALSE, col.names = FALSE)
  print(paste0("Writing to ", output2))
}


file = args[1]
percent = as.numeric(args[2])
suppressWarnings(group_sim_filter(file, percent))

