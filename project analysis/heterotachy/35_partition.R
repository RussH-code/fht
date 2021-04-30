rm(list = ls())

library(vroom)
library(tidyverse)
library(patchwork)

file = "35_hscore.txt"
rate_shift = "35_rateshift.txt"
partition = "35_partition_scheme.txt"

rs = vroom(rate_shift)
part = vroom(partition)

temp <- merge(rs, part, by.x="Site", by.y="Start", all.x=TRUE)
temp <- temp %>% 
  fill(c("Gene", "Ribosomal", "End")) %>%
  select(c("Site", "score", "Gene", "Ribosomal"))

df = vroom(file)
merged <- merge(temp, df, by.x="Site", by.y="site", all.x=TRUE)

df %>%
  group_by(Gene, Ribosomal) %>%
  summarise(variance = var(total)) %>%
  ggplot(aes(x=Gene, y=variance, fill=Ribosomal)) +
  geom_bar(aes(reorder(Gene, variance)), stat='identity') +
  theme(axis.text.x = element_text(angle=90, hjust=1)) +
  labs(y = 'Heterotachy Score Variance', x='', title = 'Sites variation in 35 Gene Dataset') +
  scale_fill_manual(values = c("#F1C40F", 
                                 "#5DADE2"))
total_count <- df %>%
  group_by(Gene) %>%
  summarise(count = n())

p2 <- df[df$total > 0.8, ] %>%
  group_by(Gene, Ribosomal) %>%
  summarise(n = n()) %>%
  left_join(total_count) %>%
  mutate("prop" = n/count) %>%
  ggplot(aes(x=Gene, y=prop, fill=Ribosomal)) +
  geom_bar(stat='identity') +
  theme(axis.text.x = element_text(angle=90, hjust=1)) +
  labs(y='Percentage', x='', title='Heterotachy Score over 0.8') +
  scale_fill_manual(values = c("#F1C40F", 
                               "#5DADE2"))
df[df$total > 0.7, ] %>%
  group_by(Gene, Ribosomal) %>%
  summarise(n = n()) %>%
  left_join(total_count) %>%
  mutate("prop" = n/count) %>%
  ggplot(aes(x=Gene, y=prop, fill=Ribosomal)) +
  geom_bar(stat='identity') +
  theme(axis.text.x = element_text(angle=90, hjust=1)) +
  labs(y='Percentage', x='', title='Heterotachy Score over 0.8') +
  scale_fill_manual(values = c("#F1C40F", 
                               "#5DADE2"))


p1 + p2 + plot_layout(ncol=1)

x = df[df$Ribosomal == TRUE, ]
y = df[df$Ribosomal == FALSE, ]
ttest <- t.test(x$total, y$total)
ttest$statistic

p3 <- temp %>% group_by(Gene, Ribosomal) %>% 
  summarise(mean = mean(`Rate Shift Score`)) %>%
  ggplot(aes(x=Gene, y=mean, fill=Ribosomal)) +
  geom_bar(stat="identity") +
  theme(axis.text.x = element_text(angle=90, hjust=1)) +
  labs(y='Mean Site Rate Shift', x='', title='Mean Site Rate Shift Score for 35 Gene Dataset') +
  scale_fill_manual(values = c("#F1C40F", 
                               "#5DADE2"))

p4 <- temp %>% group_by(Gene, Ribosomal) %>% 
  summarise(variance = var(`Rate Shift Score`)) %>%
  ggplot(aes(x=Gene, y=variance, fill=Ribosomal)) +
  geom_bar(stat="identity") +
  theme(axis.text.x = element_text(angle=90, hjust=1)) +
  labs(y='Variance', x='', title='Variance of Site Rate Shift Score for 35 Gene Dataset') +
  scale_fill_manual(values = c("#F1C40F", 
                               "#5DADE2"))


p3 + p4 + plot_layout(ncol=1)


merged %>% ggplot(aes(x=`Rate Shift Score`, y=total)) +
  geom_point()


head(rs)
rs[with(rs, order(score)), ]
