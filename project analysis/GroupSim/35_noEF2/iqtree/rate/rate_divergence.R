rm(list = ls())
library(vroom)
library(tidyverse)
library(stringr)

file1 = "35_noEF2.rate"
file2 = "35_noEF2.out"

plot_rate_vs_fd <- function(ratefile, fdfile){
  rate = vroom(file1, skip = 8)
  fd = vroom(file2, skip = 3)
  names(fd) <- c("Site", "fd_score", "seq")
  fd$Site <- as.numeric(fd$Site)
  fd$Site <- fd$Site + 1
  
  join_df <- left_join(rate, fd, by="Site")
  join_df %>% ggplot(aes(fd_score, C_Rate)) +
    geom_point()
  
  join_df %>% 
    ggplot(aes(fd_score, Rate)) + 
    geom_point()
}



plot_rate_vs_fd(file1, file2)