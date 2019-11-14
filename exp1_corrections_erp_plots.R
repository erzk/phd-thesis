# corrections

# make better ERP charts - aggregated
# ERPLab doesn't seem to work as expected
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)

# load palettes for plotting
source("/media/eub/MyPassport/R_code/phd_palettes.R")

# folder with CSV files
erp_folder <- "./ERPs/ERPs/corrections_plots/"
# txt were exported from ERPLab. then were opened in Excel and saved as csv
txt_erps <- list.files(erp_folder, pattern = ".csv")
erp_path <- paste0(erp_folder, txt_erps)

# function to clean ERP csv files
clean_erp_csv <- function(x, tone, condition) {
  # clean the basename
  clean_basename <- gsub("\\.csv$", "", basename(x))
  clean_basename <- gsub("^AVG-", "", clean_basename)
    
  # assign if missing
  if (missing(tone)) {
    tone <- substr(clean_basename, nchar(clean_basename) - 3, nchar(clean_basename))
  }
  if (missing(condition)) {
    condition <- substr(clean_basename, 1, 4)
  }
  
  all_falls <- readr::read_csv(x)
  # keep the key electrodes (1-9)
  all_falls <- all_falls[,1:11]
  # remove frontal
  all_falls$Fp1 <- NULL
  # gather
  tidy_all <- all_falls %>% tidyr::gather(., key = "Electrode", value = "Amplitude", -time)
  # create factors from the electrode names
  tidy_all$Horizontal <- substr(tidy_all$Electrode, 1, 1)
  tidy_all$Horizontal <- factor(tidy_all$Horizontal, levels = c("F", "C", "P"))
  
  tidy_all$Vertical <- substr(tidy_all$Electrode, 2, 2)
  tidy_all$Vertical <- factor(tidy_all$Vertical, levels = c("3", "z", "4"))
  
  # assign a tone
  tidy_all$Tone <- tools::toTitleCase(tone) # use title case
  # assign a condition
  tidy_all$Condition <- gsub("[[:punct:]]", "", condition)
  return(tidy_all)
}

### aggregates - all conditions but self, i.e. those without 100 ms silence
# load files
erp_path[1]
all_falls_but_self <- clean_erp_csv(erp_path[1], "Fall", "all_but_self")
erp_path[2]
all_rises_but_self <- clean_erp_csv(erp_path[2], "Rise", "all_but_self")

all_but_self <- bind_rows(all_falls_but_self, all_rises_but_self)

# collapse the electrodes
all_but_self %>%
  group_by(time) %>%
  summarise(MAmp = mean(Amplitude))

# and tones
all_but_self %>%
  group_by(time, Tone) %>%
  summarise(MAmp = mean(Amplitude))

ggplot(all_but_self %>%
         group_by(time, Tone) %>%
         summarise(Amplitude = mean(Amplitude)),
       aes(x = time, y = Amplitude, col = Tone)) +
  geom_line() +
  labs(x = "Time (ms)", y = "Amplitude (μM)") +
  theme_bw() +
  theme(legend.position = "top")

#### plots
ggplot(all_but_self, aes(x = time, y = Amplitude, col = Tone)) +
  geom_line() +
  facet_grid(Horizontal~Vertical) +
  labs(x = "Time (ms)", y = "Amplitude (μM)") +
  theme_bw() +
  theme(legend.position = "top")

### individual conditions ###
# define data frame
all_conditions <- data.frame()
# loop
for (i in 3:10) {
  print(erp_path[i])
  temp_df <- clean_erp_csv(erp_path[i])
  all_conditions <- bind_rows(all_conditions, temp_df)
}
# clean names
all_conditions$Condition <- 
  dplyr::recode(all_conditions$Condition,
              perc = "Perception",
              self = "Self-Production",
              shad = "Shadowing",
              sil = "Silent Mouthing")

# without adjustment
# plot conditions, tones and electrodes 
ggplot(all_conditions,
       aes(x = time, y = Amplitude, col = Condition)) +
  scale_color_manual(values = vocalisation_palette) +
  geom_line() +
  facet_grid(Tone~Horizontal~Vertical) +
  labs(x = "Time (ms)", y = "Amplitude (μM)") +
  theme_bw() +
  theme(legend.position = "top") +
  xlim(c(-49, 349))

# with adjustment
# remove 100 ms delay to allow aligning conditions
all_conditions_adj <- all_conditions
all_conditions_adj$time <- ifelse(all_conditions_adj$Condition != "Self-Production",
                              all_conditions_adj$time - 100,
                              all_conditions_adj$time)

# full view - to use in the thesis (appendix)
ggplot(all_conditions_adj,
       aes(x = time, y = Amplitude, col = Condition)) +
  scale_color_manual(values = vocalisation_palette) +
  geom_line() +
  facet_grid(Tone~Horizontal~Vertical) +
  labs(x = "Time (ms)", y = "Amplitude (μV)") +
  theme_bw() +
  theme(legend.position = "top") +
  xlim(c(-49, 349))

## collapse ## across electrodes
all_conditions_adj_tone_collapsed <-
  all_conditions_adj %>%
  group_by(time, Condition, Electrode) %>%
  summarise(Amplitude = mean(Amplitude))

# clean
all_conditions_adj_tone_collapsed$Horizontal <-
  substr(all_conditions_adj_tone_collapsed$Electrode, 1, 1)
all_conditions_adj_tone_collapsed$Horizontal <-
  factor(all_conditions_adj_tone_collapsed$Horizontal,
         levels = c("F", "C", "P"))

all_conditions_adj_tone_collapsed$Vertical <-
  substr(all_conditions_adj_tone_collapsed$Electrode, 2, 2)
all_conditions_adj_tone_collapsed$Vertical <-
  factor(all_conditions_adj_tone_collapsed$Vertical,
         levels = c("3", "z", "4"))

# plot
ggplot(all_conditions_adj_tone_collapsed,
       aes(x = time, y = Amplitude, col = Condition)) +
  scale_color_manual(values = vocalisation_palette) +
  geom_line() +
  facet_grid(Horizontal~Vertical) +
  labs(x = "Time (ms)", y = "Amplitude (μV)") +
  theme_bw() +
  theme(legend.position = "top") +
  xlim(c(-49, 349))

# doesn't render micro symbol in pdf :/
ggsave("exp1_erp_all_conditions_timealigned_tone_collapsed.pdf",
       width = 6, height = 6)

ggsave("exp1_erp_all_conditions_timealigned_tone_collapsed.png",
       width = 5.5, height = 5.5)
