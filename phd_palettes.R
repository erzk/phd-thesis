# all palettes used in the thesis

# four conditions - shades of green/orange
vocalisation_palette <- c("peru", "limegreen", "olivedrab4", "orangered3")

# five conditions (four main + rest)
vocalisation_palette_rest <- c("#999999", # rest
                               "peru", # perc
                               "orangered3", # silent mouthing
                               "olivedrab4", # shad
                               "limegreen") # self

# vocalisation + rest
vocalisation_palette_fnirs <- c("#999999", # gray
                                "#d95f02", # orange
                                "#1b9e77") # green

# tones (fall, rise)
tones_palette <- c("olivedrab3", "orchid3")

### vocalisation / no vocalisation
## add palettes manually: vocalisation (green), no voc (brown/orange)
## in ggpubr:
# palette = "Dark2"

## in ggplot2:
# + scale_fill_brewer(palette = "Dark2")
# + scale_color_manual(values = vocalisation_palette)