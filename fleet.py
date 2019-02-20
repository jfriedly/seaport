import numerical


all_ships = [330, 324, 277, 261, 244, 244, 210, 184, 163, 160, 140, 95, 95, 87, 87, 87, 87, 83, 83, 82]
low_crew = [330, 160]
high_crew = [324, 277, 261, 244, 210, 184, 140]
oil = [324, 277, 261, 244, 244, 210, 184, 163, 163, 158]
non_oil = numerical.remove_subset(all_ships, oil)
cement = [324, 277, 261, 244]
smallest = [163, 82]
custom = [324, 277, 261, 87, 87, 87]

subset_exclusions = {
       "low_crew": 1,
       "high_crew": 0,
       "oil": 0,
       "non-oil": 0,
       "cement": 0,
       "smallest": 0,
       "custom": 0,
}
subsets = {
        "low_crew": low_crew,
        "high_crew": high_crew,
        "oil": oil,
        "non-oil": non_oil,
        "cement": cement,
        "smallest": smallest,
        "custom": custom,
}
